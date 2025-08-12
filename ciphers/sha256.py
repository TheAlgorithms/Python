"""
Educational Implementation of the SHA-256 Hash Function
-------------------------------------------------------

This module implements the SHA-256 cryptographic hash function in accordance
with the specification defined in *FIPS PUB 180-4: Secure Hash Standard (SSH)*,
available at:
https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf

⚠ DISCLAIMER:
This implementation is intended **solely for educational and instructional purposes**.
It is not optimized for performance, security hardening, or production deployment.
Real-world applications must use well-reviewed, vetted cryptographic libraries
such as those provided by OpenSSL, libsodium, or Python's `hashlib`.

The purpose of this code is to provide a transparent, step-by-step reference
for understanding the internal mechanics of the SHA-256 algorithm as described
in the NIST standard.
"""

import math
from collections.abc import Iterator
from itertools import count, islice

# =============================================================================
# SHA-256 Core Functions
# As defined in: NIST FIPS PUB 180-4 (Secure Hash Standard)
# -----------------------------------------------------------------------------
# Section 4 of the specification defines the logical functions used throughout
# the SHA-256 compression process. All bitwise operations here assume 32-bit
# unsigned integer arithmetic.
# =============================================================================
MASK32 = 0xFFFFFFFF


def rotr(value: int, shift: int, bit_width: int = 32) -> int:
    """
    Circular right rotation (ROTR) of a `size`-bit word.
    Equivalent to shifting bits right by n positions and wrapping the overflow.

    Examples:
    >>> rotr(0b1001, 1)
    2147483652
    >>> bin(rotr(0b1001, 1))
    '0b10000000000000000000000000000100'
    >>> rotr(0b1001, 0)
    9
    >>> rotr(0b1001, 32)
    9
    >>> hex(rotr(0xF0F0F0F0, 3))
    '0x1e1e1e1e'
    """

    bit_width = int(bit_width)
    mask = (1 << bit_width) - 1
    value &= mask
    shift %= bit_width
    return ((value >> shift) | ((value << (bit_width - shift)) & mask)) & mask


def shr(value: int, shift: int) -> int:
    """
    Logical right shift (SHR).
    Bits shifted in from the left are zero-filled.

    Examples:
    >>> shr(0b1000, 1)
    4
    >>> bin(shr(0b1000, 1))
    '0b100'
    >>> shr(0b1000, 3)
    1
    >>> shr(0b1000, 4)
    0
    >>> shr(15, 0)
    15
    """
    if shift == 0:
        return value & MASK32
    return (value & MASK32) >> shift


def sig0(value: int) -> int:
    """
    σ₀ (lowercase sigma 0) function:
    σ₀(x) = ROTR⁷(x) ⊕ ROTR¹⁸(x) ⊕ SHR³(x)

    Examples:
    >>> hex(sig0(0x12345678))
    '0xe7fce6ee'
    >>> hex(sig0(0))
    '0x0'
    """
    return (rotr(value, 7) ^ rotr(value, 18) ^ shr(value, 3)) & MASK32


def sig1(value: int) -> int:
    """
    σ₁ (lowercase sigma 1) function:
    σ₁(x) = ROTR¹⁷(x) ⊕ ROTR¹⁹(x) ⊕ SHR¹⁰(x)

    Examples:
    >>> hex(sig1(0x12345678))
    '0xa1f78649'
    >>> hex(sig1(0))
    '0x0'
    """
    return (rotr(value, 17) ^ rotr(value, 19) ^ shr(value, 10)) & MASK32


def capsig0(value: int) -> int:
    """
    Σ₀ (uppercase sigma 0) function:
    Σ₀(x) = ROTR²(x) ⊕ ROTR¹³(x) ⊕ ROTR²²(x)

    Examples:
    >>> hex(capsig0(0x12345678))
    '0x66146474'
    >>> hex(capsig0(0))
    '0x0'
    """
    return (rotr(value, 2) ^ rotr(value, 13) ^ rotr(value, 22)) & MASK32


def capsig1(value: int) -> int:
    """
    Σ₁ (uppercase sigma 1) function:
    Σ₁(x) = ROTR⁶(x) ⊕ ROTR¹¹(x) ⊕ ROTR²⁵(x)

    Examples:
    >>> hex(capsig1(0x12345678))
    '0x3561abda'
    >>> hex(capsig1(0))
    '0x0'
    """
    return (rotr(value, 6) ^ rotr(value, 11) ^ rotr(value, 25)) & MASK32


