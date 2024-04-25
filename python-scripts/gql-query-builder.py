import json
from enum import Enum

import requests
from loguru import logger


class EnvironmentType(Enum):
    dev = "dev"
    stage = "stg"
    prod = "prod"



class GqlQueryBuilder:
    def __init__(self):
        self.merged_queries = {}

    def merge_common_parts(self, field_list):
        for field in field_list:
            parts = field.split('.')
            current_query = self.merged_queries

            for i, part in enumerate(parts):
                if part not in current_query:
                    current_query[part] = {}
                current_query = current_query[part]
                if i == len(parts) - 1:
                    current_query['__leaf__'] = True

    def generate_query_from_merged(self):
        def construct_query(query_obj, indentation=''):
            query = ''
            for key, value in query_obj.items():
                if '__leaf__' in value:
                    query += indentation + key + '\n'
                else:
                    query += indentation + key + ' {\n'
                    query += construct_query(value, indentation + '  ')
                    query += indentation + '}\n'
            return query

        return construct_query(self.merged_queries)

    def generate_graphql_query(self, item_id=None, product_id=None, field_list=None):
        self.merge_common_parts(field_list)
        if item_id and product_id:
            query_item = 'itemId: "{}", productId: {}'.format(item_id, product_id)
        elif item_id:
            query_item = 'itemId: "{}"'.format(item_id)
        elif product_id:
            query_item = 'productId: "{}"'.format(product_id)
        else:
            raise ValueError("Either item_id or product_id must be provided.")
        graphql_query = '{{product({}) {{ \n  ... on '.format(query_item)
        graphql_query += self.generate_query_from_merged()
        graphql_query += '... on MissingProductDetail {	\n message \n code \n ids \n} \n}}\n'
        return graphql_query


class GqlApiRequest:
    # def __init__(self, env="stage", product_id=None,
    #              _id="6279", item_id="", query_builder=None, payload=None):
    def __init__(self, env="stage", product_id=None,
             item_id="", query_builder=None, payload=None):
        self.url = f'https://{env}.girishcodealchemy.net/graphql'
        self.headers = {
            "Content-Type": "application/json",
            "svc.env": EnvironmentType[env].value,
            "svc.version": "1.0.0",
        }

        self.product_id = product_id
        self.item_id = item_id
        self.payload = payload

        if query_builder:
            gql_builder = GqlQueryBuilder()
            self.payload = gql_builder.generate_graphql_query(
                item_id=item_id,
                product_id=product_id,
                field_list=query_builder)

    def execute(self):
        # Make the HTTP POST request
        logger.info(f"******* GQL URL: {self.url}")
        logger.info(f"******* GQL Query: \n{self.payload}")
        response = requests.post(url=self.url,
                                 json={"query": self.payload},
                                 headers=self.headers, verify=False)

        # Print the response content
        logger.info(f"******** GQL response: \n{json.dumps(response.json(), indent=4)}")
        return response.json()

# Example usage
if __name__ == "__main__":
    item_id = "123"
    # product_id="245"
    query_builder = [
        "Product.itemGroups.Offers.Item.ItemStatus",
        "Product.itemGroups.onlineOffers.Item.ItemStatus",
        "Product.manufacturingInfo.disclaimers.type",
        "Product.systemTimestamp",
        "Product.productId",
        "Product.productType"
    ]

    gql_request = GqlApiRequest(env="stage", item_id=item_id, payload=None, query_builder=query_builder)
    gql_request.execute()