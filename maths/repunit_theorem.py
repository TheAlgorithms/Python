"""
Utilities related to repunits and a classical repunit divisibility theorem.

A repunit of length ``k`` is the number made of ``k`` ones:
``R_k = 11...1``.

For every positive integer ``n`` with ``gcd(n, 10) = 1``,
there exists a repunit ``R_k`` divisible by ``n``.
"""

from math import gcd


def has_repunit_multiple(divisor: int) -> bool:
    """
    Check whether a divisor admits a repunit multiple.

    >>> has_repunit_multiple(7)
    True
    >>> has_repunit_multiple(13)
    True
    >>> has_repunit_multiple(2)
    False
    >>> has_repunit_multiple(25)
    False
    """
    if divisor <= 0:
        raise ValueError("divisor must be a positive integer")
    return gcd(divisor, 10) == 1


def least_repunit_length(divisor: int) -> int:
    """
    Return the smallest length ``k`` such that repunit ``R_k`` is divisible by divisor.

    Uses modular arithmetic to avoid constructing huge integers.

    >>> least_repunit_length(3)
    3
    >>> least_repunit_length(7)
    6
    >>> least_repunit_length(41)
    5
    """
    if divisor <= 0:
        raise ValueError("divisor must be a positive integer")
    if not has_repunit_multiple(divisor):
        raise ValueError("divisor must be coprime to 10")

    remainder = 0
    for length in range(1, divisor + 1):
        remainder = (remainder * 10 + 1) % divisor
        if remainder == 0:
            return length

    # Unreachable when gcd(divisor, 10) == 1 (pigeonhole principle theorem).
    raise ArithmeticError("no repunit length found for divisor")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
