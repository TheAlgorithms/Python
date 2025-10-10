"""
SM4 block cipher
https://en.wikipedia.org/wiki/SM4_(cipher)
"""

from __future__ import annotations

from collections.abc import Iterable

__all__ = ["BLOCK_SIZE", "SM4", "pkcs7_pad", "pkcs7_unpad"]

BLOCK_SIZE: int = 16  # block size

# S-box
SBOX: list[int] = [
    0xD6,
    0x90,
    0xE9,
    0xFE,
    0xCC,
    0xE1,
    0x3D,
    0xB7,
    0x16,
    0xB6,
    0x14,
    0xC2,
    0x28,
    0xFB,
    0x2C,
    0x05,
    0x2B,
    0x67,
    0x9A,
    0x76,
    0x2A,
    0xBE,
    0x04,
    0xC3,
    0xAA,
    0x44,
    0x13,
    0x26,
    0x49,
    0x86,
    0x06,
    0x99,
    0x9C,
    0x42,
    0x50,
    0xF4,
    0x91,
    0xEF,
    0x98,
    0x7A,
    0x33,
    0x54,
    0x0B,
    0x43,
    0xED,
    0xCF,
    0xAC,
    0x62,
    0xE4,
    0xB3,
    0x1C,
    0xA9,
    0xC9,
    0x08,
    0xE8,
    0x95,
    0x80,
    0xDF,
    0x94,
    0xFA,
    0x75,
    0x8F,
    0x3F,
    0xA6,
    0x47,
    0x07,
    0xA7,
    0xFC,
    0xF3,
    0x73,
    0x17,
    0xBA,
    0x83,
    0x59,
    0x3C,
    0x19,
    0xE6,
    0x85,
    0x4F,
    0xA8,
    0x68,
    0x6B,
    0x81,
    0xB2,
    0x71,
    0x64,
    0xDA,
    0x8B,
    0xF8,
    0xEB,
    0x0F,
    0x4B,
    0x70,
    0x56,
    0x9D,
    0x35,
    0x1E,
    0x24,
    0x0E,
    0x5E,
    0x63,
    0x58,
    0xD1,
    0xA2,
    0x25,
    0x22,
    0x7C,
    0x3B,
    0x01,
    0x21,
    0x78,
    0x87,
    0xD4,
    0x00,
    0x46,
    0x57,
    0x9F,
    0xD3,
    0x27,
    0x52,
    0x4C,
    0x36,
    0x02,
    0xE7,
    0xA0,
    0xC4,
    0xC8,
    0x9E,
    0xEA,
    0xBF,
    0x8A,
    0xD2,
    0x40,
    0xC7,
    0x38,
    0xB5,
    0xA3,
    0xF7,
    0xF2,
    0xCE,
    0xF9,
    0x61,
    0x15,
    0xA1,
    0xE0,
    0xAE,
    0x5D,
    0xA4,
    0x9B,
    0x34,
    0x1A,
    0x55,
    0xAD,
    0x93,
    0x32,
    0x30,
    0xF5,
    0x8C,
    0xB1,
    0xE3,
    0x1D,
    0xF6,
    0xE2,
    0x2E,
    0x82,
    0x66,
    0xCA,
    0x60,
    0xC0,
    0x29,
    0x23,
    0xAB,
    0x0D,
    0x53,
    0x4E,
    0x6F,
    0xD5,
    0xDB,
    0x37,
    0x45,
    0xDE,
    0xFD,
    0x8E,
    0x2F,
    0x03,
    0xFF,
    0x6A,
    0x72,
    0x6D,
    0x6C,
    0x5B,
    0x51,
    0x8D,
    0x1B,
    0xAF,
    0x92,
    0xBB,
    0xDD,
    0xBC,
    0x7F,
    0x11,
    0xD9,
    0x5C,
    0x41,
    0x1F,
    0x10,
    0x5A,
    0xD8,
    0x0A,
    0xC1,
    0x31,
    0x88,
    0xA5,
    0xCD,
    0x7B,
    0xBD,
    0x2D,
    0x74,
    0xD0,
    0x12,
    0xB8,
    0xE5,
    0xB4,
    0xB0,
    0x89,
    0x69,
    0x97,
    0x4A,
    0x0C,
    0x96,
    0x77,
    0x7E,
    0x65,
    0xB9,
    0xF1,
    0x09,
    0xC5,
    0x6E,
    0xC6,
    0x84,
    0x18,
    0xF0,
    0x7D,
    0xEC,
    0x3A,
    0xDC,
    0x4D,
    0x20,
    0x79,
    0xEE,
    0x5F,
    0x3E,
    0xD7,
    0xCB,
    0x39,
    0x48,
]

