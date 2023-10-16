"""
Project Euler Problem 70: https://projecteuler.net/problem=70

Euler's Totient function, φ(n) [sometimes called the phi function], is used to
determine the number of positive numbers less than or equal to n which are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than
nine and relatively prime to nine, φ(9)=6.

The number 1 is considered to be relatively prime to every positive number, so
φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation
of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and
the ratio n/φ(n) produces a minimum.

-----

This is essentially brute force. Calculate all totients up to 10^7 and
find the minimum ratio of n/φ(n) that way. To minimize the ratio, we want
to minimize n and maximize φ(n) as much as possible, so we can store the
minimum fraction's numerator and denominator and calculate new fractions
with each totient to compare against. To avoid dividing by zero, I opt to
use cross multiplication.

References:
Finding totients
https://en.wikipedia.org/wiki/Euler%27s_totient_function#Euler%27s_product_formula
"""
from __future__ import annotations

from math import isqrt

import numpy as np


def calculate_prime_numbers(max_number: int) -> list[int]:
    """
    Returns prime numbers below max_number.
    See: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    >>> calculate_prime_numbers(10)
    [2, 3, 5, 7]
    >>> calculate_prime_numbers(2)
    []
    """
    if max_number <= 2:
        return []

    # List containing a bool value for every odd number below max_number/2
    is_prime = [True] * (max_number // 2)

    for i in range(3, isqrt(max_number - 1) + 1, 2):
        if is_prime[i // 2]:
            # Mark all multiple of i as not prime using list slicing
            is_prime[i**2 // 2 :: i] = [False] * (
                # Same as: (max_number - (i**2)) // (2 * i) + 1
                # but faster than len(is_prime[i**2 // 2 :: i])
                len(range(i**2 // 2, max_number // 2, i))
            )

    return [2] + [2 * i + 1 for i in range(1, max_number // 2) if is_prime[i]]


def np_calculate_prime_numbers(max_number: int) -> list[int]:
    """
    Returns prime numbers below max_number.
    See: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    >>> np_calculate_prime_numbers(10)
    [2, 3, 5, 7]
    >>> np_calculate_prime_numbers(2)
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


def slow_get_totients(max_one: int) -> list[int]:
    """
    Calculates a list of totients from 0 to max_one exclusive, using the
    definition of Euler's product formula.

    >>> slow_get_totients(5)
    [0, 1, 1, 2, 2]

    >>> slow_get_totients(10)
    [0, 1, 1, 2, 2, 4, 2, 6, 4, 6]
    """
    totients = np.arange(max_one)

    for i in range(2, max_one):
        if totients[i] == i:
            x = np.arange(i, max_one, i)  # array of indexes to select
            totients[x] -= totients[x] // i

    return totients.tolist()


def slicing_get_totients(max_one: int) -> list[int]:
    """
    Calculates a list of totients from 0 to max_one exclusive, using the
    definition of Euler's product formula.

    >>> slicing_get_totients(5)
    [0, 1, 1, 2, 2]

    >>> slicing_get_totients(10)
    [0, 1, 1, 2, 2, 4, 2, 6, 4, 6]
    """
    totients = np.arange(max_one)

    for i in range(2, max_one):
        if totients[i] == i:
            totients[i::i] -= totients[i::i] // i

    return totients.tolist()


def get_totients(limit) -> list[int]:
    """
    Calculates a list of totients from 0 to max_one exclusive, using the
    definition of Euler's product formula.

    >>> get_totients(5)
    [0, 1, 1, 2, 2]

    >>> get_totients(10)
    [0, 1, 1, 2, 2, 4, 2, 6, 4, 6]
    """
    totients = np.arange(limit)
    primes = calculate_prime_numbers(limit)

    for i in primes:
        totients[i::i] -= totients[i::i] // i

    return totients.tolist()


def np_get_totients(limit) -> list[int]:
    """
    Calculates a list of totients from 0 to max_one exclusive, using the
    definition of Euler's product formula.

    >>> np_get_totients(5)
    [0, 1, 1, 2, 2]

    >>> np_get_totients(10)
    [0, 1, 1, 2, 2, 4, 2, 6, 4, 6]
    """
    totients = np.arange(limit)
    primes = np_calculate_prime_numbers(limit)

    for i in primes:
        totients[i::i] -= totients[i::i] // i

    return totients.tolist()


def has_same_digits(num1: int, num2: int) -> bool:
    """
    Return True if num1 and num2 have the same frequency of every digit, False
    otherwise.

    >>> has_same_digits(123456789, 987654321)
    True

    >>> has_same_digits(123, 23)
    False

    >>> has_same_digits(1234566, 123456)
    False
    """
    return sorted(str(num1)) == sorted(str(num2))


def slow_solution(max_n: int = 10000000) -> int:
    """
    Finds the value of n from 1 to max such that n/φ(n) produces a minimum.

    >>> slow_solution(100)
    21

    >>> slow_solution(10000)
    4435
    """
    totients = slow_get_totients(max_n + 1)

    return common_solution(totients, max_n)


def slicing_solution(max_n: int = 10000000) -> int:
    """
    Finds the value of n from 1 to max such that n/φ(n) produces a minimum.

    >>> slicing_solution(100)
    21

    >>> slicing_solution(10000)
    4435
    """
    totients = slicing_get_totients(max_n + 1)

    return common_solution(totients, max_n)


def py_solution(max_n: int = 10000000) -> int:
    """
    Finds the value of n from 1 to max such that n/φ(n) produces a minimum.

    >>> py_solution(100)
    21

    >>> py_solution(10000)
    4435
    """
    totients = get_totients(max_n + 1)

    return common_solution(totients, max_n)


def solution(max_n: int = 10000000) -> int:
    """
    Finds the value of n from 1 to max such that n/φ(n) produces a minimum.

    >>> solution(100)
    21

    >>> solution(10000)
    4435
    """
    totients = np_get_totients(max_n + 1)

    return common_solution(totients, max_n)


def common_solution(totients: list[int], max_n: int = 10000000) -> int:
    """
    Finds the value of n from 1 to max such that n/φ(n) produces a minimum.

    >>> common_solution(get_totients(101), 100)
    21

    >>> common_solution(get_totients(10001), 10000)
    4435
    """
    min_numerator = 1  # i
    min_denominator = 0  # φ(i)

    for i in range(2, max_n + 1):
        t = totients[i]

        if i * min_denominator < min_numerator * t and has_same_digits(i, t):
            min_numerator = i
            min_denominator = t

    return min_numerator


def benchmark() -> None:
    """
    Benchmark
    """
    # Running performance benchmarks...
    # Solution    : 56.19136740000067
    # Slicing Sol : 70.83823779999875
    # Slow Sol    : 118.29514729999937

    from timeit import timeit

    print("Running performance benchmarks...")

    print(f"Solution    : {timeit('solution()', globals=globals(), number=10)}")
    print(f"Slicing Sol : {timeit('slicing_solution()', globals=globals(), number=10)}")
    print(f"Slow Sol    : {timeit('slow_solution()', globals=globals(), number=10)}")


if __name__ == "__main__":
    print(f"Solution    : {solution()}")
    print(f"Slicing Sol : {slicing_solution()}")
    print(f"Slow Sol    : {slow_solution()}")
    benchmark()
