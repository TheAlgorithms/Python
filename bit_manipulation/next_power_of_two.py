"""
Author  : Basuki Nath
Date    : 2025-10-04

Utility to compute the next power of two greater than or equal to n.
"""


def next_power_of_two(n: int) -> int:
    """
    Return the smallest power of two >= n for positive integers.

    >>> next_power_of_two(1)
    1
    >>> next_power_of_two(2)
    2
    >>> next_power_of_two(3)
    4
    >>> next_power_of_two(5)
    8
    >>> next_power_of_two(1025)
    2048
    >>> next_power_of_two(0)
    Traceback (most recent call last):
        ...
    ValueError: n must be positive
    >>> next_power_of_two(-3)
    Traceback (most recent call last):
        ...
    ValueError: n must be positive
    """
    if n <= 0:
        raise ValueError("n must be positive")
    # If already a power of two, return it
    if n & (n - 1) == 0:
        return n
    # Otherwise, fill bits to the right
    v = n - 1
    v |= v >> 1
    v |= v >> 2
    v |= v >> 4
    v |= v >> 8
    v |= v >> 16
    # for very large ints, continue shifting using Python's arbitrary precision
    shift = 32
    while (1 << shift) <= v:
        v |= v >> shift
        shift <<= 1
    return v + 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
