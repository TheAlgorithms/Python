"""
Project Euler Problem 6: https://projecteuler.net/problem=6

Sum square difference

The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""


def solution(n: int = 100) -> int:
    """
    Returns the difference between the sum of the squares of the first n
    natural numbers and the square of the sum.

    >>> solution(10)
    2640
    >>> solution(15)
    13160
    >>> solution(20)
    41230
    >>> solution(50)
    1582700
    """

    sum_of_squares = 0
    sum_of_ints = 0
    for i in range(1, n + 1):
        sum_of_squares += i**2
        sum_of_ints += i
    return sum_of_ints**2 - sum_of_squares


if __name__ == "__main__":
    print(f"{solution() = }")