def ch(choice_mask: int, true_value: int, false_value: int) -> int:
    """
    Choice function:
    Ch(x, y, z) = (x ∧ y) ⊕ (¬x ∧ z)

    Examples:
    >>> ch(0b0, 0b1010, 0b1111)
    15
    >>> ch(0b1, 0b1010, 0b1111)
    14
    >>> bin(ch(0b1, 0b1010, 0b1111))
    '0b1110'
    """
    return (
        (choice_mask & true_value) ^ ((~choice_mask & MASK32) & false_value)
    ) & MASK32


def maj(bit_a: int, bit_b: int, bit_c: int) -> int:
    """
    Majority function:
    Maj(x, y, z) = (x ∧ y) ⊕ (x ∧ z) ⊕ (y ∧ z)

    Examples:
    >>> maj(0b0, 0b1010, 0b1111)
    10
    >>> maj(0b1, 0b1010, 0b1111)
    11
    >>> bin(maj(0b1, 0b1010, 0b1111))
    '0b1011'
    """
    return ((bit_a & bit_b) ^ (bit_a & bit_c) ^ (bit_b & bit_c)) & MASK32


def b2i(bigi: bytes) -> int:
    """
    Converts a big-endian byte sequence to an integer.

    Examples:
    >>> b2i(b'\\x00\\x00\\x00\\x01')
    1
    >>> b2i(b'\\x12\\x34\\x56\\x78')
    305419896
    >>> b2i(b'')
    0
    """
    return int.from_bytes(bigi, byteorder="big")


def int_to_big_endian_bytes(value: int) -> bytes:
    """
    Converts a 32-bit integer to a 4-byte big-endian representation.

    Examples:
    >>> int_to_big_endian_bytes(1)
    b'\\x00\\x00\\x00\\x01'
    >>> int_to_big_endian_bytes(305419896)
    b'\\x124Vx'
    >>> int_to_big_endian_bytes(0)
    b'\\x00\\x00\\x00\\x00'
    """
    return value.to_bytes(4, byteorder="big")


# =============================================================================
# SHA-256 Constants
# -----------------------------------------------------------------------------
# Section 4.2 of NIST FIPS PUB 180-4 specifies:
#   - The initial hash values H[0..7] are the first 32 bits of the fractional
#     parts of the square roots of the first 8 prime numbers.
#   - The round constants K[0..63] are the first 32 bits of the fractional parts
#     of the cube roots of the first 64 prime numbers.
# =============================================================================


def is_prime(num_to_test: int) -> bool:
    """
    Returns True if n is a prime number.
    Uses trial division up to floor(sqrt(n)).

    Examples:
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    >>> is_prime(0)
    False
    """
    if num_to_test < 2:
        return False
    return all(num_to_test % f != 0 for f in range(2, math.isqrt(num_to_test) + 1))


def first_n_primes(count_primes: int) -> Iterator[int]:
    """
    Generates the first n prime numbers using itertools.count and a primality test.
        Examples:
    >>> list(first_n_primes(0))
    []
    >>> list(first_n_primes(1))
    [2]
    >>> list(first_n_primes(5))
    [2, 3, 5, 7, 11]
    >>> list(first_n_primes(3))
    [2, 3, 5]
    """
    return islice(filter(is_prime, count(start=2)), count_primes)


def frac_bin(fraction_value: float, bit_count: int = 32) -> int:
    """
    Returns the first n bits of the fractional part of a floating-point number.

    For example:
        frac_bin(math.sqrt(2) % 1, 32) → 0x6A09E667 (first 32 bits of √2's
        fractional part)

    This is used to derive SHA-256 constants from fractional parts of roots.
     Examples:
    >>> frac_bin(math.sqrt(2) - 1, 32)
    1779033703
    >>> frac_bin(0.5, 32)
    2147483648
    >>> frac_bin(0.0, 32)
    0
    >>> frac_bin(math.sqrt(3) - 1, 8)
    187
    """
    frac_part = fraction_value - math.floor(fraction_value)  # Keep only fractional part
    shifted = frac_part * (1 << bit_count)  # Shift left to extract bits
    return int(shifted)  # Truncate to integer (n-bit precision)


