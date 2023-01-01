from collections.abc import Generator
from math import sin


def to_little_endian(bit_string_32: str) -> str:
    """[summary]
    Converts the given binary string to little-endian in groups of 8 chars.

    Arguments:
        bit_string_32 {[string]} -- [32 bit binary]

    Raises:
        ValueError -- [if the given string not are 32 bit binary string]

    Returns:
        [string] -- [32 bit binary string]
    >>> to_little_endian('1234567890abcdfghijklmnopqrstuvw')
    'pqrstuvwhijklmno90abcdfg12345678'
    """

    if len(bit_string_32) != 32:
        raise ValueError("Need length 32")
    little_endian = ""
    for i in [3, 2, 1, 0]:
        little_endian += bit_string_32[8 * i : 8 * i + 8]
    return little_endian


def reformat_hex(i: int) -> str:
    """[summary]
    Converts the given integer into 8-char little-endian hex number.

    Arguments:
        i {[int]} -- [integer]
    >>> reformat_hex(666)
    '9a020000'
    """

    hex_rep = format(i, "08x")
    little_endian_hex = ""
    for i in [3, 2, 1, 0]:
        little_endian_hex += hex_rep[2 * i : 2 * i + 2]
    return little_endian_hex


def preprocess(message: str) -> str:
    """[summary]
    Preprocesses the message string:
    - Convert message to bit string
    - Pad bit string to a multiple of 512 bits:
        - Append a 1
        - Append 0's until length = 448 (mod 512), 64 bits short of a multiple of 512
        - Append length of original message (64 bits)

    Arguments:
            message {[string]} -- [message string]

    Returns:
            [string] -- [padded bit string]
    """
    bit_string = ""
    for char in message:
        bit_string += format(ord(char), "08b")
    start_len = format(len(bit_string), "064b")
    bit_string += "1"
    while len(bit_string) % 512 != 448:
        bit_string += "0"
    bit_string += to_little_endian(start_len[32:]) + to_little_endian(start_len[:32])
    return bit_string


def get_block_words(bit_string: str) -> Generator[list[int], None, None]:
    """[summary]
    Iterator:
        Returns by each call a list of length 16 with the 32-bit
        integer blocks.

    Arguments:
        bit_string {[string]} -- [binary string >= 512]
    """

    for pos in range(0, len(bit_string), 512):
        block = bit_string[pos : pos + 512]
        block_words = []
        for i in range(0, 512, 32):
            block_words.append(int(to_little_endian(block[i : i + 32]), 2))
        yield block_words


def not_32(i: int) -> int:
    """
    >>> not_32(34)
    4294967261
    """
    i_str = format(i, "032b")
    new_str = ""
    for c in i_str:
        new_str += "1" if c == "0" else "0"
    return int(new_str, 2)


def sum_32(a: int, b: int) -> int:
    return (a + b) % 2**32


def left_rotate_32(i: int, shift: int) -> int:
    return (i << shift) ^ (i >> (32 - shift))


def md5_me(message: str) -> str:
    """[summary]
    Returns a 32-bit hash of the string 'message'

    Arguments:
        message {[string]} -- [message]

    >>> md5_me("")
    'd41d8cd98f00b204e9800998ecf8427e'
    >>> md5_me("The quick brown fox jumps over the lazy dog")
    '9e107d9d372bb6826bd81d3542a419d6'
    >>> md5_me("The quick brown fox jumps over the lazy dog.")
    'e4d909c290d0fb1ca068ffaddf22cbd0'
    """

    bit_string = preprocess(message)

    added_consts = [int(2**32 * abs(sin(i + 1))) for i in range(64)]

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

    for block_words in get_block_words(bit_string):
        a = a0
        b = b0
        c = c0
        d = d0
        for i in range(64):
            if i <= 15:
                # f = (b & c) | (not_32(b) & d)
                f = d ^ (b & (c ^ d))
                g = i
            elif i <= 31:
                # f = (d & b) | (not_32(d) & c)
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
        a0 = sum_32(a0, a)
        b0 = sum_32(b0, b)
        c0 = sum_32(c0, c)
        d0 = sum_32(d0, d)

    digest = reformat_hex(a0) + reformat_hex(b0) + reformat_hex(c0) + reformat_hex(d0)
    return digest


if __name__ == "__main__":
    import doctest

    doctest.testmod()
