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

from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii
from hashlib import sha512

# Generate 1024-bit RSA key-pair
keyPair = RSA.generate(bits=1024)
print(f"Public key:  (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")

#pubKey = hex(keyPair.e)
pubKey = keyPair.publickey()


# RSA sign the message
msg = b'Aayush, focus please!'
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
signature = pow(hash, keyPair.d, keyPair.n)
print("Signature:", hex(signature))

# RSA verify signature
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
print("Signature valid:", hash == hashFromSignature)


# Sign the message using the PKCS#1 v1.5 signature scheme (RSASP1)
msg = b'Aayush, focus please!'

hash = SHA256.new(msg)
signer = PKCS115_SigScheme(keyPair)
signature = signer.sign(hash)
print("Signature:", binascii.hexlify(signature))

# Verify valid PKCS#1 v1.5 signature (RSAVP1)
msg = b'Aayush, focus please!'
hash = SHA256.new(msg)
verifier = PKCS115_SigScheme(pubKey)
try:
	verifier.verify(hash, signature)
	print("Signature is valid.")
except:
	print("Signature is invalid.")
	
# Verify invalid PKCS#1 v1.5 signature (RSAVP1)
msg = b'A tampered message'
hash = SHA256.new(msg)
verifier = PKCS115_SigScheme(pubKey)
try:
	verifier.verify(hash, signature)
	print("Signature is valid.")
except:
	print("Signature is invalid.")