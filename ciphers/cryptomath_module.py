"""
Cryptographic mathematics module for modular arithmetic operations.

This module provides utilities for cryptographic computations,
particularly modular multiplicative inverse.
"""

from maths.greatest_common_divisor import gcd_by_iterative


def find_mod_inverse(a: int, m: int) -> int:
    """
    Find the modular multiplicative inverse of a modulo m.

    The modular multiplicative inverse of a modulo m is an integer x
    such that (a * x) % m == 1. This only exists when gcd(a, m) == 1.

    Args:
        a: The number to find the inverse of
        m: The modulus

    Returns:
        The modular multiplicative inverse of a modulo m

    Raises:
        ValueError: If gcd(a, m) != 1 (inverse doesn't exist)

    >>> find_mod_inverse(7, 26)
    15
    >>> find_mod_inverse(3, 11)
    4
    >>> find_mod_inverse(5, 17)
    7
    >>> find_mod_inverse(1, 5)
    1
    >>> find_mod_inverse(2, 7)
    4
    """
    if gcd_by_iterative(a, m) != 1:
        msg = f"mod inverse of {a!r} and {m!r} does not exist"
        raise ValueError(msg)
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
