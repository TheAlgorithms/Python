# -*- coding: utf-8 -*-


def KSA(key):
    l = len(key)
    # Create a 256-square conversion table S from key
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % l]) % 256
        S[i], S[j] = S[j], S[i]
    return S


def PRGA(S):
    # Return a generator that spits out numbers one byte at a time while updating S
    i, j = 0, 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(m, key):
    keystream = PRGA(KSA(key))
    return bytes(i ^ j for i, j in zip(m, keystream))


# Prepare the key and message
key = b"this_is_key"
message = b"this_is_message"

# Encrypt and decrypt
print("key: %r (%d bits)" % (key, len(key) * 8))
print("message: %r" % message)
ciphertext = RC4(message, key)
print("ciphertext: %r" % ciphertext)
message2 = RC4(ciphertext, key)
print("message2: %r" % message2)
