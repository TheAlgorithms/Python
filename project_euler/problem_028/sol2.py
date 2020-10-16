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


def solution(dimension: int = 1001) -> int:
    """
    Returns the sum of the numbers on the diagonals in a
    dimension X dimension spiral grid as described in problem statement.

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
    answer = 1
    num_spiral = 1
    number_in_spiral = 3
    x = 3  # point_pour_au_spiral_suivante
    while number_in_spiral <= dimension:
        answer = answer + 4 * x + 6 * 2 * num_spiral
        x = x + 3 * 2 * num_spiral + 2 * (num_spiral + 1)
        num_spiral += 1
        number_in_spiral = 2 * num_spiral + 1
    return answer


if __name__ == "__main__":
    print(f"{solution() = }")
