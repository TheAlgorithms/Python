"""
Project Euler Problem 87
https://projecteuler.net/problem=87

The smallest number expressible as the sum of a prime square, prime cube, and prime
fourth power is 28. In fact, there are exactly four numbers below fifty that can be
expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime square,
prime cube, and prime fourth power?
"""

from typing import List


def calculate_primes(end: int) -> List[int]:
    """
    Generates a list of all prime numbers up to a given number.
    e.g.
    >>> calculate_primes(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """

    candidates = set(range(2, end + 1))
    for n in range(2, end // 2 + 1):
        for multiplier in range(2, end // 2 + 1):
            value = n * multiplier
            if value > end:
                break
            candidates.discard(value)
    return sorted(candidates)


def calculate_powers(nums: List[int], power: int) -> List[int]:
    """
    Returns a list of integers each increased by a given power.
    e.g.
    >>> calculate_powers([1, 2, 3], 3)
    [1, 8, 27]
    """

    results = []
    for n in nums:
        results.append(n ** power)
    return results


def solution(max_number: int = 50_000_000) -> int:
    """
    Calculates and returns the answer to project euler problem 87.

    Assumptions:
    1. Since we're limited to 50,000,000, we can determine ceilings for the primes:
         - Squareroot of 50M rounded down is 7071

    Answer:
    >>> solution(50)
    4
    """

    prime_power_triples = set()
    max_prime = 7071

    primes = calculate_primes(max_prime)
    squares = calculate_powers(primes, 2)
    cubes = calculate_powers(primes, 3)
    quads = calculate_powers(primes, 4)

    doubles = set()
    for q in quads:
        for c in cubes:
            doubles.add(q + c)
    for d in doubles:
        for s in squares:
            sum = d + s
            if sum >= max_number:
                break
            prime_power_triples.add(sum)

    return len(prime_power_triples)


if __name__ == "__main__":

    print(solution())
