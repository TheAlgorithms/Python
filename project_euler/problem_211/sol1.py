"""
Problem 211: https://projecteuler.net/problem=211

Name: Divisor Square Sum


For a positive integer n, let σ2(n) be the sum of the squares of its divisors.
For example, σ2(10) = 1 + 4 + 25 + 100 = 130.

Find the sum of all n, 0 < n < 64,000,000 such that σ2(n) is a perfect square.

"""

import math


def gen_square_factors_sum(limit: int) -> list:
    """
    Returns the list of sum of the squares of factors.
    >>> gen_square_factors_sum(5)
    [0, 1, 5, 10, 21]
    >>> gen_square_factors_sum(10)
    [0, 1, 5, 10, 21, 26, 50, 50, 85, 91]
    >>> gen_square_factors_sum(15)
    [0, 1, 5, 10, 21, 26, 50, 50, 85, 91, 130, 122, 210, 170, 250]
    """
    square_factors_sum = [0, 1]
    square_factors_sum.extend([i * i + 1 for i in range(2, limit)])

    for i in range(2, (limit + 1) // 2):
        square_factor = i * i
        for j in range(i * 2, limit, i):
            square_factors_sum[j] += square_factor
    return square_factors_sum


def is_squares(n: int) -> bool:
    """
    Returns if the number is perfect square are not.
    >>> is_squares(25)
    True
    >>> is_squares(16)
    True
    >>> is_squares(40)
    False
    """
    root = math.sqrt(n)
    return int(root + 0.5) ** 2 == n


def solution(limit: int = 64_000_000) -> int:
    """
    Returns the sum of divisor squares till 64,000,000.
    >>> solution(10)
    1
    >>> solution(100)
    43
    >>> solution(1000)
    1304
    """
    square_factors_sum = gen_square_factors_sum(limit)

    res = 0
    for i in range(len(square_factors_sum)):
        if is_squares(square_factors_sum[i]):
            res += i
    return res


if __name__ == "__main__":
    print(solution())
