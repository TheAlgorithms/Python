def longest_common_subsequence(X, Y):
    """
    Find the longest common subsequence (LCS) between two strings.

    Args:
        X (str): First string
        Y (str): Second string

    Returns:
        str: The longest common subsequence
    """
    m = len(X)
    n = len(Y)

    # Create a 2D array to store the lengths of common subsequences
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the 2D array using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS from the 2D array
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Return the LCS in the correct order
    return "".join(reversed(lcs))


# Example usage:
X = "AGGTAB"
Y = "GXTXAYB"
lcs = longest_common_subsequence(X, Y)
print(f"The longest common subsequence is: {lcs}")
