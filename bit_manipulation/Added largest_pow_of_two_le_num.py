"""
Author  : Dwarkadhish Kamthane
Date    : October 2 2023
Task:
Find largest power of 2 less than or equal to a given number
"""


def largest_power_of_two(number: int) -> int:
    """
    Return the largest power of two less than or equal to a number.
    >>> largest_power_of_two(0)
    0
    >>> largest_power_of_two(1)
    1
    >>> largest_power_of_two(-1)
    0
    >>> largest_power_of_two(3)
    2
    >>> largest_power_of_two(15)
    8
    >>> largest_power_of_two(99)
    64
    >>> largest_power_of_two(178)
    128
    >>> largest_power_of_two(999999)
    524288
    >>> largest_power_of_two(99.9)
    Traceback (most recent call last):
        ...
    TypeError: Input value must be a 'int' type
    """
    if isinstance(number, float):
        raise TypeError("Please enter an int type input")
    if (number <= 0):
        return 0
    x = 1
    while (x << 1) <= number:
        x <<= 1
    return x


if __name__ == "__main__":
    import doctest

    doctest.testmod()