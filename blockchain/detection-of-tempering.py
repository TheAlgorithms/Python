# Contributed by @Shah-Aayush
# Signing and Verifying with Detection of Tempering.

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