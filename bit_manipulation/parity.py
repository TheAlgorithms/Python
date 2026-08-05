"""
Author  : Basuki Nath
Date    : 2025-10-04

Simple parity utility for integers.

The parity is 1 when the number of set bits is odd, otherwise 0.
"""


def parity(number: int) -> int:
    """
    Return 1 if `number` has an odd number of set bits, otherwise 0.

    >>> parity(0)
    0
    >>> parity(1)
    1
    >>> parity(2)  # 10b -> one set bit
    1
    >>> parity(3)  # 11b -> two set bits
    0
    >>> parity(1023)  # 10 ones -> even
    0
    >>> parity(-1)
    Traceback (most recent call last):
        ...
    ValueError: number must not be negative
    """
    if number < 0:
        raise ValueError("number must not be negative")
    # Kernighan's algorithm toggling parity
    p = 0
    while number:
        p ^= 1
        number &= number - 1
    return p


if __name__ == "__main__":
    import doctest

    doctest.testmod()
