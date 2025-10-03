def get_nibbles(num: int) -> tuple[int, int]:
    """
    Return the upper and lower nibbles of an 8-bit integer.

    A nibble is 4 bits. The lower nibble is the last 4 bits, and
    the upper nibble is the first 4 bits of the 8-bit number.

    See also: https://en.wikipedia.org/wiki/Nibble

    >>> get_nibbles(100)   # binary: 01100100
    (6, 4)
    >>> get_nibbles(255)   # binary: 11111111
    (15, 15)
    >>> get_nibbles(0)     # binary: 00000000
    (0, 0)
    >>> get_nibbles(1)     # binary: 00000001
    (0, 1)
    >>> get_nibbles(240)   # binary: 11110000
    (15, 0)
    """
    lower = num & 0x0F
    upper = (num & 0xF0) >> 4
    return upper, lower


if __name__ == "__main__":
    import doctest

    doctest.testmod()
