"""
The MD5 algorithm is a hash function that's commonly used as a checksum to
detect data corruption. The algorithm works by processing a given message in
blocks of 512 bits, padding the message as needed. It uses the blocks to operate
a 128-bit state and performs a total of 64 such operations. Note that all values
are little-endian, so inputs are converted as needed.

Although MD5 was used as a cryptographic hash function in the past, it's since
been cracked, so it shouldn't be used for security purposes.

For more info, see https://en.wikipedia.org/wiki/MD5
"""

from collections.abc import Generator
from math import sin


def to_little_endian(string_32: bytes) -> bytes:
    """
    Converts the given string to little-endian in groups of 8 chars.

    Arguments:
        string_32 {[string]} -- [32-char string]

    Raises:
        ValueError -- [input is not 32 char]

    Returns:
        32-char little-endian string
    >>> to_little_endian(b'1234567890abcdfghijklmnopqrstuvw')
    b'pqrstuvwhijklmno90abcdfg12345678'
    >>> to_little_endian(b'1234567890')
    Traceback (most recent call last):
    ...
    ValueError: Input must be of length 32
    """
    if len(string_32) != 32:
        raise ValueError("Input must be of length 32")

    little_endian = b""
    for i in [3, 2, 1, 0]:
        little_endian += string_32[8 * i : 8 * i + 8]
    return little_endian


def reformat_hex(i: int) -> bytes:
    """
    Converts the given non-negative integer to hex string.

    Example: Suppose the input is the following:
        i = 1234

        The input is 0x000004d2 in hex, so the little-endian hex string is
        "d2040000".

    Arguments:
        i {[int]} -- [integer]

    Raises:
        ValueError -- [input is negative]

    Returns:
        8-char little-endian hex string

    >>> reformat_hex(1234)
    b'd2040000'
    >>> reformat_hex(666)
    b'9a020000'
    >>> reformat_hex(0)
    b'00000000'
    >>> reformat_hex(1234567890)
    b'd2029649'
    >>> reformat_hex(1234567890987654321)
    b'b11c6cb1'
    >>> reformat_hex(-1)
    Traceback (most recent call last):
    ...
    ValueError: Input must be non-negative
    """
    if i < 0:
        raise ValueError("Input must be non-negative")

    hex_rep = format(i, "08x")[-8:]
    little_endian_hex = b""
    for i in [3, 2, 1, 0]:
        little_endian_hex += hex_rep[2 * i : 2 * i + 2].encode("utf-8")
    return little_endian_hex


def preprocess(message: bytes) -> bytes:
    """
    Preprocesses the message string:
    - Convert message to bit string
    - Pad bit string to a multiple of 512 chars:
        - Append a 1
        - Append 0's until length = 448 (mod 512)
        - Append length of original message (64 chars)

    Example: Suppose the input is the following:
        message = "a"

        The message bit string is "01100001", which is 8 bits long. Thus, the
        bit string needs 439 bits of padding so that
        (bit_string + "1" + padding) = 448 (mod 512).
        The message length is "000010000...0" in 64-bit little-endian binary.
        The combined bit string is then 512 bits long.

    Arguments:
        message {[string]} -- [message string]

    Returns:
        processed bit string padded to a multiple of 512 chars

    >>> preprocess(b"a") == (b"01100001" + b"1" +
    ...                     (b"0" * 439) + b"00001000" + (b"0" * 56))
    True
    >>> preprocess(b"") == b"1" + (b"0" * 447) + (b"0" * 64)
    True
    """
    bit_string = b""
    for char in message:
        bit_string += format(char, "08b").encode("utf-8")
    start_len = format(len(bit_string), "064b").encode("utf-8")

    # Pad bit_string to a multiple of 512 chars
    bit_string += b"1"
    while len(bit_string) % 512 != 448:
        bit_string += b"0"
    bit_string += to_little_endian(start_len[32:]) + to_little_endian(start_len[:32])

    return bit_string


