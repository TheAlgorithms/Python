#!/usr/bin/env python3
"""
Module for prime number operations
"""

import math


def is_prime(number: int) -> bool:
    """Checks to see if a number is a prime in O(sqrt(n)).

    A number is prime if it has exactly two factors: 1 and itself.

    >>> is_prime(0)
    False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(27)
    False
    >>> is_prime(563)
    True
    >>> is_prime(2999)
    True
    >>> is_prime(67483)
    False
    """

    if not isinstance(number, int) or number < 0:
        raise ValueError("'number' must be a non-negative integer")

    if number < 2:
        return False
    if number in (2, 3):
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(math.isqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def next_prime(value: int, factor: int = 1, **kwargs) -> int:
    """
    Returns the next prime number after (factor * value).
    If desc=True, returns the previous smaller prime number.

    >>> next_prime(5)
    7
    >>> next_prime(10)
    11
    >>> next_prime(7, desc=True)
    5
    >>> next_prime(2, desc=True)
    Traceback (most recent call last):
        ...
    ValueError: No smaller prime exists below 2.
    """

    if not isinstance(value, int) or value < 0:
        raise ValueError("'value' must be a non-negative integer")

    value *= factor
    descending = kwargs.get("desc", False)

    if descending:
        if value <= 2:
            raise ValueError("No smaller prime exists below 2.")
        value -= 1
        while value > 1 and not is_prime(value):
            value -= 1
    else:
        value += 1
        while not is_prime(value):
            value += 1

    return value


def generate_primes(limit: int) -> list[int]:
    """
    Generate all prime numbers up to the given limit (inclusive).

    >>> generate_primes(10)
    [2, 3, 5, 7]
    >>> generate_primes(1)
    []
    >>> generate_primes(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    if not isinstance(limit, int) or limit < 0:
        raise ValueError("'limit' must be a non-negative integer")

    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print("All doctests passed ✅")
