"""
Problem 81: https://projecteuler.net/problem=81
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
by only moving to the right and down, is indicated in bold red and is equal to 2427.

    [131]   673   234    103    18
    [201]  [96]  [342]   965   150
     630   803   [746]  [422]  111
     537   699   497    [121]  956
     805   732   524    [37]  [331]

Find the minimal path sum from the top left to the bottom right by only moving right
and down in matrix.txt (https://projecteuler.net/project/resources/p081_matrix.txt),
a 31K text file containing an 80 by 80 matrix.
"""

import os


def solution(filename: str = "matrix.txt") -> int:
    """
    Returns the minimal path sum from the top left to the bottom right of the matrix.
    >>> solution()
    427337
    """
    with open(os.path.join(os.path.dirname(__file__), filename)) as in_file:
        data = in_file.read()

    grid = [[int(cell) for cell in row.split(",")] for row in data.strip().splitlines()]
    dp = [[0 for cell in row] for row in grid]
    n = len(grid[0])

    dp = [[0 for i in range(n)] for j in range(n)]
    dp[0][0] = grid[0][0]
    for i in range(1, n):
        dp[0][i] = grid[0][i] + dp[0][i - 1]
    for i in range(1, n):
        dp[i][0] = grid[i][0] + dp[i - 1][0]

    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


if __name__ == "__main__":
    print(f"{solution() = }")
