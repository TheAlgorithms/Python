"""
Classical simulation of Shor's Algorithm to factor integers.

Source: https://en.wikipedia.org/wiki/Shor%27s_algorithm
"""

import math
import random
from typing import Any


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    >>> is_prime(2)
    True
    >>> is_prime(4)
    False
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    r = math.isqrt(n)
    return all(n % i != 0 for i in range(3, r + 1, 2))


def modexp(a: int, b: int, m: int) -> int:
    """
    Modular exponentiation: (a^b) % m

    >>> modexp(2, 5, 13)
    6
    """
    result = 1
    a = a % m
    while b > 0:
        if b & 1:
            result = (result * a) % m
        a = (a * a) % m
        b >>= 1
    return result


def shor_classical(n: int, max_attempts: int = 10) -> str | tuple[int, int]:
    """
    Classical approximation of Shor's Algorithm to factor a number.

    >>> result = shor_classical(15)
    >>> isinstance(result, tuple)
    True
    >>> sorted(result) == [3, 5]
    True

    >>> shor_classical(13)  # Prime
    'No factors: 13 is prime'
    """
    if n <= 1:
        return "Failure: input must be > 1"
    if n % 2 == 0:
        return 2, n // 2
    if is_prime(n):
        return f"No factors: {n} is prime"

    for _ in range(max_attempts):
        a = random.randrange(2, n - 1)
        g = math.gcd(a, n)
        if g > 1:
            return g, n // g

        r = 1
        while r < n:
            if modexp(a, r, n) == 1:
                break
            r += 1
        else:
            continue

        if r % 2 != 0:
            continue
        x = modexp(a, r // 2, n)
        if x == n - 1:
            continue

        factor1 = math.gcd(x - 1, n)
        factor2 = math.gcd(x + 1, n)
        if factor1 not in (1, n) and factor2 not in (1, n):
            return factor1, factor2

    return "Failure: try more attempts"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
