"""
Problem 82: https://projecteuler.net/problem=82
The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the
left column and finishing in any cell in the right column, and only moving up,
down, and right, is indicated in red and bold; the sum is equal to 994.

    131    673   [234]  [103]  [18]
    [201]  [96]  [342]  965    150
    630    803   746    422    111
    537    699   497    121    956
    805    732   524    37     331

Find the minimal path sum from the left column to the right column in
https://projecteuler.net/project/resources/p082_matrix.txt, a 31K text file
containing an 80 by 80 matrix.
"""
import os


def solution(filename: str = "matrix.txt") -> int:
    """
    Returns the minimal path sum from the left column to the right column of
    the matrix.
    >>> solution()
    260324
    """
    with open(os.path.join(os.path.dirname(__file__), filename)) as in_file:
        data = in_file.read()

    grid = [[int(c) for c in r.split(",")] for r in data.strip().splitlines()]
    N = len(grid)
    dp = [grid[i][-1] for i in range(N)]

    for i in range(N - 2, -1, -1):
        dp[0] += grid[0][i]

        for j in range(1, N):
            dp[j] = min(grid[j][i] + dp[j], grid[j][i] + dp[j - 1])

        for j in range(N - 2, -1, -1):
            dp[j] = min(dp[j], grid[j][i] + dp[j + 1])

    return min(dp)


if __name__ == "__main__":
    print(f"{solution()}")