# FK
FK: list[int] = [0xA3B1BAC6, 0x56AA3350, 0x677D9197, 0xB27022DC]

# CK
CK: list[int] = [
    0x00070E15,
    0x1C232A31,
    0x383F464D,
    0x545B6269,
    0x70777E85,
    0x8C939AA1,
    0xA8AFB6BD,
    0xC4CBD2D9,
    0xE0E7EEF5,
    0xFC030A11,
    0x181F262D,
    0x343B4249,
    0x50575E65,
    0x6C737A81,
    0x888F969D,
    0xA4ABB2B9,
    0xC0C7CED5,
    0xDCE3EAF1,
    0xF8FF060D,
    0x141B2229,
    0x30373E45,
    0x4C535A61,
    0x686F767D,
    0x848B9299,
    0xA0A7AEB5,
    0xBCC3CAD1,
    0xD8DFE6ED,
    0xF4FB0209,
    0x10171E25,
    0x2C333A41,
    0x484F565D,
    0x646B7279,
]


def _rotl32(value: int, shift: int) -> int:
    """Left rotate a 32-bit value by shift bits."""
    return ((value << shift) & 0xFFFFFFFF) | ((value & 0xFFFFFFFF) >> (32 - shift))


def _bytes_to_u32_list(data: bytes) -> list[int]:
    """Convert `data` bytes to list of 32-bit unsigned integers."""
    if len(data) % 4 != 0:
        raise ValueError("bytes length must be multiple of 4")
    return [int.from_bytes(data[i : i + 4], "big") for i in range(0, len(data), 4)]


def _u32_list_to_bytes(words: Iterable[int]) -> bytes:
    """Convert iterable of 32-bit words to bytes (big-endian)."""
    return b"".join(int(w & 0xFFFFFFFF).to_bytes(4, "big") for w in words)


def _tau(word: int) -> int:
    """Non-linear byte substitution using SBOX."""
    b0 = (word >> 24) & 0xFF
    b1 = (word >> 16) & 0xFF
    b2 = (word >> 8) & 0xFF
    b3 = word & 0xFF
    return (SBOX[b0] << 24) | (SBOX[b1] << 16) | (SBOX[b2] << 8) | SBOX[b3]


def _l_transform(b: int) -> int:
    """
    Linear transform L used in the round function:
    L(B) = B ^ (B <<< 2) ^ (B <<< 10) ^ (B <<< 18) ^ (B <<< 24)
    """
    return b ^ _rotl32(b, 2) ^ _rotl32(b, 10) ^ _rotl32(b, 18) ^ _rotl32(b, 24)


def _l_transform_key(b: int) -> int:
    """
    Linear transform L':
    L'(B) = B ^ (B <<< 13) ^ (B <<< 23)
    """
    return b ^ _rotl32(b, 13) ^ _rotl32(b, 23)


