"""
Generate prime numbers up to a given limit using different approaches.
"""

from collections.abc import Iterator
from math import isqrt


def slow_primes(max_n: int) -> Iterator[int]:
    """
    Generate prime numbers up to max_n using a slow approach.

    >>> list(slow_primes(10))
    [2, 3, 5, 7]
    >>> list(slow_primes(1))
    []
    >>> list(slow_primes(-5))
    []
    """
    for num in range(2, max_n + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num


def primes(max_n: int) -> Iterator[int]:
    """
    Generate prime numbers up to max_n using an optimized approach.

    >>> list(primes(10))
    [2, 3, 5, 7]
    >>> list(primes(1))
    []
    >>> list(primes(0))
    []
    """
    for num in range(2, max_n + 1):
        for i in range(2, isqrt(num) + 1):
            if num % i == 0:
                break
        else:
            yield num


def fast_primes(max_n: int) -> Iterator[int]:
    """
    Generate prime numbers up to max_n using the Sieve of Eratosthenes.

    >>> list(fast_primes(10))
    [2, 3, 5, 7]
    >>> list(fast_primes(1))
    []
    """
    if max_n < 2:
        return iter(())

    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False

    for num in range(2, isqrt(max_n) + 1):
        if sieve[num]:
            for multiple in range(num * num, max_n + 1, num):
                sieve[multiple] = False

    return (num for num in range(2, max_n + 1) if sieve[num])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
