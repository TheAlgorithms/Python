"""
Pure Python implementation of the RIPEMD-160 algorithm.
DISCLAIMER:
This implementation is intended **solely for educational and instructional purposes**.
Reference:
/*
 * Preneel, Bosselaers, Dobbertin, "The Cryptographic Hash Function RIPEMD-160",
 * RSA Laboratories, CryptoBytes, Volume 3, Number 2, Autumn 1997,
 * ftp://ftp.rsasecurity.com/pub/cryptobytes/crypto3n2.pdf
 */
"""

import struct
import sys


def ripemd160(b: bytes) -> bytes:
    """
    Compute the RIPEMD-160 hash of the input byte sequence.

    Parameters
    ----------
    message : bytes
        Input data to be hashed.

    Returns
    -------
    bytes
        The 20-byte RIPEMD-160 hash digest.

    Examples
    --------
    >>> ripemd160(b'')
    b'\\x9c\\x11\\x85\\xa5\\xc5\\xe9\\xfcTa(\\x08\\x97~\\xe8\\xf5H\\xb2%\\x8d1'
    >>> ripemd160(b'The quick brown fox jumps over the lazy cog')
    b'\\x13 r\\xdfi\\t3\\x83^\\xb8\\xb6\\xad\\x0bw\\xe7\\xb6\\xf1J\\xca\\xd7'
    """
    ctx = Context()
    update(ctx, b, len(b))
    digest = final(ctx)
    return digest


class Context:
    """
    Context for RIPEMD-160 computation maintaining state and buffer.

    Attributes
    ----------
    state : list[int]
        The current state of the hash (5 32-bit unsigned integers).
    count : int
        Number of bits processed so far.
    buffer : list[int]
        Input buffer for message blocks (64 bytes).

    Examples
    --------
    >>> ctx = Context()
    >>> ctx.state == [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]
    True
    """

    def __init__(self) -> None:
        """
            Examples
        --------
        >>> ctx = Context()
        >>> ctx.state == [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]
        True
        >>> ctx.count
        0
        >>> len(ctx.buffer)
        64
        >>> all(b == 0 for b in ctx.buffer)
        True
        """
        self.state: list[int] = [
            0x67452301,
            0xEFCDAB89,
            0x98BADCFE,
            0x10325476,
            0xC3D2E1F0,
        ]
        self.count: int = 0
        self.buffer: list[int] = [0] * 64


