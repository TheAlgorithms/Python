"""
continuation of rsa_encryption.py file
here in this script we will decryt the rsa cipher
"""

from base64 import b64decode, b64encode

from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import MD5, SHA, SHA256, SHA384, SHA512
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

hash = "SHA-256"


def newkeys(keysize):
    random_generator = Random.new().read
    key = RSA.generate(keysize, random_generator)
    private, public = key, key.publickey()
    return public, private


def importKey(externKey):
    return RSA.importKey(externKey)


def getpublickey(priv_key):
    return priv_key.publickey()


def encrypt(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    return cipher.encrypt(message)


def decrypt(ciphertext, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    return cipher.decrypt(ciphertext)


"""
  For public key cryptography or asymmetric key cryptography,
  it is important to maintain two important features namely
  `Authentication` and `Authorization`.
 """
# Authorization
def sign(message, priv_key, hashAlg="SHA-256"):
    global hash
    hash = hashAlg
    signer = PKCS1_v1_5.new(priv_key)

    if hash == "SHA-512":
        digest = SHA512.new()
    elif hash == "SHA-384":
        digest = SHA384.new()
    elif hash == "SHA-256":
        digest = SHA256.new()
    elif hash == "SHA-1":
        digest = SHA.new()
    else:
        digest = MD5.new()
    digest.update(message)
    return signer.sign(digest)


# Authentication
def verify(message, signature, pub_key):
    signer = PKCS1_v1_5.new(pub_key)
    if hash == "SHA-512":
        digest = SHA512.new()
    elif hash == "SHA-384":
        digest = SHA384.new()
    elif hash == "SHA-256":
        digest = SHA256.new()
    elif hash == "SHA-1":
        digest = SHA.new()
    else:
        digest = MD5.new()
    digest.update(message)
    return signer.verify(digest, signature)
