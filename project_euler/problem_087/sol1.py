"""
Project Euler Problem 87: https://projecteuler.net/problem=87

-----------------------------------------------------------------------------

PROBLEM STATEMENT

The smallest number expressible as the sum of a prime square, prime cube,
and prime fourth power is 28. In fact, there are exactly four numbers below
fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime
square, prime cube, and prime fourth power?

-----------------------------------------------------------------------------

SOLUTION

Using the Sieve of Eratosthenes, we can generated all the prime numbers
that can be used.

Then iterate through all possible triplets and count the
ones that satisfy the problem requirements

We can avoid unnecessary computation by breaking early when
the partial sum surpasses the given threshold. We can do that
because the sieve algorithm returns the prime numbers in
ascending order

"""

import math


def sieve(limit: int = 10000):
    """
    return a list with all the prime numbers not greater than limit
    using the Sieve of Eratosthenes

    >>> sieve(3)
    [2, 3]
    >>> sieve(1)
    []
    >>> sieve(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """

    if limit < 2:
        # there are no primes lower than 2
        return []

    primes = [2]

    # mark with True multiples of prime numbers
    # that were sieved
    # we can initialize it the following way, since
    # we know 2 is prime and all even numbers are multiples of 2
    checked = [not (i & 1) for i in range(limit + 1)]

    for number in range(3, limit + 1, 2):
        # since we're ignoring even numbers we can use a step of 2
        if checked[number]:
            continue

        primes.append(number)
        for mark in range(number ** 2, limit + 1, number):
            # iterate through non marked multiples of number and mark them
            checked[mark] = True

    return primes


def solution(max_sum: int = 50_000_000) -> int:
    """
    Use the sieve algorithm to compute prime numbers,
    then iterate through triplets and find the answer

    >>> solution(50)
    4
    >>> solution()
    1097343
    """

    # we can find a reference for the biggest prime if we think
    # that small numbers are used for the powers 3 and 4 and a big number
    # is squared.
    # thus, we can find the superior limit of the prime as being the
    # square root of the maximum sum

    prime_limit = int(math.sqrt(max_sum))
    primes = sieve(prime_limit)

    solutions = set()  # store solutions in set to avoid duplicates
    for first in primes:
        for second in primes:
            sum_sec = first ** 2 + second ** 3
            if sum_sec >= max_sum:
                # we can brake since the primes are in ascending order
                # and the sum will only increase
                break
            for third in primes:
                sum_fin = sum_sec + third ** 4
                if sum_fin > max_sum:
                    # same as above
                    break
                solutions.add(sum_fin)

    return len(solutions)


if __name__ == "__main__":
    print(solution())
