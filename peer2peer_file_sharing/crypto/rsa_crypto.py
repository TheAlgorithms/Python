from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def generate_rsa_key_pair(private_path: str, public_path: str):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    
    with open(private_path, "wb") as f:
        
        f.write(private_key.private_bytes(
            serialization.Encoding.PEM,
            serialization.PrivateFormat.TraditionalOpenSSL,
            serialization.NoEncryption()
        ))
    
    with open(public_path, "wb") as f:
        
        f.write(private_key.public_key().public_bytes(
            serialization.Encoding.PEM,
            serialization.PublicFormat.SubjectPublicKeyInfo
        ))

def encrypt_with_rsa_public_key(data: bytes, public_key_path: str) -> bytes:

    with open(public_key_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    if not isinstance(public_key, rsa.RSAPublicKey):
        raise TypeError("\n[!] The loaded public key is not an RSA key.")
    
    return public_key.encrypt(
        data,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )

def decrypt_with_rsa_private_key(ciphertext: bytes, private_key_path: str) -> bytes:
    
    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    if not isinstance(private_key, rsa.RSAPrivateKey):
        raise TypeError("\n[!] The loaded private key is not an RSA key.")
    
    return private_key.decrypt(
        ciphertext,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )

def is_valid_pem_key(file_path: str, is_private: bool = False) -> bool:
    
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            if not data:
                return False
            if is_private:
                serialization.load_pem_private_key(data, password=None)
            else:
                serialization.load_pem_public_key(data)
        return True
    
    except Exception:
        return False
    