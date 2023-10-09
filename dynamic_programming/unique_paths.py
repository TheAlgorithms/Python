#Calculate number of unique paths from starting to ending cell in a grid.
def uniquePaths(m, n):
    """
    Calculate the number of unique paths in an m x n grid.

    Args:
        m (int): Number of rows in the grid.
        n (int): Number of columns in the grid.

    Returns:
        int: The number of unique paths from the top-left corner to the bottom-right corner.

    Examples:
        >>> uniquePaths(3, 7)
        28
        >>> uniquePaths(3, 2)
        3
    """
    dp = [[0] * n for _ in range(m)]

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