def get_block_words(bit_string: bytes) -> Generator[list[int], None, None]:
    """
    Splits bit string into blocks of 512 chars and yields each block as a list
    of 32-bit words

    Example: Suppose the input is the following:
        bit_string =
            "000000000...0" +  # 0x00 (32 bits, padded to the right)
            "000000010...0" +  # 0x01 (32 bits, padded to the right)
            "000000100...0" +  # 0x02 (32 bits, padded to the right)
            "000000110...0" +  # 0x03 (32 bits, padded to the right)
            ...
            "000011110...0"    # 0x0a (32 bits, padded to the right)

        Then len(bit_string) == 512, so there'll be 1 block. The block is split
        into 32-bit words, and each word is converted to little endian. The
        first word is interpreted as 0 in decimal, the second word is
        interpreted as 1 in decimal, etc.

        Thus, block_words == [[0, 1, 2, 3, ..., 15]].

    Arguments:
        bit_string {[string]} -- [bit string with multiple of 512 as length]

    Raises:
        ValueError -- [length of bit string isn't multiple of 512]

    Yields:
        a list of 16 32-bit words

    >>> test_string = ("".join(format(n << 24, "032b") for n in range(16))
    ...                  .encode("utf-8"))
    >>> list(get_block_words(test_string))
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]
    >>> list(get_block_words(test_string * 4)) == [list(range(16))] * 4
    True
    >>> list(get_block_words(b"1" * 512)) == [[4294967295] * 16]
    True
    >>> list(get_block_words(b""))
    []
    >>> list(get_block_words(b"1111"))
    Traceback (most recent call last):
    ...
    ValueError: Input must have length that's a multiple of 512
    """
    if len(bit_string) % 512 != 0:
        raise ValueError("Input must have length that's a multiple of 512")

    for pos in range(0, len(bit_string), 512):
        block = bit_string[pos : pos + 512]
        block_words = []
        for i in range(0, 512, 32):
            block_words.append(int(to_little_endian(block[i : i + 32]), 2))
        yield block_words


def not_32(i: int) -> int:
    """
    Perform bitwise NOT on given int.

    Arguments:
        i {[int]} -- [given int]

    Raises:
        ValueError -- [input is negative]

    Returns:
        Result of bitwise NOT on i

    >>> not_32(34)
    4294967261
    >>> not_32(1234)
    4294966061
    >>> not_32(4294966061)
    1234
    >>> not_32(0)
    4294967295
    >>> not_32(1)
    4294967294
    >>> not_32(-1)
    Traceback (most recent call last):
    ...
    ValueError: Input must be non-negative
    """
    if i < 0:
        raise ValueError("Input must be non-negative")

    i_str = format(i, "032b")
    new_str = ""
    for c in i_str:
        new_str += "1" if c == "0" else "0"
    return int(new_str, 2)


def sum_32(a: int, b: int) -> int:
    """
    Add two numbers as 32-bit ints.

    Arguments:
        a {[int]} -- [first given int]
        b {[int]} -- [second given int]

    Returns:
        (a + b) as an unsigned 32-bit int

    >>> sum_32(1, 1)
    2
    >>> sum_32(2, 3)
    5
    >>> sum_32(0, 0)
    0
    >>> sum_32(-1, -1)
    4294967294
    >>> sum_32(4294967295, 1)
    0
    """
    return (a + b) % 2**32


