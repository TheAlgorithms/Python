"""
Project Euler Problem 50: https://projecteuler.net/problem=50

Consecutive prime sum

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

from __future__ import annotations


def prime_sieve(limit: int) -> list[int]:
    """
    Sieve of Erotosthenes
    Function to return all the prime numbers up to a number 'limit'
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    >>> prime_sieve(3)
    [2]

    >>> prime_sieve(50)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    is_prime = [True] * limit
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True

    for i in range(3, int(limit**0.5 + 1), 2):
        index = i * 2
        while index < limit:
            is_prime[index] = False
            index = index + i

    primes = [2]

    for i in range(3, limit, 2):
        if is_prime[i]:
            primes.append(i)

    return primes


def solution(ceiling: int = 1_000_000) -> int:
    """
    Returns the biggest prime, below the celing, that can be written as the sum
    of consecutive the most consecutive primes.

    >>> solution(500)
    499

    >>> solution(1_000)
    953

    >>> solution(10_000)
    9521
    """
    primes = prime_sieve(ceiling)
    length = 0
    largest = 0

    for i in range(len(primes)):
        for j in range(i + length, len(primes)):
            sol = sum(primes[i:j])
            if sol >= ceiling:
                break

            if sol in primes:
                length = j - i
                largest = sol

    return largest


if __name__ == "__main__":
    print(f"{solution() = }")
