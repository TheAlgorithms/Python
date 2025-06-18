"""
Classical simulation of Shor's Algorithm to factor integers.

Source: https://en.wikipedia.org/wiki/Shor%27s_algorithm
"""

import random
import math
from typing import Tuple, Union


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
    r = int(math.isqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True


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


def shor_classical(N: int, max_attempts: int = 10) -> Union[str, Tuple[int, int]]:
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
    if N <= 1:
        return "Failure: input must be > 1"
    if N % 2 == 0:
        return 2, N // 2
    if is_prime(N):
        return f"No factors: {N} is prime"

    for _ in range(max_attempts):
        a = random.randrange(2, N - 1)
        g = math.gcd(a, N)
        if g > 1:
            return g, N // g

        r = 1
        while r < N:
            if modexp(a, r, N) == 1:
                break
            r += 1
        else:
            continue

        if r % 2 != 0:
            continue
        x = modexp(a, r // 2, N)
        if x == N - 1:
            continue

        factor1 = math.gcd(x - 1, N)
        factor2 = math.gcd(x + 1, N)
        if factor1 not in (1, N) and factor2 not in (1, N):
            return factor1, factor2

    return "Failure: try more attempts"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
