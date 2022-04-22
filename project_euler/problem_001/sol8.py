"""
Project Euler Problem 1: https://projecteuler.net/problem=1

Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_divisible_by(divisor: int, limit: int) -> int:
    p = (limit - 1) // divisor

    return divisor * (p * (p + 1) // 2)


def solution(n: int = 1000) -> int:
    """
    Returns the sum of all the multiples of 3 or 5 below n.

    >>> solution(3)
    0
    >>> solution(4)
    3
    >>> solution(10)
    23
    >>> solution(600)
    83700
    >>> solution(1000000000)
    233333333166666668
    """

    return sum_divisible_by(3, n) + sum_divisible_by(5, n) - sum_divisible_by(15, n)


if __name__ == "__main__":
    print(f"{solution() = }")
