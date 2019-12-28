# -*- coding: utf-8 -*-
"""
Problem:

The sum of the squares of the first ten natural numbers is,
            1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
            (1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first N natural
numbers and the square of the sum.
"""


def solution(n):
    """Returns the difference between the sum of the squares of the first n
    natural numbers and the square of the sum.

    >>> solution(10)
    2640
    >>> solution(15)
    13160
    >>> solution(20)
    41230
    >>> solution(50)
    1582700
    >>> solution(100)
    25164150
    """
    sum_of_squares = n * (n + 1) * (2 * n + 1) / 6
    square_of_sum = (n * (n + 1) / 2) ** 2
    return int(square_of_sum - sum_of_squares)


if __name__ == "__main__":
    print(solution(int(input("Enter a number: ").strip())))
