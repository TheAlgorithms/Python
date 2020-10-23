"""
Problem 28
Url: https://projecteuler.net/problem=28
Statement:
Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?
"""

from math import ceil


def solution(n: int = 1001) -> int:
    """Returns the sum of the numbers on the diagonals in a n by n spiral
    formed in the same way.

    >>> solution(1001)
    669171001
    >>> solution(500)
    82959497
    >>> solution(100)
    651897
    >>> solution(50)
    79697
    >>> solution(10)
    537
    """
    total = 1

    for i in range(1, int(ceil(n / 2.0))):
        odd = 2 * i + 1
        even = 2 * i
        total = total + 4 * odd ** 2 - 6 * even

    return total


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print(solution())
    else:
        try:
            n = int(sys.argv[1])
            print(solution(n))
        except ValueError:
            print("Invalid entry - please enter a number")
