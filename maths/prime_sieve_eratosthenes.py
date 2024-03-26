"""
Sieve of Eratosthenes

Input: n = 10
Output: 2 3 5 7

Input: n = 20
Output: 2 3 5 7 11 13 17 19

you can read in detail about this at
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

from math import isqrt

import numpy as np


def prime_sieve_eratosthenes(num: int) -> list[int]:
    """
    Print the prime numbers up to n

    >>> prime_sieve_eratosthenes(10)
    [2, 3, 5, 7]
    >>> prime_sieve_eratosthenes(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> prime_sieve_eratosthenes(2)
    [2]
    >>> prime_sieve_eratosthenes(1)
    []
    >>> prime_sieve_eratosthenes(-1)
    Traceback (most recent call last):
    ...
    ValueError: Input must be a positive integer
    """

    if num <= 0:
        raise ValueError("Input must be a positive integer")

    primes = [True] * (num + 1)

    p = 2
    while p * p <= num:
        if primes[p]:
            for i in range(p * p, num + 1, p):
                primes[i] = False
        p += 1

    return [prime for prime in range(2, num + 1) if primes[prime]]


def np_prime_sieve_eratosthenes(max_number: int) -> list[int]:
    """
    Returns prime numbers below max_number.
    See: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    >>> np_prime_sieve_eratosthenes(10)
    [2, 3, 5, 7]
    >>> np_prime_sieve_eratosthenes(2)
    []
    """
    if max_number <= 2:
        return []

    # List containing a bool value for every odd number below max_number/2
    is_prime = np.ones(max_number // 2, dtype=bool)

    for i in range(3, isqrt(max_number - 1) + 1, 2):
        if is_prime[i // 2]:
            # Mark all multiple of i as not prime using list slicing
            is_prime[i**2 // 2 :: i] = False

    primes = np.where(is_prime)[0] * 2 + 1
    primes[0] = 2
    return primes.tolist()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    user_num = int(input("Enter a positive integer: ").strip())
    print(np_prime_sieve_eratosthenes(user_num))
