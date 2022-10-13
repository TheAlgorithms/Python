# Contributed by @Shah-Aayush
# Signing and Verifying with Detection of Tempering.

"""
# Signing and verifying with detection of tempering
- What is signing in blockchain?
> Digital Signing in Blockchain is a process to verify the user's impressions of the transaction. It uses the private key to sign the digital transaction, and its corresponding public key will help to authorize the sender. However, in this way, anyone with the sender's public key can easily decrypt the document.
- What is tampering ?
> A blockchain network uses a distributed ledger system to record transaction data with timestamps and in chronological order. To tamper with such data, the attacker will have to change the information across all the ledgers – all the way back to the very first block.
- How the data is tamper proof in blockchain?
> Each block is connected to all the blocks before and after it. This makes it difficult to tamper with a single record because a hacker would need to change the block containing that record as well as those linked to it to avoid detection.
"""

# installed `pycryptodome` with `pip install pycryptodome`

import binascii
from hashlib import sha512

# uncomment below lines after installing `pycryptodome`.
# from Crypto.Hash import SHA256
# from Crypto.PublicKey import RSA
# from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme

# Remove below code after uncommenting above lines
# start removing...
class RSA:
    def generate(bits:str)->str:
        return bits


class SHA256:
    def new(hash:str)->str:
        return hash


class PKCS115_SigScheme:
    def generate(data:str)->str:
        return data

class Test:
    print("Sample output is here")
    """
Public key:  (n=0xd58fca3c762dbdc6ae214a6acafd4a29801e4ff13bb953ce5643678443053803d2395a075c0f71adf1b784a4b2b8b7fd6179e33fa4d2ff884e71458e1b46704f3daa7ad8930e6b6e978eea8d5259b5c32bcde2a3068225d6ba1b33aad6432ae0737e30b16df7894a5541510c91e88e6810caf05f10d69169e8fb224a8c73d7b9, e=0x10001)
Private key: (n=0xd58fca3c762dbdc6ae214a6acafd4a29801e4ff13bb953ce5643678443053803d2395a075c0f71adf1b784a4b2b8b7fd6179e33fa4d2ff884e71458e1b46704f3daa7ad8930e6b6e978eea8d5259b5c32bcde2a3068225d6ba1b33aad6432ae0737e30b16df7894a5541510c91e88e6810caf05f10d69169e8fb224a8c73d7b9, d=0x686ed84698c3e579b2cd34c6e45cd85752ff7fb847ac68ff0dd0085ef527282d3630358643ce8998b60b38221203a27595a5352b7a3e741703c5006e6d881482c66a4faa7fb6aa0607b2e46fc7c5d0a6e655d21844e05b6c714c23db1b2e9565b3b1aa47baa05908cb4729156d08907d8d0101b9953013f2c2e60c105ac7281)
Signature: 0x4dadb7ca1e9867ff5a8502ae5160375c82cfefec26265b97adcc754111da113e4355f7bd3eeeedc7c793d9f13004aeee47974611cb840092f9791b38a9f177df82fb5d9931bc59b70bcd1a42f1bd1bc6a4d26d84fdf1e5289f72311bec7fb34a8d125d0e2c2994cca9a9e05a07f10f72a146f6b8bc04cb5bfe324946b6db8d89
Signature valid: True
Signature: b'3700ad70dcb486d780461bbc810ab15687b34d670a8e55c607e948a37e9d2280839f89d5c0e0e972c617ea3ab36607e2018de8d335bf081e5dfc1ea17df8a85fc5d0824de9d1e11f4e40e35e6b2425ac1fc38a71569ab4af36a521d821849d999a9096c50fc78104f31cdf673371b038446e9cee8b03529f38dc104ddcd7206c'
Signature is valid.
Signature is invalid.
    """

# end

# Generate 1024-bit RSA key-pair
key_pair = RSA.generate(bits=1024)
print(f"Public key:  (n={hex(key_pair.n)}, e={hex(key_pair.e)})")
print(f"Private key: (n={hex(key_pair.n)}, d={hex(key_pair.d)})")

# pub_key = hex(key_pair.e)
pub_key = key_pair.publickey()


# RSA sign the message
msg = b"Aayush, focus please!"
hash = int.from_bytes(sha512(msg).digest(), byteorder="big")
signature = pow(hash, key_pair.d, key_pair.n)
print("Signature:", hex(signature))

# RSA verify signature
hash_from_signature = pow(signature, key_pair.e, key_pair.n)
print("Signature valid:", hash == hash_from_signature)


# Sign the message using the PKCS#1 v1.5 signature scheme (RSASP1)
msg = b"Aayush, focus please!"

hash = SHA256.new(msg)
signer = PKCS115_SigScheme(key_pair)
signature = signer.sign(hash)
print("Signature:", binascii.hexlify(signature))

# Verify valid PKCS#1 v1.5 signature (RSAVP1)
msg = b"Aayush, focus please!"
hash = SHA256.new(msg)
verifier = PKCS115_SigScheme(pub_key)
try:
    verifier.verify(hash, signature)
    print("Signature is valid.")
except:
    print("Signature is invalid.")

# Verify invalid PKCS#1 v1.5 signature (RSAVP1)
msg = b"A tampered message"
hash = SHA256.new(msg)
verifier = PKCS115_SigScheme(pub_key)
try:
    verifier.verify(hash, signature)
    print("Signature is valid.")
except:
    print("Signature is invalid.")
