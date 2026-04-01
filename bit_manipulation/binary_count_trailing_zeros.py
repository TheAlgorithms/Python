from math import log2


def binary_count_trailing_zeros(a: int) -> int:
    """
    Take in 1 integer, return the number of trailing zeros in binary representation.

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
    Traceback (most recent call last):
        ...
    ValueError: Trailing zeros for 0 are undefined
    >>> binary_count_trailing_zeros(-10)
    Traceback (most recent call last):
        ...
    ValueError: Input value must be a positive integer
    >>> binary_count_trailing_zeros(0.8)
    Traceback (most recent call last):
        ...
    TypeError: Input value must be an integer
    >>> binary_count_trailing_zeros("0")
    Traceback (most recent call last):
        ...
    TypeError: Input value must be an integer
    """

    # Type check
    if not isinstance(a, int):
        raise TypeError("Input value must be an integer")

    # Edge case: zero
    if a == 0:
        raise ValueError("Trailing zeros for 0 are undefined")

    # Negative numbers not allowed
    if a < 0:
        raise ValueError("Input value must be a positive integer")

    # Core logic
    return int(log2(a & -a))


if __name__ == "__main__":
    import doctest
    doctest.testmod()