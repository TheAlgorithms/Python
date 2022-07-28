"""
Project Euler Problem 10: https://projecteuler.net/problem=10

Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

References:
    - https://en.wikipedia.org/wiki/Prime_number
"""
import math
from collections.abc import Iterator
from itertools import takewhile


def is_prime(number: int) -> bool:
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

    if number % 2 == 0 and number > 2:
        return False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2))


def prime_generator() -> Iterator[int]:
    """
    Generate a list sequence of prime numbers
    """

    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


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

    return sum(takewhile(lambda x: x < n, prime_generator()))


if __name__ == "__main__":
    print(f"{solution() = }")
