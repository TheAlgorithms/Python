"""
RSA Encryption and Decryption using the `cryptography` library.

This script demonstrates RSA encryption and decryption using the
`cryptography` library. The `cryptography` library is a package
which provides cryptographic recipes and primitives to Python
developers. It aims to support all currently supported versions
of Python.

The RSA algorithm is an asymmetric encryption algorithm, meaning
that it uses two keys: one public and one private. The public key
can be shared with everyone, while the private key must be kept
secret. In RSA, this asymmetry is based on the practical difficulty
of the factorization of the product of two large prime numbers, the
"factoring problem". The public key consists of the modulus n and
the public (or encryption) exponent e. The private key consists of
the modulus n and the private (or decryption) exponent d, which must
be kept secret. RSA is often used to encrypt session keys, which are
symmetric keys used to encrypt data in a symmetric encryption scheme.
This avoids the need to distribute a symmetric key to each party
wanting to encrypt data.

References:
- RSA Algorithm: https://en.wikipedia.org/wiki/RSA_(cryptosystem)
- cryptography library: https://cryptography.io/

"""

from doctest import testmod

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa

from typing import Tuple, Union

def generate_key_pair() -> Tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]:
    """
    Generate RSA key pair.

    Returns:
        private_key: Private key for decryption.
        public_key: Public key for encryption.

    >>> private_key, public_key = generate_key_pair()
    >>> isinstance(private_key, rsa.RSAPrivateKey)
    True
    >>> isinstance(public_key, rsa.RSAPublicKey)
    True
    """

    private_key = rsa.generate_private_key(
        public_exponent=65537, key_size=2048, backend=default_backend()
    )

    public_key = private_key.public_key()

    return private_key, public_key


def encrypt(message: str, public_key: rsa.RSAPublicKey) -> bytes:
    """
    Encrypt a message using RSA.

    Args:
        message (str): Message to be encrypted.
        public_key (rsa.RSAPublicKey): Public key for encryption.

    Returns:
        bytes: Encrypted ciphertext.

    >>> private_key, public_key = generate_key_pair()
    >>> message = "Hello, this is a message to be encrypted!" 
    >>> ciphertext = encrypt(message, public_key)
    >>> decrypted_message = decrypt(ciphertext, private_key)
    >>> decrypted_message == message
    True
    """

    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return ciphertext


def decrypt(ciphertext: bytes, private_key: rsa.RSAPrivateKey) -> str:
    """
    Decrypt a ciphertext using RSA.

    Args:
        ciphertext (bytes): Encrypted ciphertext.
        private_key (rsa.RSAPrivateKey): Private key for decryption.

    Returns:
        str: Decrypted plaintext.

    >>> private_key, public_key = generate_key_pair()
    >>> message = "Hello, this is a message to be encrypted!"
    >>> ciphertext = encrypt(message, public_key)
    >>> decrypted_message = decrypt(ciphertext, private_key)
    >>> decrypted_message == message
    True
    """

    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return plaintext.decode()


if __name__ == "__main__":
    testmod(name="generate_key_pair", verbose=True)
    testmod(name="encrypt", verbose=True)
    testmod(name="decrypt", verbose=True)
