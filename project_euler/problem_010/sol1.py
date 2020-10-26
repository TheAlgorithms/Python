"""
Project Euler Problem 10: https://projecteuler.net/problem=10

Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

References:
    - https://en.wikipedia.org/wiki/Prime_number
"""

from math import sqrt


def is_prime(n: int) -> bool:
    """
    Returns boolean representing primality of given number num.

    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(27)
    False
    >>> is_prime(2999)
    True
    """

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


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
        if is_prime(i):
            sum_of_primes += i

    return sum_of_primes


if __name__ == "__main__":
    print(f"{solution() = }")
