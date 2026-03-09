"""
Author  : Alexander Pantyukhin
Date    : November 30, 2022

Task:
Given two int numbers. Return True these numbers have opposite signs
or False otherwise.

Implementation notes: Use bit manipulation.
Use XOR for two numbers.
"""


def different_signs(num1: int, num2: int) -> bool:
    """
    Return True if numbers have opposite signs False otherwise.

    >>> different_signs(1, -1)
    True
    >>> different_signs(1, 1)
    False
    >>> different_signs(1000000000000000000000000000, -1000000000000000000000000000)
    True
    >>> different_signs(-1000000000000000000000000000, 1000000000000000000000000000)
    True
    >>> different_signs(50, 278)
    False
    >>> different_signs(0, 2)
    False
    >>> different_signs(2, 0)
    False
    """
    return num1 ^ num2 < 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
