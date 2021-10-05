"""
Author: Nikola Grujic
Date: October 5, 2021

Problem:
Given matrix dimensions, count number of different paths
from the top-left corner to the bottom-right corner by only
moving right or down.
"""

def count_paths(rows: int, cols: int) -> int:
    """
    >>> count_paths(3, 7)
    28

    >>> count_paths(3, 3)
    6
    """

    # initializing the DP matrix with 1s
    dp = [cols * [1]] * rows

    # updating number of paths
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()