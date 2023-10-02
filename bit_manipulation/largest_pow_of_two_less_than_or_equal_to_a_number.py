"""
Author  : Naman Sharma
Date    : October 2, 2023

Task:
Find largest power of 2 less than or equal to a given number

Implementation notes: Use bit manipulation.
We start from 1 & left shift the set bit to check if (res<<1)<=number.
Each left bit shift represents a pow of 2.

For example:
number: 15
res:    1   0b1
        2   0b10
        4   0b100
        8   0b1000
        16  0b10000 (Exit)
"""


def largest_pow_of_two_less_than_or_equal_to_a_number(number: int) -> int:
    """
    Return the largest power of two less than or equal to a number.

    >>> largest_pow_of_two_less_than_or_equal_to_a_number(0)
    0
    >>> largest_pow_of_two_less_than_or_equal_to_a_number(1)
    1
    >>> largest_pow_of_two_less_than_or_equal_to_a_number(-1)
    0
    >>> largest_pow_of_two_less_than_or_equal_to_a_number(3)
    2
    >>> largest_pow_of_two_less_than_or_equal_to_a_number(15)
    8
    >>> largest_pow_of_two_less_than_or_equal_to_a_number(99)
    64
    >>> largest_pow_of_two_less_than_or_equal_to_a_number(178)
    128
    >>> largest_pow_of_two_less_than_or_equal_to_a_number(999999)
    524288
    >>> largest_pow_of_two_less_than_or_equal_to_a_number(99.9)
    Traceback (most recent call last):
        ...
    TypeError: Input value must be a 'int' type
    """
    if isinstance(number, float):
        raise TypeError("Input value must be a 'int' type")
    if number <= 0:
        return 0
    res = 1
    while (res << 1) <= number:
        res <<= 1
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