class SM4:
    """
    SM4 implementation.
    Example:
        cipher = SM4(key_bytes)
        ct = cipher.encrypt_ecb(plaintext)
        pt = cipher.decrypt_ecb(ct)

    >>> key = bytes.fromhex("0123456789abcdeffedcba9876543210")
    >>> sm4 = SM4(key)
    >>> pt_block = b"0123456789abcdeF"
    >>> ct_block = sm4.encrypt_block(pt_block)
    >>> sm4.decrypt_block(ct_block) == pt_block
    True
    """

    rk: list[int]

    def __init__(self, key: bytes) -> None:
        """
        Initialize with a 16-byte key.

        :param key: 16 bytes
        :raises ValueError: if key length != 16
        """
        if len(key) != BLOCK_SIZE:
            raise ValueError("SM4 key must be 16 bytes")
        self.rk = self._key_schedule(key)

    def _key_schedule(self, key: bytes) -> list[int]:
        """Generate 32 round keys from the 128-bit key using FK and CK constants."""
        mk = _bytes_to_u32_list(key)
        k = [mk[i] ^ FK[i] for i in range(4)]
        rk: list[int] = []
        for i in range(32):
            tmp = k[1] ^ k[2] ^ k[3] ^ CK[i]
            tmp = _tau(tmp)
            tmp = _l_transform_key(tmp)
            new_k = (k[0] ^ tmp) & 0xFFFFFFFF
            rk.append(new_k)
            # rotate
            k = [k[1], k[2], k[3], new_k]
        return rk

    def encrypt_block(self, block: bytes) -> bytes:
        """
        Encrypt a single 16-byte block.

        :param block: 16 bytes
        :return: 16 byte ciphertext
        :raises ValueError: if block length != 16
        """
        if len(block) != BLOCK_SIZE:
            raise ValueError("block must be 16 bytes")

        x = _bytes_to_u32_list(block)  # X0, X1, X2, X3
        for i in range(32):
            tmp = x[1] ^ x[2] ^ x[3] ^ self.rk[i]
            t = _tau(tmp)
            t = _l_transform(t)
            new = (x[0] ^ t) & 0xFFFFFFFF
            x = [x[1], x[2], x[3], new]
        out = list(reversed(x))
        return _u32_list_to_bytes(out)

    def decrypt_block(self, block: bytes) -> bytes:
        """
        Decrypt a single 16-byte block.

        :param block: 16 bytes
        :return: 16 byte plaintext
        :raises ValueError: if block length != 16
        """
        if len(block) != BLOCK_SIZE:
            raise ValueError("block must be 16 bytes")

        x = _bytes_to_u32_list(block)
        for i in range(32):
            tmp = x[1] ^ x[2] ^ x[3] ^ self.rk[31 - i]
            t = _tau(tmp)
            t = _l_transform(t)
            new = (x[0] ^ t) & 0xFFFFFFFF
            x = [x[1], x[2], x[3], new]
        out = list(reversed(x))
        return _u32_list_to_bytes(out)

    def encrypt_ecb(self, data: bytes) -> bytes:
        """
        Encrypt data in ECB mode with PKCS#7 padding.

        :param data: plaintext bytes
        :return: ciphertext bytes (multiple of 16)
        """
        padded = pkcs7_pad(data, BLOCK_SIZE)
        out_parts: list[bytes] = []
        for i in range(0, len(padded), BLOCK_SIZE):
            out_parts.append(self.encrypt_block(padded[i : i + BLOCK_SIZE]))
        return b"".join(out_parts)

    def decrypt_ecb(self, data: bytes) -> bytes:
        """
        Decrypt data in ECB mode and remove PKCS#7 padding.

        :param data: ciphertext bytes (multiple of 16)
        :return: plaintext bytes
        :raises ValueError: if ciphertext length not multiple of block size
        """
        if len(data) % BLOCK_SIZE != 0:
            raise ValueError("ciphertext length must be multiple of block size")
        out_parts: list[bytes] = []
        for i in range(0, len(data), BLOCK_SIZE):
            out_parts.append(self.decrypt_block(data[i : i + BLOCK_SIZE]))
        return pkcs7_unpad(b"".join(out_parts), BLOCK_SIZE)


def pkcs7_pad(data: bytes, block_size: int) -> bytes:
    """
    Apply PKCS#7 padding to data for a given block_size.

    :param data: bytes to pad
    :param block_size: block size (1..255)
    """
    if block_size <= 0 or block_size > 255:
        raise ValueError("block_size must be between 1 and 255")
    pad_len = block_size - (len(data) % block_size)
    if pad_len == 0:
        pad_len = block_size
    return data + bytes([pad_len]) * pad_len


def pkcs7_unpad(data: bytes, block_size: int) -> bytes:
    """
    Remove PKCS#7 padding and validate.

    :param data: padded bytes
    :param block_size: block size used for padding
    :raises ValueError: on invalid padding
    """
    if not data or len(data) % block_size != 0:
        raise ValueError("invalid padded data length")
    pad_len = data[-1]
    if pad_len <= 0 or pad_len > block_size:
        raise ValueError("invalid padding length")
    if data[-pad_len:] != bytes([pad_len]) * pad_len:
        raise ValueError("invalid PKCS#7 padding bytes")
    return data[:-pad_len]


if __name__ == "__main__":
    "an example of sm4 encrypt and decrypt:"
    key = bytes.fromhex("0123456789abcdeffedcba9876543210")
    sm4 = SM4(key)

    pt = b"0123456789abcdeF"
    ct = sm4.encrypt_block(pt)
    dec = sm4.decrypt_block(ct)
    assert dec == pt, "Block encrypt/decrypt failed"

    print(f"Block test passed: {ct.hex()}")
    msg = b"The quick fox jumps over the lazy dog"
    enc = sm4.encrypt_ecb(msg)
    dec = sm4.decrypt_ecb(enc)
    assert dec == msg, "ECB roundtrip failed"
