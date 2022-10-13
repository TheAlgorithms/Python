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
    def generate(bits: str) -> str:
        return bits


class SHA256:
    def new(hash: str) -> str:
        return hash


class PKCS115_SigScheme:
    def generate(data: str) -> str:
        return data


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
