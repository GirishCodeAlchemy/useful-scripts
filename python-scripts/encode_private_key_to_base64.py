import base64

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


# Function to load a private key from a PEM file
def load_pem_private_key(pem_file_path):
    with open(pem_file_path, 'rb') as pem_file:
        pem_data = pem_file.read()
        private_key = serialization.load_pem_private_key(
            pem_data,
            password=None,
            backend=default_backend()
        )
    return private_key

# Function to convert a private key to a Base64-encoded string
def private_key_to_base64(private_key):
    pem_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    base64_encoded_key = base64.b64encode(pem_private_key).decode('utf-8')
    return base64_encoded_key

# Example usage
pem_file_path = 'private-key.pem'  # Replace with your PEM file path
private_key = load_pem_private_key(pem_file_path)
base64_encoded_key = private_key_to_base64(private_key)

# Print the Base64-encoded private key
print(base64_encoded_key)
