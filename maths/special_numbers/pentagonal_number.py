"""
== Pentagonal Numbers ==
A pentagonal number is a figurate number that represents a pentagon. The nth
pentagonal number P(n) counts the dots in a pattern of nested pentagons that
share a common corner, where the outermost pentagon has n dots on each side.

The nth pentagonal number is given by the formula:

    P(n) = (3 * n * n - n) / 2

The sequence begins 1, 5, 12, 22, 35, 51, 70, ... for n = 1, 2, 3, ...

Reference: https://en.wikipedia.org/wiki/Pentagonal_number
"""

from math import isqrt


def is_pentagonal(number: int) -> bool:
    """
    Return True if ``number`` is a pentagonal number, otherwise False.

    A positive integer x is pentagonal if and only if (1 + sqrt(24x + 1)) / 6
    is a positive integer. This is the inverse of the pentagonal-number formula
    solved for n. The check is performed with integer arithmetic (math.isqrt)
    to avoid floating-point rounding errors for large inputs.

    >>> is_pentagonal(1)
    True
    >>> is_pentagonal(5)
    True
    >>> is_pentagonal(12)
    True
    >>> is_pentagonal(35)
    True
    >>> is_pentagonal(2)
    False
    >>> is_pentagonal(10)
    False
    >>> is_pentagonal(0)
    False
    >>> is_pentagonal(-5)
    False
    """
    if number < 1:
        return False
    discriminant = 24 * number + 1
    root = isqrt(discriminant)
    if root * root != discriminant:
        return False
    return (1 + root) % 6 == 0


def pentagonal(position: int) -> int:
    """
    Return the pentagonal number at the given 1-based ``position`` using the
    closed-form formula P(n) = (3 * n * n - n) / 2.

    >>> pentagonal(1)
    1
    >>> pentagonal(2)
    5
    >>> pentagonal(3)
    12
    >>> pentagonal(10)
    145
    >>> pentagonal(0)
    Traceback (most recent call last):
        ...
    ValueError: position must be a positive integer
    >>> pentagonal(-3)
    Traceback (most recent call last):
        ...
    ValueError: position must be a positive integer
    >>> pentagonal(1.5)
    Traceback (most recent call last):
        ...
    TypeError: position must be an integer
    """
    if not isinstance(position, int):
        raise TypeError("position must be an integer")
    if position < 1:
        raise ValueError("position must be a positive integer")
    return (3 * position * position - position) // 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("The first 10 pentagonal numbers are:")
    print([pentagonal(n) for n in range(1, 11)])
