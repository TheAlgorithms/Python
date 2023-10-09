"""
There is a robot on an m x n grid.
The robot is initially located at the top-left corner of grid
the robot tries to move to the bottom-right corner.
The robot can only move either down or right at any point in time.
Return number of all  possible unique paths robot can take.
"""


def uniquepaths(m, n):
    """
    >>> uniquepaths(3,2)
    3
    >>> uniquepaths(3,7)
    28
    """
    dp = [[0] * n for _ in range(m)]
    # number of ways to reach any cell in the first row or first column is 1.
    for i in range(m):
        dp[i][0] = 1

    for i in range(n):
        dp[0][i] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
