"""Sieve of Eratosthenes for generating primes up to n."""

from typing import List


def sieve_of_eratosthenes(limit: int) -> List[int]:
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    p = 2
    while p * p <= limit:
        if sieve[p]:
            for multiple in range(p * p, limit + 1, p):
                sieve[multiple] = False
        p += 1
    return [num for num, is_prime in enumerate(sieve) if is_prime]
