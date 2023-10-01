"""
author: Sanket Kittad
Given a string s, find the longest palindromic subsequence's length in s.
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
"""


def longest_palindromic_subsequence(s: str) -> int:
    """
    This function returns the longest palindromic subsequence in a string
    >>> longest_palindromic_subsequence("bbbab")
    4
    >>> longest_palindromic_subsequence("bbabcbcab")
    7
    """
    n = len(s)
    rev = s[::-1]
    m = len(rev)
    dp = [[-1] * (m + 1) for i in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(m + 1):
        dp[0][i] = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If characters at i and j are the same
            # include them in the palindromic subsequence
            if s[i - 1] == rev[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
