from math import log2


def binary_count_trailing_zeros(a: int) -> int:
    """
    Take in 1 integer, return a number that is
    the number of trailing zeros in binary representation of that number.

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
    ValueError: Input value must be a positive integer
    >>> binary_count_trailing_zeros(0.8)
    Traceback (most recent call last):
        ...
    TypeError: Input value must be a 'int' type
    >>> binary_count_trailing_zeros("0")
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    """
    if a < 0:
        raise ValueError("Input value must be a positive integer")
    elif isinstance(a, float):
        raise TypeError("Input value must be a 'int' type")
    return 0 if (a == 0) else int(log2(a & -a))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
