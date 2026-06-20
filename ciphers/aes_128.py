"""
Advanced Encryption Standard (AES) - 128 bit

AES is a symmetric block cipher chosen by the U.S. government to
protect classified information. AES is implemented in software
and hardware throughout the world to encrypt sensitive data.
This implementation provides the core AES-128 block encryption
algorithm (operating on 16-byte blocks).

Reference: https://en.wikipedia.org/wiki/Advanced_Encryption_Standard
"""

# Precomputed S-Box for byte substitution
S_BOX = (
    0x63,
    0x7C,
    0x77,
    0x7B,
    0xF2,
    0x6B,
    0x6F,
    0xC5,
    0x30,
    0x01,
    0x67,
    0x2B,
    0xFE,
    0xD7,
    0xAB,
    0x76,
    0xCA,
    0x82,
    0xC9,
    0x7D,
    0xFA,
    0x59,
    0x47,
    0xF0,
    0xAD,
    0xD4,
    0xA2,
    0xAF,
    0x9C,
    0xA4,
    0x72,
    0xC0,
    0xB7,
    0xFD,
    0x93,
    0x26,
    0x36,
    0x3F,
    0xF7,
    0xCC,
    0x34,
    0xA5,
    0xE5,
    0xF1,
    0x71,
    0xD8,
    0x31,
    0x15,
    0x04,
    0xC7,
    0x23,
    0xC3,
    0x18,
    0x96,
    0x05,
    0x9A,
    0x07,
    0x12,
    0x80,
    0xE2,
    0xEB,
    0x27,
    0xB2,
    0x75,
    0x09,
    0x83,
    0x2C,
    0x1A,
    0x1B,
    0x6E,
    0x5A,
    0xA0,
    0x52,
    0x3B,
    0xD6,
    0xB3,
    0x29,
    0xE3,
    0x2F,
    0x84,
    0x53,
    0xD1,
    0x00,
    0xED,
    0x20,
    0xFC,
    0xB1,
    0x5B,
    0x6A,
    0xCB,
    0xBE,
    0x39,
    0x4A,
    0x4C,
    0x58,
    0xCF,
    0xD0,
    0xEF,
    0xAA,
    0xFB,
    0x43,
    0x4D,
    0x33,
    0x85,
    0x45,
    0xF9,
    0x02,
    0x7F,
    0x50,
    0x3C,
    0x9F,
    0xA8,
    0x51,
    0xA3,
    0x40,
    0x8F,
    0x92,
    0x9D,
    0x38,
    0xF5,
    0xBC,
    0xB6,
    0xDA,
    0x21,
    0x10,
    0xFF,
    0xF3,
    0xD2,
    0xCD,
    0x0C,
    0x13,
    0xEC,
    0x5F,
    0x97,
    0x44,
    0x17,
    0xC4,
    0xA7,
    0x7E,
    0x3D,
    0x64,
    0x5D,
    0x19,
    0x73,
    0x60,
    0x81,
    0x4F,
    0xDC,
    0x22,
    0x2A,
    0x90,
    0x88,
    0x46,
    0xEE,
    0xB8,
    0x14,
    0xDE,
    0x5E,
    0x0B,
    0xDB,
    0xE0,
    0x32,
    0x3A,
    0x0A,
    0x49,
    0x06,
    0x24,
    0x5C,
    0xC2,
    0xD3,
    0xAC,
    0x62,
    0x91,
    0x95,
    0xE4,
    0x79,
    0xE7,
    0xC8,
    0x37,
    0x6D,
    0x8D,
    0xD5,
    0x4E,
    0xA9,
    0x6C,
    0x56,
    0xF4,
    0xEA,
    0x65,
    0x7A,
    0xAE,
    0x08,
    0xBA,
    0x78,
    0x25,
    0x2E,
    0x1C,
    0xA6,
    0xB4,
    0xC6,
    0xE8,
    0xDD,
    0x74,
    0x1F,
    0x4B,
    0xBD,
    0x8B,
    0x8A,
    0x70,
    0x3E,
    0xB5,
    0x66,
    0x48,
    0x03,
    0xF6,
    0x0E,
    0x61,
    0x35,
    0x57,
    0xB9,
    0x86,
    0xC1,
    0x1D,
    0x9E,
    0xE1,
    0xF8,
    0x98,
    0x11,
    0x69,
    0xD9,
    0x8E,
    0x94,
    0x9B,
    0x1E,
    0x87,
    0xE9,
    0xCE,
    0x55,
    0x28,
    0xDF,
    0x8C,
    0xA1,
    0x89,
    0x0D,
    0xBF,
    0xE6,
    0x42,
    0x68,
    0x41,
    0x99,
    0x2D,
    0x0F,
    0xB0,
    0x54,
    0xBB,
    0x16,
)

# Round constants used for key expansion
RCON = (0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36)


def sub_bytes(state: list[int]) -> None:
    """
    Applies the AES S-Box substitution to each byte in the state.

    Args:
        state: A list of 16 integers representing the state matrix.

    Examples:
        >>> state = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        >>> sub_bytes(state)
        >>> state[:4]
        [99, 124, 119, 123]
    """

    for i in range(16):
        state[i] = S_BOX[state[i]]


