"""
Project Euler Problem 1: https://projecteuler.net/problem=1

Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from functools import reduce


def solution(n: int = 1000) -> int:
    """
    Returns the sum of all multiples of 3 or 5 bellow n

    >>> solution(3)
    0
    >>> solution(4)
    3
    >>> solution(10)
    23
    >>> solution(600)
    83700
    >>> solution(-7)
    0
    """

    multiples = [num for num in range(0, n) if num % 3 == 0 or num % 5 == 0]
    return reduce(lambda x, y: x + y, multiples) if multiples else 0


if __name__ == "__main__":
    print(f"{solution() = }")
