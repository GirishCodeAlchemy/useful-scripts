import base64

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# Example Base64-encoded private key (PEM format)
base64_encoded_key = """
sdfasdaf...
"""

# Remove any surrounding whitespace or newline characters
base64_encoded_key = base64_encoded_key.strip()

# Decode the Base64 string
decoded_key_bytes = base64.b64decode(base64_encoded_key)

# Load the private key
private_key = serialization.load_pem_private_key(
    decoded_key_bytes,
    password=None,
    backend=default_backend()
)

pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
print(pem_private_key.decode('utf-8'))
# Print the private key details (just as an example)
# print(private_key)
