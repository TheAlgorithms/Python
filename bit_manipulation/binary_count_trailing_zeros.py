from math import log2


def binary_count_trailing_zeros(a: int) -> int:
    """
    Return the number of trailing zeros in the binary
    representation of a non-negative integer.

    Note:
    For a == 0, returns 0 by convention.

    >>> binary_count_trailing_zeros(25)
    0
    >>> binary_count_trailing_zeros(36)
    2
    >>> binary_count_trailing_zeros(16)
    4
    >>> binary_count_trailing_zeros(58)
    1
    >>> binary_count_trailing_zeros(4294967296)
    32
    >>> binary_count_trailing_zeros(0)
    0
    >>> binary_count_trailing_zeros(-10)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a non-negative integer
    >>> binary_count_trailing_zeros(0.8)
    Traceback (most recent call last):
        ...
    TypeError: Input must be an integer
    >>> binary_count_trailing_zeros("0")
    Traceback (most recent call last):
        ...
    TypeError: Input must be an integer
    """

    if not isinstance(a, int):
        raise TypeError("Input must be an integer")

    if a < 0:
        raise ValueError("Input must be a non-negative integer")

    if a == 0:
        return 0

    return int(log2(a & -a))