def shift_rows(state: list[int]) -> None:
    """
    Shifts the rows of the 4x4 state matrix.

    Args:
        state: A list of 16 integers representing the state matrix.

    Examples:
        >>> state = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        >>> shift_rows(state)
        >>> state
        [0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12, 1, 6, 11]
    """
    # Row 0: unchanged
    # Row 1: shifted left by 1
    state[1], state[5], state[9], state[13] = state[5], state[9], state[13], state[1]
    # Row 2: shifted left by 2
    state[2], state[6], state[10], state[14] = state[10], state[14], state[2], state[6]
    # Row 3: shifted left by 3
    state[3], state[7], state[11], state[15] = state[15], state[3], state[7], state[11]


def galois_multiply(multiplicand: int, multiplier: int) -> int:
    """
    Multiplies two numbers in the GF(2^8) Galois field.

    Args:
        multiplicand: The first integer to multiply.
        multiplier: The second integer to multiply.

    Returns:
        The product of the two numbers in the Galois field.

    Examples:
        >>> galois_multiply(2, 3)
        6
        >>> galois_multiply(87, 19)
        254
    """
    p = 0
    for _ in range(8):
        if multiplier & 1:
            p ^= multiplicand
        hi_bit_set = multiplicand & 0x80
        multiplicand <<= 1
        if hi_bit_set:
            multiplicand ^= 0x11B  # x^8 + x^4 + x^3 + x + 1
        multiplier >>= 1
    return p % 256


def mix_columns(state: list[int]) -> None:
    """
    Mixes the columns of the state matrix to provide diffusion.

    Args:
        state: A list of 16 integers representing the state matrix.

    Examples:
        >>> state = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        >>> mix_columns(state)
        >>> state
        [2, 1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    """
    for i in range(4):
        col = state[i * 4 : (i + 1) * 4]
        state[i * 4] = (
            galois_multiply(col[0], 2) ^ galois_multiply(col[1], 3) ^ col[2] ^ col[3]
        )
        state[i * 4 + 1] = (
            col[0] ^ galois_multiply(col[1], 2) ^ galois_multiply(col[2], 3) ^ col[3]
        )
        state[i * 4 + 2] = (
            col[0] ^ col[1] ^ galois_multiply(col[2], 2) ^ galois_multiply(col[3], 3)
        )
        state[i * 4 + 3] = (
            galois_multiply(col[0], 3) ^ col[1] ^ col[2] ^ galois_multiply(col[3], 2)
        )


def add_round_key(state: list[int], round_key: list[int]) -> None:
    """
    XORs the state matrix with the current round key.

    Args:
        state: A list of 16 integers representing the state matrix.
        round_key: A list of 16 integers representing the round key.

    Examples:
        >>> state = [0] * 16
        >>> round_key = [1] * 16
        >>> add_round_key(state, round_key)
        >>> state
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    """
    for i in range(16):
        state[i] ^= round_key[i]


def key_expansion(key: bytes) -> list[int]:
    """
    Expands a 16-byte key into 11 round keys (176 bytes total).

    Args:
        key: Exactly 16 bytes of encryption key.

    Returns:
        A list of 176 integers representing the expanded key schedule.

    Examples:
        >>> key = bytes([0] * 16)
        >>> len(key_expansion(key))
        176
    """
    key_schedule = list(key)
    for i in range(4, 44):
        word = key_schedule[(i - 1) * 4 : i * 4]
        if i % 4 == 0:
            # Shift row
            word = word[1:] + word[:1]
            # Sub bytes
            word = [S_BOX[b] for b in word]
            # XOR RCON
            word[0] ^= RCON[i // 4]

        for j in range(4):
            key_schedule.append(key_schedule[(i - 4) * 4 + j] ^ word[j])

    return key_schedule


def aes_128_encrypt_block(plaintext: bytes, key: bytes) -> bytes:
    """
    Encrypts a single 16-byte block of plaintext using AES-128.

    Args:
        plaintext: Exactly 16 bytes of data.
        key: Exactly 16 bytes of encryption key.

    Returns:
        16 bytes of encrypted ciphertext.

    Raises:
        ValueError: If plaintext or key are not exactly 16 bytes.

    Examples:

        >>> key = bytes.fromhex('2b7e151628aed2a6abf7158809cf4f3c')
        >>> plaintext = bytes.fromhex('3243f6a8885a308d313198a2e0370734')
        >>> ciphertext = aes_128_encrypt_block(plaintext, key)
        >>> ciphertext.hex()
        '3925841d02dc09fbdc118597196a0b32'
    """
    if len(plaintext) != 16 or len(key) != 16:
        raise ValueError("Plaintext and Key must be exactly 16 bytes long.")

    state = list(plaintext)
    expanded_key = key_expansion(key)

    # Initial Round
    add_round_key(state, expanded_key[0:16])

    # 9 Main Rounds
    for round_num in range(1, 10):
        sub_bytes(state)
        shift_rows(state)
        mix_columns(state)
        add_round_key(state, expanded_key[round_num * 16 : (round_num + 1) * 16])

    # Final Round (No MixColumns)
    sub_bytes(state)
    shift_rows(state)
    add_round_key(state, expanded_key[160:176])

    return bytes(state)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