def gen_k() -> list[int]:
    """
    Generates the 64 SHA-256 round constants (K[0..63]) as per FIPS PUB 180-4, §4.2.2.

    Definition:
        K[t] = first 32 bits of the fractional part of the cube root of the
        t-th prime number, for t = 1 to 64.

    Formula:
        K[t] = floor( ( { p_t^(1/3) } ) x 2^32 )

    Returns:
        List of 64 unsigned 32-bit integers representing the K constants.

    Expected Values (hexadecimal):
        428a2f98 71374491 b5c0fbcf e9b5dba5 3956c25b 59f111f1 923f82a4 ab1c5ed5
        d807aa98 12835b01 243185be 550c7dc3 72be5d74 80deb1fe 9bdc06a7 c19bf174
        e49b69c1 efbe4786 0fc19dc6 240ca1cc 2de92c6f 4a7484aa 5cb0a9dc 76f988da
        983e5152 a831c66d b00327c8 bf597fc7 c6e00bf3 d5a79147 06ca6351 14292967
        27b70a85 2e1b2138 4d2c6dfc 53380d13 650a7354 766a0abb 81c2c92e 92722c85
        a2bfe8a1 a81a664b c24b8b70 c76c51a3 d192e819 d6990624 f40e3585 106aa070
        19a4c116 1e376c08 2748774c 34b0bcb5 391c0cb3 4ed8aa4a 5b9cca4f 682e6ff3
        748f82ee 78a5636f 84c87814 8cc70208 90befffa a4506ceb bef9a3f7 c67178f2

    Examples:
    >>> gen_k()[0]  # K[0] = first 32 bits of fractional part of cube root of 2
    1116352408
    >>> gen_k()[1]  # K[1] = first 32 bits of fractional part of cube root of 3
    1899447441
    >>> gen_k()[2]  # K[2] = first 32 bits of fractional part of cube root of 5
    3049323471
    >>> len(gen_k())
    64
    >>> gen_k()[63]  # K[63] = first 32 bits of fractional part of cube root of 311
    3329325298
    """
    return [frac_bin(p ** (1 / 3.0)) & 0xFFFFFFFF for p in first_n_primes(64)]


def gen_h() -> list[int]:
    """
    Generates the initial hash value H⁽⁰⁾[0..7] for SHA-256 as defined in
    FIPS PUB 180-4, §5.3.3.

    Definition:
        H⁽⁰⁾[i] = first 32 bits of the fractional part of the square root
                  of the (i+1)-th prime number, for i = 0..7.

    Formula:
        H⁽⁰⁾[i] = floor( ( { sqrt(p_{i+1}) } ) x 2^32 )

    Returns:
        List of 8 unsigned 32-bit integers representing the initial hash values.

    Expected Values (hexadecimal):
        6a09e667 bb67ae85 3c6ef372 a54ff53a
        9b05688c 510e527f 1f83d9ab 5be0cd19
    Examples:
    >>> gen_h()[0]  # H⁽⁰⁾[0] = first 32 bits of fractional part of sqrt(2)
    1779033703
    >>> gen_h()[1]  # H⁽⁰⁾[1] = first 32 bits of fractional part of sqrt(3)
    3144134277
    >>> gen_h()[2]  # H⁽⁰⁾[2] = first 32 bits of fractional part of sqrt(5)
    1013904242
    >>> len(gen_h())
    8
    >>> gen_h()[7]  # H⁽⁰⁾[7] = first 32 bits of fractional part of sqrt(17)
    1541459225
    """
    return [frac_bin(p**0.5) & 0xFFFFFFFF for p in first_n_primes(8)]


def pad(message: bytes) -> bytearray:
    """
    Pads the input message according to SHA-256 specification (FIPS PUB 180-4 §5.1.1).

    Padding Steps:
        1. Append a single '1' bit to the message (represented here as 0x80).
        2. Append 'k' zero bits, where k is the smallest non-negative integer
           such that the total message length (in bits) is congruent to 448
           modulo 512.
        3. Append the original message length (before padding) as a 64-bit
           big-endian integer.

    Parameters:
        message (bytes): The original message byte sequence.

    Returns:
        bytearray: The padded message, length a multiple of 512 bits (64 bytes).

    Examples:
    >>> pad(b"")
    bytearray(b'\\x80\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00')
    >>> pad(b"abc")
    bytearray(b'abc\\x80\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x18')
    >>> len(pad(b"A" * 55)) % 64
    0
    >>> pad(b"A" * 55)[-8:]  # Last 8 bytes encode original bit length (55 * 8 = 440)
    bytearray(b'\\x00\\x00\\x00\\x00\\x00\\x00\\x01\\xb8')
    """
    b = bytearray(message)  # Convert to mutable type
    original_bit_len = len(b) * 8  # Message length in bits

    # Step 1: Append the bit '1' followed by seven '0' bits to complete the byte
    b.append(0x80)  # 0b10000000

    # Step 2: Append zero bytes until message length (in bits) ≡ 448 mod 512
    while (len(b) * 8) % 512 != 448:
        b.append(0x00)

    # Step 3: Append 64-bit big-endian integer of original bit length
    b.extend(original_bit_len.to_bytes(8, byteorder="big"))

    return b


