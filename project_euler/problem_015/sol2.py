"""
Problem 15: https://projecteuler.net/problem=15

Starting in the top left corner of a 2x2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20x20 grid?
"""

from numpy import integer, ones


def solution(n: int = 20) -> int:
    """
    Solve by explicitly counting the paths with dynamic programming.

    >>> solution(6)
    924
    >>> solution(2)
    6
    >>> solution(1)
    2
    """

    counts = ones((n + 1, n + 1), dtype=integer)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            counts[i][j] = counts[i - 1][j] + counts[i][j - 1]

    return int(counts[n][n])


if __name__ == "__main__":
    print(solution())
