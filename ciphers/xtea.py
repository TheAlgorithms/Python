"""
XTEA (eXtended Tiny Encryption Algorithm) is a block cipher designed to
correct weaknesses in TEA. It was published by David Wheeler and Roger
Needham in 1997. XTEA operates on 64-bit blocks with a 128-bit key and
uses a Feistel network with a recommended 64 rounds.

It's still found in embedded systems and game networking protocols due
to its simplicity and small code footprint.

Reference: https://en.wikipedia.org/wiki/XTEA
"""

import struct

DELTA = 0x9E3779B9
MASK = 0xFFFFFFFF


def xtea_encrypt(
    block: bytes, key: bytes, num_rounds: int = 64
) -> bytes:
    """
    Encrypt a single 64-bit block using XTEA.

    :param block: 8 bytes of plaintext
    :param key: 16 bytes (128-bit key)
    :param num_rounds: number of Feistel rounds (default 64)
    :return: 8 bytes of ciphertext

    >>> key = b'\\x00' * 16
    >>> plaintext = b'\\x00' * 8
    >>> ciphertext = xtea_encrypt(plaintext, key)
    >>> ciphertext.hex()
    'fc924d124ad0ed50'

    >>> xtea_encrypt(b'hello!!!', b'sixteenbyteskey!')
    b'u\\x8d\\x00\\x17c\\xb8\\xf0*'

    >>> xtea_encrypt(b'short', key)
    Traceback (most recent call last):
        ...
    ValueError: block must be 8 bytes

    >>> xtea_encrypt(plaintext, b'short')
    Traceback (most recent call last):
        ...
    ValueError: key must be 16 bytes
    """
    if len(block) != 8:
        raise ValueError("block must be 8 bytes")
    if len(key) != 16:
        raise ValueError("key must be 16 bytes")

    v0, v1 = struct.unpack("!II", block)
    k = struct.unpack("!4I", key)

    total = 0
    for _ in range(num_rounds):
        v0 = (v0 + ((((v1 << 4) ^ (v1 >> 5)) + v1) ^ (total + k[total & 3]))) & MASK
        total = (total + DELTA) & MASK
        v1 = (
            v1 + ((((v0 << 4) ^ (v0 >> 5)) + v0) ^ (total + k[(total >> 11) & 3]))
        ) & MASK

    return struct.pack("!II", v0, v1)


def xtea_decrypt(
    block: bytes, key: bytes, num_rounds: int = 64
) -> bytes:
    """
    Decrypt a single 64-bit block using XTEA.

    :param block: 8 bytes of ciphertext
    :param key: 16 bytes (128-bit key)
    :param num_rounds: number of Feistel rounds (default 64)
    :return: 8 bytes of plaintext

    Roundtrip test -- encrypt then decrypt returns original plaintext:
    >>> key = b'\\x00' * 16
    >>> plaintext = b'\\x00' * 8
    >>> xtea_decrypt(xtea_encrypt(plaintext, key), key) == plaintext
    True

    >>> msg = b'hello!!!'
    >>> k = b'sixteenbyteskey!'
    >>> xtea_decrypt(xtea_encrypt(msg, k), k) == msg
    True

    >>> xtea_decrypt(b'short', key)
    Traceback (most recent call last):
        ...
    ValueError: block must be 8 bytes

    >>> xtea_decrypt(b'\\x00' * 8, b'short')
    Traceback (most recent call last):
        ...
    ValueError: key must be 16 bytes
    """
    if len(block) != 8:
        raise ValueError("block must be 8 bytes")
    if len(key) != 16:
        raise ValueError("key must be 16 bytes")

    v0, v1 = struct.unpack("!II", block)
    k = struct.unpack("!4I", key)

    total = (DELTA * num_rounds) & MASK
    for _ in range(num_rounds):
        v1 = (
            v1 - ((((v0 << 4) ^ (v0 >> 5)) + v0) ^ (total + k[(total >> 11) & 3]))
        ) & MASK
        total = (total - DELTA) & MASK
        v0 = (v0 - ((((v1 << 4) ^ (v1 >> 5)) + v1) ^ (total + k[total & 3]))) & MASK

    return struct.pack("!II", v0, v1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