def sha256(message: bytes) -> bytes:
    """
    Computes the SHA-256 hash of the input message as specified in
    FIPS PUB 180-4 (Secure Hash Standard).

    Parameters:
        message (bytes): Input message of arbitrary length.

    Returns:
        bytes: The 32-byte (256-bit) SHA-256 digest.

    Examples:
    >>> sha256(b"")
    b"\\xe3\\xb0\\xc4B\\x98\\xfc\\x1c\\x14\\x9a\\xfb\\xf4\\xc8\\x99o\\xb9$'\\xaeA\\xe4d\\x9b\\x93L\\xa4\\x95\\x99\\x1bxR\\xb8U"

    >>> sha256(b"abc")
    b'\\xbax\\x16\\xbf\\x8f\\x01\\xcf\\xeaAA@\\xde]\\xae"#\\xb0\\x03a\\xa3\\x96\\x17z\\x9c\\xb4\\x10\\xffa\\xf2\\x00\\x15\\xad'

    >>> sha256(b"abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq")
    b'$\\x8dja\\xd2\\x068\\xb8\\xe5\\xc0&\\x93\\x0c>`9\\xa3<\\xe4Yd\\xff!g\\xf6\\xec\\xed\\xd4\\x19\\xdb\\x06\\xc1'

    >>> sha256(b"A" * 1000)[:8]  # Partial check for large input
    b'\\xc2\\xe6\\x86\\x824\\x89\\xce\\xd2'
    """

    # Section 4.2: SHA-256 Constants (K)
    k: list[int] = gen_k()

    # Section 5.1: Preprocessing (Padding the message)
    padded_message: bytearray = pad(message)

    # Section 5.2: Parse padded message into 512-bit (64-byte) blocks
    blocks: list[bytes] = [
        padded_message[i : i + 64] for i in range(0, len(padded_message), 64)
    ]

    # Section 5.3: Initialize hash values (H⁽⁰⁾)
    h: list[int] = gen_h()

    # Section 6: Hash computation
    for block in blocks:
        # 1. Prepare the message schedule W (64 words)
        w: list[int] = [0] * 64

        # The first 16 words are directly extracted from the block
        for t in range(16):
            w[t] = b2i(block[t * 4 : t * 4 + 4])

        # Extend the remaining words using σ₀ and σ₁ functions
        for t in range(16, 64):
            s0 = sig0(w[t - 15])
            s1 = sig1(w[t - 2])
            w[t] = (w[t - 16] + s0 + w[t - 7] + s1) & 0xFFFFFFFF

        # 2. Initialize working variables with previous hash value
        a, b_, c, d, e, f, g, h_temp = h  # Use b_ to avoid shadowing input bytes 'b'

        # 3. Main compression loop
        for t in range(64):
            t1 = (h_temp + capsig1(e) + ch(e, f, g) + k[t] + w[t]) & 0xFFFFFFFF
            t2 = (capsig0(a) + maj(a, b_, c)) & 0xFFFFFFFF

            h_temp = g
            g = f
            f = e
            e = (d + t1) & 0xFFFFFFFF
            d = c
            c = b_
            b_ = a
            a = (t1 + t2) & 0xFFFFFFFF

        # 4. Compute the intermediate hash value H⁽ⁱ⁾
        h = [(x + y) & 0xFFFFFFFF for x, y in zip(h, [a, b_, c, d, e, f, g, h_temp])]

    # Produce the final digest by concatenating H[0..7] in big-endian byte order
    return b"".join(int_to_big_endian_bytes(h_i) for h_i in h)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