def update(ctx, inp, inplen):
    """
    Update the RIPEMD-160 context with new data.

    Parameters
    ----------
    ctx : RMDContext
        The hash context to update.
    inp : bytes
        Input bytes to process.
    inplen : int
        Length of input in bytes.

    Examples
    --------
    >>> ctx = Context()
    >>> update(ctx, b'abc', 3)
    >>> ctx.count
    24
    >>> all(isinstance(b, int) for b in ctx.buffer)
    True
    """
    have = int((ctx.count // 8) % 64)
    inplen = int(inplen)
    ctx.count += 8 * inplen
    off = 0
    if inplen >= (need := 64 - have):
        if have:
            for i in range(need):
                ctx.buffer[have + i] = inp[i]
            transform(ctx.state, ctx.buffer)
            off = need
            have = 0
        while off + 64 <= inplen:
            transform(ctx.state, inp[off:])  # <---
            off += 64
    if off < inplen:
        for i in range(inplen - off):
            ctx.buffer[have + i] = inp[off + i]


def final(ctx):
    """
    Finalize the RIPEMD-160 hash and return the digest.

    Parameters
    ----------
    ctx : RMDContext
        The hash context to finalize.

    Returns
    -------
    bytes
        The final 20-byte hash digest.

    Examples
    --------
    >>> ctx = Context()
    >>> final(ctx)  # hashing empty input (no update)
    b'\\x9c\\x11\\x85\\xa5\\xc5\\xe9\\xfcTa(\\x08\\x97~\\xe8\\xf5H\\xb2%\\x8d1'
    >>> ctx = Context()
    >>> update(ctx, b'abc', 3)
    >>> final(ctx)
    b'\\x8e\\xb2\\x08\\xf7\\xe0]\\x98z\\x9b\\x04J\\x8e\\x98\\xc6\\xb0\\x87\\xf1Z\\x0b\\xfc'
    """
    size = struct.pack("<Q", ctx.count)
    padlen = 64 - ((ctx.count // 8) % 64)
    if padlen < 1 + 8:
        padlen += 64
    update(ctx, PADDING, padlen - 8)
    update(ctx, size, 8)
    return struct.pack("<5L", *ctx.state)


# Round constants for RIPEMD-160 left line
K0 = 0x00000000  # Round 1 constant
K1 = 0x5A827999  # Round 2 constant
K2 = 0x6ED9EBA1  # Round 3 constant
K3 = 0x8F1BBCDC  # Round 4 constant
K4 = 0xA953FD4E  # Round 5 constant

# Round constants for RIPEMD-160 right line (parallel)
KK0 = 0x50A28BE6  # Parallel Round 1 constant
KK1 = 0x5C4DD124  # Parallel Round 2 constant
KK2 = 0x6D703EF3  # Parallel Round 3 constant
KK3 = 0x7A6D76E9  # Parallel Round 4 constant
KK4 = 0x00000000  # Parallel Round 5 constant

PADDING = [0x80] + [0] * 63


def rol(n, x):
    """
    Rotate left operation on a 32-bit integer.

    Args:
        n (int): Number of bits to rotate left.
        x (int): 32-bit unsigned integer.

    Returns:
        int: Result of rotating x left by n bits, masked to 32 bits.

    >>> rol(1, 0x80000000)
    1
    >>> rol(4, 0x12345678)
    591751041
    """
    return ((x << n) & 0xFFFFFFFF) | (x >> (32 - n))


def f0(x, y, z):
    """
    Boolean function f0 used in RIPEMD160.

    Returns bitwise XOR of three inputs.

    >>> f0(0b1010, 0b1100, 0b0110)
    0
    """
    return x ^ y ^ z


def f1(x, y, z):
    """
    Boolean function f1 used in RIPEMD160.

    Returns (x AND y) OR (NOT x AND z).

    >>> f1(0b1010, 0b1100, 0b0110)
    12
    """
    return (x & y) | (((~x) % 0x100000000) & z)


def f2(x, y, z):
    """
    Boolean function f2 used in RIPEMD160.

    Returns (x OR NOT y) XOR z.

    >>> f2(0b1010, 0b1100, 0b0110)
    4294967293
    """
    return (x | ((~y) % 0x100000000)) ^ z


def f3(x, y, z):
    """
    Boolean function f3 used in RIPEMD160.

    Returns (x AND z) OR (NOT z AND y).

    >>> f3(0b1010, 0b1100, 0b0110)
    10
    """
    return (x & z) | (((~z) % 0x100000000) & y)


def f4(x, y, z):
    """
    Boolean function f4 used in RIPEMD160.

    Returns x XOR (y OR NOT z).

    >>> f4(0b1010, 0b1100, 0b0110)
    4294967287
    """
    return x ^ (y | ((~z) % 0x100000000))


def one(a, b, c, d, e, fj, kj, sj, rj, x):
    """
    Perform one round step in RIPEMD160 compression function.

    Args:
        a, b, c, d, e (int): 32-bit words representing the current state.
        fj (function): One of the boolean functions f0..f4.
        kj (int): Round constant.
        sj (int): Number of bits to rotate left.
        rj (int): Index into the message block.
        x (list[int]): List of 16 32-bit words from the message block.

    Returns:
        tuple: Updated values (a, c) after the round.

    >>> x = [i for i in range(16)]
    >>> a, c = one(
    ...     0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476,
    ...     0xc3d2e1f0, f0, 0x00000000, 5, 0, x
    ... )
    >>> hex(a), hex(c)
    ('0x951ba249', '0xeb73fa62')
    """
    a = rol(sj, (a + fj(b, c, d) + x[rj] + kj) % 0x100000000) + e
    c = rol(10, c)
    return a % 0x100000000, c


def _process_round_1(a, b, c, d, e, x):
    """
    Process Round 1 of RIPEMD-160 compression function (steps 0-15).

    Round 1 characteristics:
    - Uses boolean function f0 (x ⊕ y ⊕ z)
    - Round constant K0 = 0x00000000
    - Message selection order: 0, 1, 2, ..., 15 (sequential)
    - Rotation amounts: [11, 14, 15, 12, 5, 8, 7, 9, 11, 13, 14, 15, 6, 7, 9, 8]

    The round implements the basic XOR mixing function, providing initial
    diffusion of the input message block through all state variables.

    Args:
        a, b, c, d, e (int): Five 32-bit state variables
        x (list[int]): 16 32-bit message words

    Returns:
        tuple: Updated state variables (a, b, c, d, e)

    Example:
        >>> # Initialize with RIPEMD-160 initial values
        >>> a0 = 0x67452301
        >>> b0 = 0xefcdab89
        >>> c0 = 0x98badcfe
        >>> d0 = 0x10325476
        >>> e0 = 0xc3d2e1f0
        >>> # Test message block (16 words of zeros)
        >>> x = [0] * 16
        >>> a1, b1, c1, d1, e1 = _process_round_1(a0, b0, c0, d0, e0, x)
        >>> # Verify state has changed from initial values
        >>> (a1 != a0) and (b1 != b0) and (c1 != c0) and (d1 != d0) and (e1 != e0)
        True
        >>> # Check that outputs are valid 32-bit integers
        >>> all(0 <= val <= 0xffffffff for val in [a1, b1, c1, d1, e1])
        True
    """
    # Step 0: Process message word x[0] with rotation 11
    a, c = one(a, b, c, d, e, f0, K0, 11, 0, x)

    # Step 1: Process message word x[1] with rotation 14
    e, b = one(e, a, b, c, d, f0, K0, 14, 1, x)

    # Step 2: Process message word x[2] with rotation 15
    d, a = one(d, e, a, b, c, f0, K0, 15, 2, x)

    # Step 3: Process message word x[3] with rotation 12
    c, e = one(c, d, e, a, b, f0, K0, 12, 3, x)

    # Step 4: Process message word x[4] with rotation 5
    b, d = one(b, c, d, e, a, f0, K0, 5, 4, x)

    # Step 5: Process message word x[5] with rotation 8
    a, c = one(a, b, c, d, e, f0, K0, 8, 5, x)

    # Step 6: Process message word x[6] with rotation 7
    e, b = one(e, a, b, c, d, f0, K0, 7, 6, x)

    # Step 7: Process message word x[7] with rotation 9
    d, a = one(d, e, a, b, c, f0, K0, 9, 7, x)

    # Step 8: Process message word x[8] with rotation 11
    c, e = one(c, d, e, a, b, f0, K0, 11, 8, x)

    # Step 9: Process message word x[9] with rotation 13
    b, d = one(b, c, d, e, a, f0, K0, 13, 9, x)

    # Step 10: Process message word x[10] with rotation 14
    a, c = one(a, b, c, d, e, f0, K0, 14, 10, x)

    # Step 11: Process message word x[11] with rotation 15
    e, b = one(e, a, b, c, d, f0, K0, 15, 11, x)

    # Step 12: Process message word x[12] with rotation 6
    d, a = one(d, e, a, b, c, f0, K0, 6, 12, x)

    # Step 13: Process message word x[13] with rotation 7
    c, e = one(c, d, e, a, b, f0, K0, 7, 13, x)

    # Step 14: Process message word x[14] with rotation 9
    b, d = one(b, c, d, e, a, f0, K0, 9, 14, x)

    # Step 15: Process message word x[15] with rotation 8 (final step of round 1)
    a, c = one(a, b, c, d, e, f0, K0, 8, 15, x)

    return a, b, c, d, e


def _process_round_2(a, b, c, d, e, x):
    """
    Process Round 2 of RIPEMD-160 compression function (steps 16-31).

    Round 2 characteristics:
    - Uses boolean function f1 ((x AND y) OR (NOT x AND z)) - conditional selection
    - Round constant K1 = 0x5A827999 (adds non-linearity through constant)
    - Message selection order: [7, 4, 13, 1, 10, 6, 15, 3, 12, 0, 9, 5, 2, 14, 11, 8]
    - Rotation amounts: [7, 6, 8, 13, 11, 9, 7, 15, 7, 12, 15, 9, 11, 7, 13, 12]

    This round introduces significant non-linearity through the conditional
    function f1, which selects bits from y or z based on the value of x.
    The non-sequential message access pattern ensures that message words
    influence the hash in a complex, interdependent manner.

    Cryptographic Purpose:
    Function f1 creates conditional dependencies: when x[i]=1, output[i]=y[i];
    when x[i]=0, output[i]=z[i]. This creates avalanche effects where small
    input changes cause large output changes, crucial for hash security.

    Args:
        a, b, c, d, e (int): Five 32-bit state variables from Round 1
        x (list[int]): 16 32-bit message words from input block

    Returns:
        tuple: Updated state variables (a, b, c, d, e) after 16 operations

    Example:
        >>> # Continue from Round 1 results
        >>> a0 = 0x67452301
        >>> b0 = 0xefcdab89
        >>> c0 = 0x98badcfe
        >>> d0 = 0x10325476
        >>> e0 = 0xc3d2e1f0
        >>> x = [0] * 16
        >>> a1, b1, c1, d1, e1 = _process_round_1(a0, b0, c0, d0, e0, x)
        >>> a2, b2, c2, d2, e2 = _process_round_2(a1, b1, c1, d1, e1, x)
        >>> # Verify further evolution occurred
        >>> (a2 != a1) and (b2 != b1) and (c2 != c1) and (d2 != d1) and (e2 != e1)
        True
        >>> all(0 <= val <= 0xffffffff for val in [a2, b2, c2, d2, e2])
        True
        >>> # Test non-linear behavior with different inputs
        >>> x_alt = [1] * 16
        >>> a3, b3, c3, d3, e3 = _process_round_2(a1, b1, c1, d1, e1, x_alt)
        >>> # Results should significantly differ due to f1's conditional nature
        >>> (a3 != a2) or (b3 != b2) or (c3 != c2) or (d3 != d2) or (e3 != e2)
        True
    """
    e, b = one(e, a, b, c, d, f1, K1, 7, 7, x)
    d, a = one(d, e, a, b, c, f1, K1, 6, 4, x)
    c, e = one(c, d, e, a, b, f1, K1, 8, 13, x)
    b, d = one(b, c, d, e, a, f1, K1, 13, 1, x)
    a, c = one(a, b, c, d, e, f1, K1, 11, 10, x)
    e, b = one(e, a, b, c, d, f1, K1, 9, 6, x)
    d, a = one(d, e, a, b, c, f1, K1, 7, 15, x)
    c, e = one(c, d, e, a, b, f1, K1, 15, 3, x)
    b, d = one(b, c, d, e, a, f1, K1, 7, 12, x)
    a, c = one(a, b, c, d, e, f1, K1, 12, 0, x)
    e, b = one(e, a, b, c, d, f1, K1, 15, 9, x)
    d, a = one(d, e, a, b, c, f1, K1, 9, 5, x)
    c, e = one(c, d, e, a, b, f1, K1, 11, 2, x)
    b, d = one(b, c, d, e, a, f1, K1, 7, 14, x)
    a, c = one(a, b, c, d, e, f1, K1, 13, 11, x)
    e, b = one(e, a, b, c, d, f1, K1, 12, 8, x)  # #31
    return a, b, c, d, e


def _process_round_3(a, b, c, d, e, x):
    """Process Round 3 of RIPEMD-160.
    Example:
        >>> a0 = 0x67452301
        >>> b0 = 0xefcdab89
        >>> c0 = 0x98badcfe
        >>> d0 = 0x10325476
        >>> e0 = 0xc3d2e1f0
        >>> x = [0] * 16
        >>> a1, b1, c1, d1, e1 = _process_round_1(a0, b0, c0, d0, e0, x)
        >>> a2, b2, c2, d2, e2 = _process_round_2(a1, b1, c1, d1, e1, x)
        >>> a3, b3, c3, d3, e3 = _process_round_3(a2, b2, c2, d2, e2, x)
        >>> # Continued state evolution
        >>> (a3 != a2) and (b3 != b2) and (c3 != c2) and (d3 != d2) and (e3 != e2)
        True
        >>> all(0 <= val <= 0xffffffff for val in [a3, b3, c3, d3, e3])
        True
        >>> # Test f2's unique behavior
        >>> x_test = [0xffffffff] * 16  # All bits set
        >>> a4, b4, c4, d4, e4 = _process_round_3(a2, b2, c2, d2, e2, x_test)
        >>> # Should produce different results due to f2's OR/XOR nature
        >>> (a4 != a3) or (b4 != b3) or (c4 != c3) or (d4 != d3) or (e4 != e3)
        True
    """
    d, a = one(d, e, a, b, c, f2, K2, 11, 3, x)
    c, e = one(c, d, e, a, b, f2, K2, 13, 10, x)
    b, d = one(b, c, d, e, a, f2, K2, 6, 14, x)
    a, c = one(a, b, c, d, e, f2, K2, 7, 4, x)
    e, b = one(e, a, b, c, d, f2, K2, 14, 9, x)
    d, a = one(d, e, a, b, c, f2, K2, 9, 15, x)
    c, e = one(c, d, e, a, b, f2, K2, 13, 8, x)
    b, d = one(b, c, d, e, a, f2, K2, 15, 1, x)
    a, c = one(a, b, c, d, e, f2, K2, 14, 2, x)
    e, b = one(e, a, b, c, d, f2, K2, 8, 7, x)
    d, a = one(d, e, a, b, c, f2, K2, 13, 0, x)
    c, e = one(c, d, e, a, b, f2, K2, 6, 6, x)
    b, d = one(b, c, d, e, a, f2, K2, 5, 13, x)
    a, c = one(a, b, c, d, e, f2, K2, 12, 11, x)
    e, b = one(e, a, b, c, d, f2, K2, 7, 5, x)
    d, a = one(d, e, a, b, c, f2, K2, 5, 12, x)  # #47
    return a, b, c, d, e


def _process_round_4(a, b, c, d, e, x):
    """Process Round 4 of RIPEMD-160.
    Example:
        >>> a0 = 0x67452301
        >>> b0 = 0xefcdab89
        >>> c0 = 0x98badcfe
        >>> d0 = 0x10325476
        >>> e0 = 0xc3d2e1f0
        >>> x = [0] * 16
        >>> a1, b1, c1, d1, e1 = _process_round_1(a0, b0, c0, d0, e0, x)
        >>> a2, b2, c2, d2, e2 = _process_round_2(a1, b1, c1, d1, e1, x)
        >>> a3, b3, c3, d3, e3 = _process_round_3(a2, b2, c2, d2, e2, x)
        >>> a4, b4, c4, d4, e4 = _process_round_4(a3, b3, c3, d3, e3, x)
        >>> # Final main round evolution
        >>> (a4 != a3) and (b4 != b3) and (c4 != c3) and (d4 != d3) and (e4 != e3)
        True
        >>> all(0 <= val <= 0xffffffff for val in [a4, b4, c4, d4, e4])
        True
        >>> # Test f3's complementary selection behavior
        >>> x_pattern = [0xaaaa5555] * 16  # Alternating bit pattern
        >>> a5, b5, c5, d5, e5 = _process_round_4(a3, b3, c3, d3, e3, x_pattern)
        >>> # Should show f3's unique conditional selection properties
        >>> (a5 != a4) or (b5 != b4) or (c5 != c4) or (d5 != d4) or (e5 != e4)
        True
    """
    c, e = one(c, d, e, a, b, f3, K3, 11, 1, x)
    b, d = one(b, c, d, e, a, f3, K3, 12, 9, x)
    a, c = one(a, b, c, d, e, f3, K3, 14, 11, x)
    e, b = one(e, a, b, c, d, f3, K3, 15, 10, x)
    d, a = one(d, e, a, b, c, f3, K3, 14, 0, x)
    c, e = one(c, d, e, a, b, f3, K3, 15, 8, x)
    b, d = one(b, c, d, e, a, f3, K3, 9, 12, x)
    a, c = one(a, b, c, d, e, f3, K3, 8, 4, x)
    e, b = one(e, a, b, c, d, f3, K3, 9, 13, x)
    d, a = one(d, e, a, b, c, f3, K3, 14, 3, x)
    c, e = one(c, d, e, a, b, f3, K3, 5, 7, x)
    b, d = one(b, c, d, e, a, f3, K3, 6, 15, x)
    a, c = one(a, b, c, d, e, f3, K3, 8, 14, x)
    e, b = one(e, a, b, c, d, f3, K3, 6, 5, x)
    d, a = one(d, e, a, b, c, f3, K3, 5, 6, x)
    c, e = one(c, d, e, a, b, f3, K3, 12, 2, x)  # #63
    return a, b, c, d, e


def _process_round_5(a, b, c, d, e, x):
    """
    Process Round 5 of RIPEMD-160 compression function.

    This round uses the boolean function f4, constant K4, and specific rotation
    amounts and message word indices as defined by the RIPEMD-160 specification.

    Parameters
    ----------
    a, b, c, d, e : int
        Five 32-bit state variables.
    x : list[int]
        List of sixteen 32-bit words from the message block.

    Returns
    -------
    tuple[int, int, int, int, int]
        Updated state variables (a, b, c, d, e).

    Examples
    --------
    >>> a0 = 0x67452301
    >>> b0 = 0xEFCDAB89
    >>> c0 = 0x98BADCFE
    >>> d0 = 0x10325476
    >>> e0 = 0xC3D2E1F0
    >>> x = [0]*16
    >>> a1, b1, c1, d1, e1 = _process_round_5(a0, b0, c0, d0, e0, x)
    >>> # Confirm the returned values differ from initial state
    >>> (a1 != a0) and (b1 != b0) and (c1 != c0) and (d1 != d0) and (e1 != e0)
    True
    >>> # Confirm all outputs fit within 32-bit unsigned integer range
    >>> all(0 <= v <= 0xFFFFFFFF for v in (a1, b1, c1, d1, e1))
    True
    """
    b, d = one(b, c, d, e, a, f4, K4, 9, 4, x)
    a, c = one(a, b, c, d, e, f4, K4, 15, 0, x)
    e, b = one(e, a, b, c, d, f4, K4, 5, 5, x)
    d, a = one(d, e, a, b, c, f4, K4, 11, 9, x)
    c, e = one(c, d, e, a, b, f4, K4, 6, 7, x)
    b, d = one(b, c, d, e, a, f4, K4, 8, 12, x)
    a, c = one(a, b, c, d, e, f4, K4, 13, 2, x)
    e, b = one(e, a, b, c, d, f4, K4, 12, 10, x)
    d, a = one(d, e, a, b, c, f4, K4, 5, 14, x)
    c, e = one(c, d, e, a, b, f4, K4, 12, 1, x)
    b, d = one(b, c, d, e, a, f4, K4, 13, 3, x)
    a, c = one(a, b, c, d, e, f4, K4, 14, 8, x)
    e, b = one(e, a, b, c, d, f4, K4, 11, 11, x)
    d, a = one(d, e, a, b, c, f4, K4, 8, 6, x)
    c, e = one(c, d, e, a, b, f4, K4, 5, 15, x)
    b, d = one(b, c, d, e, a, f4, K4, 6, 13, x)  # #79
    return a, b, c, d, e


def _process_parallel_round_1(a, b, c, d, e, x):
    """Process Parallel Round 1 of RIPEMD-160.

     Examples
    --------
    >>> a0 = 0x67452301
    >>> b0 = 0xEFCDAB89
    >>> c0 = 0x98BADCFE
    >>> d0 = 0x10325476
    >>> e0 = 0xC3D2E1F0
    >>> x = [0]*16
    >>> a1, b1, c1, d1, e1 = _process_parallel_round_1(a0, b0, c0, d0, e0, x)
    >>> (a1 != a0) and (b1 != b0) and (c1 != c0) and (d1 != d0) and (e1 != e0)
    True
    >>> all(0 <= v <= 0xFFFFFFFF for v in (a1, b1, c1, d1, e1))
    True
    """
    a, c = one(a, b, c, d, e, f4, KK0, 8, 5, x)
    e, b = one(e, a, b, c, d, f4, KK0, 9, 14, x)
    d, a = one(d, e, a, b, c, f4, KK0, 9, 7, x)
    c, e = one(c, d, e, a, b, f4, KK0, 11, 0, x)
    b, d = one(b, c, d, e, a, f4, KK0, 13, 9, x)
    a, c = one(a, b, c, d, e, f4, KK0, 15, 2, x)
    e, b = one(e, a, b, c, d, f4, KK0, 15, 11, x)
    d, a = one(d, e, a, b, c, f4, KK0, 5, 4, x)
    c, e = one(c, d, e, a, b, f4, KK0, 7, 13, x)
    b, d = one(b, c, d, e, a, f4, KK0, 7, 6, x)
    a, c = one(a, b, c, d, e, f4, KK0, 8, 15, x)
    e, b = one(e, a, b, c, d, f4, KK0, 11, 8, x)
    d, a = one(d, e, a, b, c, f4, KK0, 14, 1, x)
    c, e = one(c, d, e, a, b, f4, KK0, 14, 10, x)
    b, d = one(b, c, d, e, a, f4, KK0, 12, 3, x)
    a, c = one(a, b, c, d, e, f4, KK0, 6, 12, x)  # #15
    return a, b, c, d, e


def _process_parallel_round_2(a, b, c, d, e, x):
    """Process Parallel Round 2 of RIPEMD-160.
    Examples
    --------
    >>> a0 = 0x67452301
    >>> b0 = 0xEFCDAB89
    >>> c0 = 0x98BADCFE
    >>> d0 = 0x10325476
    >>> e0 = 0xC3D2E1F0
    >>> x = [0]*16
    >>> a1, b1, c1, d1, e1 = _process_parallel_round_2(a0, b0, c0, d0, e0, x)
    >>> (a1 != a0) and (b1 != b0) and (c1 != c0) and (d1 != d0) and (e1 != e0)
    True
    >>> all(0 <= val <= 0xFFFFFFFF for val in (a1, b1, c1, d1, e1))
    True
    """
    e, b = one(e, a, b, c, d, f3, KK1, 9, 6, x)
    d, a = one(d, e, a, b, c, f3, KK1, 13, 11, x)
    c, e = one(c, d, e, a, b, f3, KK1, 15, 3, x)
    b, d = one(b, c, d, e, a, f3, KK1, 7, 7, x)
    a, c = one(a, b, c, d, e, f3, KK1, 12, 0, x)
    e, b = one(e, a, b, c, d, f3, KK1, 8, 13, x)
    d, a = one(d, e, a, b, c, f3, KK1, 9, 5, x)
    c, e = one(c, d, e, a, b, f3, KK1, 11, 10, x)
    b, d = one(b, c, d, e, a, f3, KK1, 7, 14, x)
    a, c = one(a, b, c, d, e, f3, KK1, 7, 15, x)
    e, b = one(e, a, b, c, d, f3, KK1, 12, 8, x)
    d, a = one(d, e, a, b, c, f3, KK1, 7, 12, x)
    c, e = one(c, d, e, a, b, f3, KK1, 6, 4, x)
    b, d = one(b, c, d, e, a, f3, KK1, 15, 9, x)
    a, c = one(a, b, c, d, e, f3, KK1, 13, 1, x)
    e, b = one(e, a, b, c, d, f3, KK1, 11, 2, x)  # #31
    return a, b, c, d, e


def _process_parallel_round_3(a, b, c, d, e, x):
    """Process Parallel Round 3 of RIPEMD-160.
     Examples
    --------
    >>> a0 = 0x67452301
    >>> b0 = 0xEFCDAB89
    >>> c0 = 0x98BADCFE
    >>> d0 = 0x10325476
    >>> e0 = 0xC3D2E1F0
    >>> x = [0]*16
    >>> a1, b1, c1, d1, e1 = _process_parallel_round_2(a0, b0, c0, d0, e0, x)
    >>> (a1 != a0) and (b1 != b0) and (c1 != c0) and (d1 != d0) and (e1 != e0)
    True
    >>> all(0 <= v <= 0xFFFFFFFF for v in (a1, b1, c1, d1, e1))
    True
    """
    d, a = one(d, e, a, b, c, f2, KK2, 9, 15, x)
    c, e = one(c, d, e, a, b, f2, KK2, 7, 5, x)
    b, d = one(b, c, d, e, a, f2, KK2, 15, 1, x)
    a, c = one(a, b, c, d, e, f2, KK2, 11, 3, x)
    e, b = one(e, a, b, c, d, f2, KK2, 8, 7, x)
    d, a = one(d, e, a, b, c, f2, KK2, 6, 14, x)
    c, e = one(c, d, e, a, b, f2, KK2, 6, 6, x)
    b, d = one(b, c, d, e, a, f2, KK2, 14, 9, x)
    a, c = one(a, b, c, d, e, f2, KK2, 12, 11, x)
    e, b = one(e, a, b, c, d, f2, KK2, 13, 8, x)
    d, a = one(d, e, a, b, c, f2, KK2, 5, 12, x)
    c, e = one(c, d, e, a, b, f2, KK2, 14, 2, x)
    b, d = one(b, c, d, e, a, f2, KK2, 13, 10, x)
    a, c = one(a, b, c, d, e, f2, KK2, 13, 0, x)
    e, b = one(e, a, b, c, d, f2, KK2, 7, 4, x)
    d, a = one(d, e, a, b, c, f2, KK2, 5, 13, x)  # #47
    return a, b, c, d, e


def _process_parallel_round_4(a, b, c, d, e, x):
    """Process Parallel Round 4 of RIPEMD-160.
    Examples
    --------
    >>> a0 = 0x67452301
    >>> b0 = 0xEFCDAB89
    >>> c0 = 0x98BADCFE
    >>> d0 = 0x10325476
    >>> e0 = 0xC3D2E1F0
    >>> x = [0]*16
    >>> a1, b1, c1, d1, e1 = _process_parallel_round_4(a0, b0, c0, d0, e0, x)
    >>> (a1 != a0) and (b1 != b0) and (c1 != c0) and (d1 != d0) and (e1 != e0)
    True
    >>> all(0 <= v <= 0xFFFFFFFF for v in (a1, b1, c1, d1, e1))
    True
    """
    c, e = one(c, d, e, a, b, f1, KK3, 15, 8, x)
    b, d = one(b, c, d, e, a, f1, KK3, 5, 6, x)
    a, c = one(a, b, c, d, e, f1, KK3, 8, 4, x)
    e, b = one(e, a, b, c, d, f1, KK3, 11, 1, x)
    d, a = one(d, e, a, b, c, f1, KK3, 14, 3, x)
    c, e = one(c, d, e, a, b, f1, KK3, 14, 11, x)
    b, d = one(b, c, d, e, a, f1, KK3, 6, 15, x)
    a, c = one(a, b, c, d, e, f1, KK3, 14, 0, x)
    e, b = one(e, a, b, c, d, f1, KK3, 6, 5, x)
    d, a = one(d, e, a, b, c, f1, KK3, 9, 12, x)
    c, e = one(c, d, e, a, b, f1, KK3, 12, 2, x)
    b, d = one(b, c, d, e, a, f1, KK3, 9, 13, x)
    a, c = one(a, b, c, d, e, f1, KK3, 12, 9, x)
    e, b = one(e, a, b, c, d, f1, KK3, 5, 7, x)
    d, a = one(d, e, a, b, c, f1, KK3, 15, 10, x)
    c, e = one(c, d, e, a, b, f1, KK3, 8, 14, x)  # #63
    return a, b, c, d, e


def _process_parallel_round_5(a, b, c, d, e, x):
    """Process Parallel Round 5 of RIPEMD-160.
    Examples
    --------
    >>> a0 = 0x67452301
    >>> b0 = 0xEFCDAB89
    >>> c0 = 0x98BADCFE
    >>> d0 = 0x10325476
    >>> e0 = 0xC3D2E1F0
    >>> x = [0]*16
    >>> a1, b1, c1, d1, e1 = _process_parallel_round_5(a0, b0, c0, d0, e0, x)
    >>> (a1 != a0) and (b1 != b0) and (c1 != c0) and (d1 != d0) and (e1 != e0)
    True
    >>> all(0 <= v <= 0xFFFFFFFF for v in (a1, b1, c1, d1, e1))
    True
    """
    b, d = one(b, c, d, e, a, f0, KK4, 8, 12, x)
    a, c = one(a, b, c, d, e, f0, KK4, 5, 15, x)
    e, b = one(e, a, b, c, d, f0, KK4, 12, 10, x)
    d, a = one(d, e, a, b, c, f0, KK4, 9, 4, x)
    c, e = one(c, d, e, a, b, f0, KK4, 12, 1, x)
    b, d = one(b, c, d, e, a, f0, KK4, 5, 5, x)
    a, c = one(a, b, c, d, e, f0, KK4, 14, 8, x)
    e, b = one(e, a, b, c, d, f0, KK4, 6, 7, x)
    d, a = one(d, e, a, b, c, f0, KK4, 8, 6, x)
    c, e = one(c, d, e, a, b, f0, KK4, 13, 2, x)
    b, d = one(b, c, d, e, a, f0, KK4, 6, 13, x)
    a, c = one(a, b, c, d, e, f0, KK4, 5, 14, x)
    e, b = one(e, a, b, c, d, f0, KK4, 15, 0, x)
    d, a = one(d, e, a, b, c, f0, KK4, 13, 3, x)
    c, e = one(c, d, e, a, b, f0, KK4, 11, 9, x)
    b, d = one(b, c, d, e, a, f0, KK4, 11, 11, x)
    return a, b, c, d, e


def transform(state, block):
    """
    Transform the hash state using a 512-bit block of data.

    This is the core function of RIPEMD-160 that implements the compression
    function. It takes the current hash state and a 512-bit message block,
    then applies the RIPEMD-160 compression algorithm to produce a new state.

    RIPEMD-160 Architecture:
    The algorithm uses a dual-path structure with two parallel computation
    lines that process the same message block independently, then combines
    their results. This design provides resistance against certain attacks
    and increases the algorithm's security margin.

    Left Line Processing:
    - 5 rounds using functions f0, f1, f2, f3, f4 in sequence
    - Constants K0, K1, K2, K3, K4
    - Different message word permutations per round
    - Varying rotation amounts for each step

    Right Line (Parallel) Processing:
    - 5 rounds using functions f4, f3, f2, f1, f0 in reverse order
    - Constants KK0, KK1, KK2, KK3, KK4 (different from left line)
    - Different message permutations from left line
    - Different rotation patterns

    Final Combination:
    The results from both lines are combined with the original state using
    a carefully designed mixing operation that ensures both computation
    paths contribute to the final result.

    Cryptographic Rationale:
    1. Dual-path design makes it harder to find collisions since an attacker
       must satisfy constraints in both computation paths simultaneously
    2. Different boolean functions in each round provide varied non-linearity
    3. Message word permutations ensure each input bit affects many output bits
    4. Rotation amounts are chosen to maximize bit diffusion
    5. Round constants break symmetries and add structure

    Args:
        state (list[int]): Five 32-bit words representing current hash state.
                          Modified in-place to contain the new state.
        block (bytes): 64-byte message block to be processed.

    Raises:
        AssertionError: If system is not little-endian (implementation limitation).

    Examples:
        >>> import struct
        >>> # Test with standard RIPEMD-160 initial state
        >>> state = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]
        >>> original_state = state.copy()
        >>> # Test with zero block (64 bytes of zeros)
        >>> zero_block = b'\\x00' * 64
        >>> transform(state, zero_block)
        >>> # State should have changed
        >>> state != original_state
        True
        >>> # All state values should be valid 32-bit integers
        >>> all(0 <= val <= 0xffffffff for val in state)
        True

        >>> # Test with different block content
        >>> state2 = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]
        >>> # Block with all bytes set to 0x55 (alternating bit pattern)
        >>> pattern_block = b'\\x55' * 64
        >>> transform(state2, pattern_block)
        >>> # Should produce different result from zero block
        >>> state2 != state
        True

        >>> state_a = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]
        >>> state_b = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]
        >>> block_a = b'\\x00' * 64
        >>> block_b = b'\\x01' + b'\\x00' * 63  # Single bit difference
        >>> transform(state_a, block_a)
        >>> transform(state_b, block_b)
        >>> # States should be significantly different
        >>> sum(a != b for a, b in zip(state_a, state_b)) >= 3
        True
    """
    # Endianness check for correct byte interpretation
    assert sys.byteorder == "little", (
        "Only little endian is supported for RIPEMD-160 implementation. "
        "This limitation is due to the specific byte-order requirements "
        "of the algorithm specification and struct.unpack format strings."
    )

    # Parse 512-bit block into sixteen 32-bit words
    # Format '<16L' means: little-endian (<), 16 unsigned longs (L)
    # This converts the 64-byte block into 16 uint32 values
    x = struct.unpack("<16L", bytes(block[0:64]))

    # Extract current state for left-line processing
    # These values will be modified through 5 rounds of processing
    a = state[0]  # First state word (initially 0x67452301)
    b = state[1]  # Second state word (initially 0xEFCDAB89)
    c = state[2]  # Third state word (initially 0x98BADCFE)
    d = state[3]  # Fourth state word (initially 0x10325476)
    e = state[4]  # Fifth state word (initially 0xC3D2E1F0)

    # LEFT LINE PROCESSING (Main computation path)
    # Process through 5 rounds with different boolean functions
    # Each round processes all 16 message words with specific permutations

    # Round 1: f0 (XOR) - Linear mixing for initial diffusion
    a, b, c, d, e = _process_round_1(a, b, c, d, e, x)

    # Round 2: f1 (conditional) - First non-linear transformation
    a, b, c, d, e = _process_round_2(a, b, c, d, e, x)

    # Round 3: f2 (OR/XOR) - Second non-linear transformation
    a, b, c, d, e = _process_round_3(a, b, c, d, e, x)

    # Round 4: f3 (conditional variant) - Third non-linear transformation
    a, b, c, d, e = _process_round_4(a, b, c, d, e, x)

    # Round 5: f4 (XOR/OR) - Final non-linear transformation
    a, b, c, d, e = _process_round_5(a, b, c, d, e, x)

    # Save left-line results for final combination
    # These intermediate values represent the output of the left computation path
    aa = a  # Final left-line value for state[0] position
    bb = b  # Final left-line value for state[1] position
    cc = c  # Final left-line value for state[2] position
    dd = d  # Final left-line value for state[3] position
    ee = e  # Final left-line value for state[4] position

    # RIGHT LINE PROCESSING (Parallel computation path)
    # Reset to original state values for independent parallel processing
    # This creates the dual-path structure that strengthens RIPEMD-160
    a = state[0]
    b = state[1]
    c = state[2]
    d = state[3]
    e = state[4]

    # Process through 5 parallel rounds with reversed function order
    # Uses different constants, permutations, and rotations from left line

    # Parallel Round 1: f4 (XOR/OR) - Starts with what left line ended with
    a, b, c, d, e = _process_parallel_round_1(a, b, c, d, e, x)

    # Parallel Round 2: f3 (conditional variant) - Reverse of left round 4
    a, b, c, d, e = _process_parallel_round_2(a, b, c, d, e, x)

    # Parallel Round 3: f2 (OR/XOR) - Same as left round 3 but different params
    a, b, c, d, e = _process_parallel_round_3(a, b, c, d, e, x)

    # Parallel Round 4: f1 (conditional) - Same as left round 2 but different params
    a, b, c, d, e = _process_parallel_round_4(a, b, c, d, e, x)

    # Parallel Round 5: f0 (XOR) - Ends with what left line started with
    a, b, c, d, e = _process_parallel_round_5(a, b, c, d, e, x)

    # FINAL COMBINATION PHASE
    # Combine results from both computation paths with original state
    # This mixing ensures both paths contribute to the final hash state

    # The combination formula is carefully designed to:
    # 1. Include contributions from original state, left path, and right path
    # 2. Use a cyclic permutation to mix the state words
    # 3. Ensure that attacks must satisfy constraints in both paths

    # Temporary variable for state[1] since we overwrite states in sequence
    t = (state[1] + cc + d) % 0x100000000

    # Cyclic combination: each new state position gets contributions from:
    # - Original state at next position (cyclically)
    # - Left path result at corresponding position
    # - Right path result at corresponding position
    state[1] = (state[2] + dd + e) % 0x100000000  # state[2] + left_d + right_e
    state[2] = (state[3] + ee + a) % 0x100000000  # state[3] + left_e + right_a
    state[3] = (state[4] + aa + b) % 0x100000000  # state[4] + left_a + right_b
    state[4] = (state[0] + bb + c) % 0x100000000  # state[0] + left_b + right_c
    state[0] = t  # state[1] + left_c + right_d (from temporary)

    # The modulo 0x100000000 (2^32) ensures all values remain 32-bit
    # This combination scheme creates a strong avalanche effect where
    # small changes in either computation path affect the entire final state


if __name__ == "__main__":
    import doctest

    print("Running doctests for RIPEMD-160 ")
    doctest.testmod(verbose=True)
