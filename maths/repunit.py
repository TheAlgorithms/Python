"""
Repunit Theorem: Divisibility of repunit and repeated-digit numbers.

A repunit R(n) is a number consisting of n ones: 1, 11, 111, 1111, ...
More generally, a repeated-digit number like 777...7 (n digits) equals
7 * R(n), where R(n) = (10^n - 1) / 9.

Key theorem: A prime p (p != 2, 5) divides R(n) if and only if n is a
multiple of the multiplicative order of 10 modulo p — that is, the
smallest positive k such that 10^k ≡ 1 (mod p).

This enables O(log n) divisibility checks for numbers with millions of digits,
without ever constructing the number itself.

References:
  - https://en.wikipedia.org/wiki/Repunit
  - https://en.wikipedia.org/wiki/Multiplicative_order
  - Hardy & Wright, "An Introduction to the Theory of Numbers", §9
"""

from math import gcd


def multiplicative_order(base: int, modulus: int) -> int:
    """
    Return the multiplicative order of *base* modulo *modulus*: the smallest
    positive integer k such that base^k ≡ 1 (mod modulus).

    The order exists only when gcd(base, modulus) == 1; a ValueError is raised
    otherwise.

    :param base: The base integer (must be coprime to modulus).
    :param modulus: A positive integer >= 2.
    :return: The multiplicative order k.

    Examples:
    >>> multiplicative_order(10, 7)
    6
    >>> multiplicative_order(10, 11)
    2
    >>> multiplicative_order(10, 13)
    6
    >>> multiplicative_order(10, 17)
    16
    >>> multiplicative_order(3, 7)
    6
    >>> multiplicative_order(2, 5)
    4
    >>> multiplicative_order(10, 25)
    Traceback (most recent call last):
        ...
    ValueError: base 10 and modulus 25 share a common factor; gcd = 5
    >>> multiplicative_order(10, 2)
    Traceback (most recent call last):
        ...
    ValueError: base 10 and modulus 2 share a common factor; gcd = 2
    >>> multiplicative_order(10, 1)
    Traceback (most recent call last):
        ...
    ValueError: modulus must be >= 2, got 1
    """
    if modulus < 2:
        raise ValueError(f"modulus must be >= 2, got {modulus}")
    g = gcd(base, modulus)
    if g != 1:
        raise ValueError(
            f"base {base} and modulus {modulus} share a common factor; gcd = {g}"
        )
    order = 1
    current = base % modulus
    while current != 1:
        current = (current * base) % modulus
        order += 1
    return order


def repunit_length_for_prime(prime: int) -> int:
    """
    Return the smallest n such that the repunit R(n) = 111...1 (n ones)
    is divisible by *prime*.

    By the repunit theorem this equals the multiplicative order of 10 mod
    *prime*.  The function raises ValueError for primes 2 and 5, which never
    divide any repunit (since repunits are odd and not divisible by 5).

    :param prime: A prime number other than 2 or 5.
    :return: Smallest n >= 1 such that prime | R(n).

    Examples:
    >>> repunit_length_for_prime(7)
    6
    >>> repunit_length_for_prime(11)
    2
    >>> repunit_length_for_prime(13)
    6
    >>> repunit_length_for_prime(41)
    5
    >>> repunit_length_for_prime(239)
    7
    >>> repunit_length_for_prime(2)
    Traceback (most recent call last):
        ...
    ValueError: prime must not be 2 or 5 (repunits are never divisible by 2 or 5)
    >>> repunit_length_for_prime(5)
    Traceback (most recent call last):
        ...
    ValueError: prime must not be 2 or 5 (repunits are never divisible by 2 or 5)
    """
    if prime in (2, 5):
        raise ValueError(
            "prime must not be 2 or 5 (repunits are never divisible by 2 or 5)"
        )
    return multiplicative_order(10, prime)


def is_repunit(n: int) -> bool:
    """
    Return True if *n* is a repunit (consists solely of the digit 1).

    :param n: A positive integer.

    Examples:
    >>> is_repunit(1)
    True
    >>> is_repunit(11)
    True
    >>> is_repunit(111)
    True
    >>> is_repunit(1111111111111)
    True
    >>> is_repunit(12)
    False
    >>> is_repunit(121)
    False
    >>> is_repunit(0)
    False
    >>> is_repunit(-1)
    False
    """
    if n <= 0:
        return False
    return all(digit == "1" for digit in str(n))


def repunit_divisible_by(n: int, prime: int) -> bool:
    """
    Return True if the n-digit repunit R(n) = 111...1 is divisible by *prime*,
    using O(log prime) arithmetic — no need to build the repunit itself.

    The theorem states: prime | R(n) iff ord_{prime}(10) | n,
    where ord_{prime}(10) is the multiplicative order of 10 mod prime.

    :param n: Number of digits in the repunit (positive integer).
    :param prime: A prime != 2 and != 5.

    Examples:
    >>> repunit_divisible_by(6, 7)
    True
    >>> repunit_divisible_by(3, 7)
    False
    >>> repunit_divisible_by(2, 11)
    True
    >>> repunit_divisible_by(1, 11)
    False
    >>> repunit_divisible_by(5, 41)
    True
    >>> repunit_divisible_by(4, 41)
    False
    """
    order = repunit_length_for_prime(prime)
    return n % order == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
