"""
Author  : Basuki Nath
Date    : 2025-10-04

Bit rotation helpers for 32-bit unsigned integers.
"""


def rotate_left32(x: int, k: int) -> int:
    """
    Rotate the lower 32 bits of x left by k and return result in 0..2**32-1.

    >>> rotate_left32(1, 1)
    2
    >>> rotate_left32(1, 31)
    2147483648
    >>> rotate_left32(0x80000000, 1)
    1
    >>> rotate_left32(0x12345678, 4)
    591751041
    >>> rotate_left32(-1, 3)
    Traceback (most recent call last):
        ...
    ValueError: x must be a non-negative integer
    >>> rotate_left32(1, -1)
    Traceback (most recent call last):
        ...
    ValueError: k must be non-negative
    """
    if not isinstance(x, int) or x < 0:
        raise ValueError("x must be a non-negative integer")
    if not isinstance(k, int) or k < 0:
        raise ValueError("k must be non-negative")
    mask = (1 << 32) - 1
    k &= 31
    return ((x << k) & mask) | ((x & mask) >> (32 - k))


def rotate_right32(x: int, k: int) -> int:
    """
    Rotate the lower 32 bits of x right by k and return result in 0..2**32-1.

    >>> rotate_right32(2, 1)
    1
    >>> rotate_right32(1, 1)
    2147483648
    >>> rotate_right32(0x12345678, 4)
    2166572391
    >>> rotate_right32(-1, 1)
    Traceback (most recent call last):
        ...
    ValueError: x must be a non-negative integer
    >>> rotate_right32(1, -3)
    Traceback (most recent call last):
        ...
    ValueError: k must be non-negative
    """
    if not isinstance(x, int) or x < 0:
        raise ValueError("x must be a non-negative integer")
    if not isinstance(k, int) or k < 0:
        raise ValueError("k must be non-negative")
    mask = (1 << 32) - 1
    k &= 31
    return ((x & mask) >> k) | ((x << (32 - k)) & mask)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
