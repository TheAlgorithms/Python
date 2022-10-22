# rsa cipher encryption

# The modules included for the encryption algorithm are as follows
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512, SHA384, SHA256, SHA, MD5
from Crypto import Random
from base64 import b64encode, b64decode
hash = "SHA-256"  # We have initialized the hash value as SHA-256 for better security purpose. 

"""
We will use a function to generate new keys
or a pair of public and private key using the following code
"""
def newkeys(keysize):
   random_generator = Random.new().read
   key = RSA.generate(keysize, random_generator)
   private, public = key, key.publickey()
   return public, private

def importKey(externKey):
   return RSA.importKey(externKey)

def getpublickey(priv_key):
   return priv_key.publickey()
"""
For encryption, the following function is used which follows the RSA algorithm
Two parameters are mandatory: 
`message` and `pub_key` which refers to Public key. 
A public key is used for encryption and private key is used for decryption.
"""
def encrypt(message, pub_key):
   cipher = PKCS1_OAEP.new(pub_key)
   return cipher.encrypt(message)
