"""
== Evil Number ==
An evil number is a non-negative integer that has an even number of 1s in its
binary expansion. Numbers that are not evil are called odious numbers.

Examples of evil numbers: 0, 3, 5, 6, 9, 10, 12, 15, 17, 18, 20, 23, 24, 27, ...
Reference: https://en.wikipedia.org/wiki/Evil_number
"""


def is_evil_number(number: int) -> bool:
    """
    Check if a given number is an evil number.

    A non-negative integer is evil if the sum of its binary digits (its Hamming weight)
    is even.

    :param number: A non-negative integer.
    :return: True if number is an evil number, False otherwise.

    >>> is_evil_number(0)
    True
    >>> is_evil_number(3)
    True
    >>> is_evil_number(5)
    True
    >>> is_evil_number(6)
    True
    >>> is_evil_number(9)
    True
    >>> is_evil_number(1)
    False
    >>> is_evil_number(2)
    False
    >>> is_evil_number(4)
    False
    >>> is_evil_number(7)
    False
    >>> is_evil_number(8)
    False
    >>> is_evil_number(-1)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a non-negative integer
    >>> is_evil_number(5.5)
    Traceback (most recent call last):
        ...
    TypeError: Input must be an integer
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    if number < 0:
        raise ValueError("Input must be a non-negative integer")

    count = 0
    temp = number
    while temp > 0:
        if temp % 2 == 1:
            count += 1
        temp = temp // 2
    return count % 2 == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
