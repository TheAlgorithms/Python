"""
LPS Problem Statement: Find the length of the longest palindromic subsequence
in a given string. A palindromic subsequence is a sequence that reads the same
forward and backward, but not necessarily continuous.

Example: For the input "babad," the longest palindromic subsequence
can be "bab" or "aba."
"""


def longest_palindromic_subsequence(s: str) -> tuple[int, str]:
    """
    Finds the length and the longest palindromic subsequence in a given string.

    Parameters:
        s (str): The input string.

    Returns:
        Tuple[int, str]: A tuple containing the length of the longest
        palindromic subsequence and the subsequence itself.

    Raises:
        ValueError: If the input string is empty or None.

    Example:
        >>> longest_palindromic_subsequence("bbbab")
        (4, 'bbbb')
        >>> longest_palindromic_subsequence("babad")
        (3, 'bab')
        >>> longest_palindromic_subsequence("cbbd")
        (2, 'bb')
    """
    if s is None or len(s) == 0:
        raise ValueError("Input string cannot be empty or None")

    n = len(s)
    # Create a table to store results of subproblems
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # Reconstruct the Longest Palindromic Subsequence
    i, j = 0, n - 1
    lps = []
    while i < n and j >= 0:
        if s[i] == s[j]:
            lps.append(s[i])
            i += 1
            j -= 1
        elif i < j and dp[i][j - 1] >= dp[i + 1][j]:
            j -= 1
        else:
            i += 1

    return dp[0][n - 1], "".join(lps)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
