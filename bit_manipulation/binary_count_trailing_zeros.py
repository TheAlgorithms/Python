from math import log2


def binary_count_trailing_zeros(a: int) -> int:
    """
    Take in 1 integer, return a number that is
    the number of trailing zeros in binary representation of that number.
    Counts consecutive zero bits at the right (least significant) end of the binary
    representation. Uses the clever trick: a & -a isolates the lowest set bit,
    then log2 finds its position.
    Algorithm:
    1. Handle special case: if number is 0, return 0 (no set bits, no trailing zeros)
    2. Compute a & -a: This isolates the lowest set bit (e.g., 0b1000 for 0b11000)
    3. Apply log2 to get the position (which equals the number of trailing zeros)
    Example 1: 36 = 0b100100
    - Lowest set bit: 0b100 (position 2)
    - Trailing zeros: 2
    Example 2: 16 = 0b10000
    - Lowest set bit: 0b10000 (position 4)
    - Trailing zeros: 4

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
