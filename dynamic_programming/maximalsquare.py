"""
Maximal square is an infamous coding question which is often seen in company interviews
It follows a dynamic programming algorithm and DP on Grids approach

Leetcode link for the problem: leetcode.com/problems/maximal-square/
"""


def maximal_square(matrix: list[list[str]]) -> int:
    """
    >>> maximal_square([
    ...    ["1", "0", "1", "0", "0"],
    ...    ["1", "0", "1", "1", "1"],
    ...    ["1", "1", "1", "1", "1"],
    ...    ["1", "0", "0", "1", "0"]
    ... ])
    4
    >>> maximal_square([
    ...    ["0", "1"],
    ...    ["1", "0"]
    ... ])
    1
    >>> maximal_square([
    ...    ["0"]
    ... ])
    0
    >>> maximal_square([])  # Empty matrix
    0
    >>> maximal_square([["1"]])  # Single-cell square
    1
    >>> maximal_square([["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]])
    0
    """
    if not matrix:
        return 0

    m = len(matrix)
    n = len(matrix[0])

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    maxval = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if matrix[i - 1][j - 1] == "1":
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                maxval = max(maxval, dp[i][j])

    return maxval * maxval


if __name__ == "__main__":
    import doctest

    doctest.testmod()
