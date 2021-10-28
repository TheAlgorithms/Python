"""
Project Euler Problem 10: https://projecteuler.net/problem=10

Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

References:
    - https://en.wikipedia.org/wiki/Prime_number
"""

from maths.prime_check import prime_check


def solution(n: int = 2000000) -> int:
    """
    Returns the sum of all the primes below n.

    >>> solution(1000)
    76127
    >>> solution(5000)
    1548136
    >>> solution(10000)
    5736396
    >>> solution(7)
    10
    """

    if n > 2:
        sum_of_primes = 2
    else:
        return 0

    for i in range(3, n, 2):
        if prime_check(i):
            sum_of_primes += i

    return sum_of_primes


if __name__ == "__main__":
    print(f"{solution() = }")