def left_rotate_32(i: int, shift: int) -> int:
    """
    Rotate the bits of a given int left by a given amount.

    Arguments:
        i {[int]} -- [given int]
        shift {[int]} -- [shift amount]

    Raises:
        ValueError -- [either given int or shift is negative]

    Returns:
        `i` rotated to the left by `shift` bits

    >>> left_rotate_32(1234, 1)
    2468
    >>> left_rotate_32(1111, 4)
    17776
    >>> left_rotate_32(2147483648, 1)
    1
    >>> left_rotate_32(2147483648, 3)
    4
    >>> left_rotate_32(4294967295, 4)
    4294967295
    >>> left_rotate_32(1234, 0)
    1234
    >>> left_rotate_32(0, 0)
    0
    >>> left_rotate_32(-1, 0)
    Traceback (most recent call last):
    ...
    ValueError: Input must be non-negative
    >>> left_rotate_32(0, -1)
    Traceback (most recent call last):
    ...
    ValueError: Shift must be non-negative
    """
    if i < 0:
        raise ValueError("Input must be non-negative")
    if shift < 0:
        raise ValueError("Shift must be non-negative")
    return ((i << shift) ^ (i >> (32 - shift))) % 2**32


def md5_me(message: bytes) -> bytes:
    """
    Returns the 32-char MD5 hash of a given message.

    Reference: https://en.wikipedia.org/wiki/MD5#Algorithm

    Arguments:
        message {[string]} -- [message]

    Returns:
        32-char MD5 hash string

    >>> md5_me(b"")
    b'd41d8cd98f00b204e9800998ecf8427e'
    >>> md5_me(b"The quick brown fox jumps over the lazy dog")
    b'9e107d9d372bb6826bd81d3542a419d6'
    >>> md5_me(b"The quick brown fox jumps over the lazy dog.")
    b'e4d909c290d0fb1ca068ffaddf22cbd0'

    >>> import hashlib
    >>> from string import ascii_letters
    >>> msgs = [b"", ascii_letters.encode("utf-8"), "Üñîçø∂é".encode("utf-8"),
    ...         b"The quick brown fox jumps over the lazy dog."]
    >>> all(md5_me(msg) == hashlib.md5(msg).hexdigest().encode("utf-8") for msg in msgs)
    True
    """

    # Convert to bit string, add padding and append message length
    bit_string = preprocess(message)

    added_consts = [int(2**32 * abs(sin(i + 1))) for i in range(64)]

    # Starting states
    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    shift_amounts = [
        7,
        12,
        17,
        22,
        7,
        12,
        17,
        22,
        7,
        12,
        17,
        22,
        7,
        12,
        17,
        22,
        5,
        9,
        14,
        20,
        5,
        9,
        14,
        20,
        5,
        9,
        14,
        20,
        5,
        9,
        14,
        20,
        4,
        11,
        16,
        23,
        4,
        11,
        16,
        23,
        4,
        11,
        16,
        23,
        4,
        11,
        16,
        23,
        6,
        10,
        15,
        21,
        6,
        10,
        15,
        21,
        6,
        10,
        15,
        21,
        6,
        10,
        15,
        21,
    ]

    # Process bit string in chunks, each with 16 32-char words
    for block_words in get_block_words(bit_string):
        a = a0
        b = b0
        c = c0
        d = d0

        # Hash current chunk
        for i in range(64):
            if i <= 15:
                # f = (b & c) | (not_32(b) & d)     # Alternate definition for f
                f = d ^ (b & (c ^ d))
                g = i
            elif i <= 31:
                # f = (d & b) | (not_32(d) & c)     # Alternate definition for f
                f = c ^ (d & (b ^ c))
                g = (5 * i + 1) % 16
            elif i <= 47:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
            else:
                f = c ^ (b | not_32(d))
                g = (7 * i) % 16
            f = (f + a + added_consts[i] + block_words[g]) % 2**32
            a = d
            d = c
            c = b
            b = sum_32(b, left_rotate_32(f, shift_amounts[i]))

        # Add hashed chunk to running total
        a0 = sum_32(a0, a)
        b0 = sum_32(b0, b)
        c0 = sum_32(c0, c)
        d0 = sum_32(d0, d)

    digest = reformat_hex(a0) + reformat_hex(b0) + reformat_hex(c0) + reformat_hex(d0)
    return digest


if __name__ == "__main__":
    import doctest

    doctest.testmod()
