"""
Finding the index of rightmost set bit has some very peculiar use-cases,
especially in finding missing or/and repeating numbers in a list of positive integers.
"""


def get_index_of_rightmost_set_bit(number: int) -> int:

    """
    Take in a positive integer 'number'.
    Returns the zero-based index of first set bit in that 'number' from right.
    Returns -1, If no set bit found.

    >>> get_index_of_rightmost_set_bit(0)
    -1
    >>> get_index_of_rightmost_set_bit(5)
    0
    >>> get_index_of_rightmost_set_bit(36)
    2
    >>> get_index_of_rightmost_set_bit(8)
    3
    >>> get_index_of_rightmost_set_bit(-18)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a non-negative integer
    """

    if number >= 0 and type(number) == int:
        temp = number
        intermediate = number & ~(number - 1)
        index = 0
        while intermediate:
            intermediate >>= 1
            index += 1
        return index - 1
    else:
        raise ValueError("Input must be a non-negative integer")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
