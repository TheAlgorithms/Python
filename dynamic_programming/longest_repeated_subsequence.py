"""
Given a string, print the longest repeating subsequence such that the two
subsequence don’t have same string character at same position, i.e., any
i’th character in the two subsequences shouldn’t have the same index in
the original string.

Input: s = "aabb"
Output: "ab"

Input: s = "aab"
Output: "a"

The two subsequence are 'a'(first) and 'a' (second). Note that 'b' cannot be
considered as part of subsequence as it would be at sameindex in both.

This problem is just the modification of Longest Common Subsequence problem.
The idea is to find the LCS(s, s) where s is the input string with the
restriction that when both the characters are same, they shouldn’t be on the
same index in the two strings.
"""


def longest_repeating_subsequence(s: str) -> str:
    """
    Time complexity: O(n^2)

    >>> longest_repeating_subsequence("aabb")
    'ab'
    >>> longest_repeating_subsequence("aab")
    'a'
    """
    n = len(s)
    # Create and initialize DP table
    dp = [[0 for k in range(n+1)] for l in range(n+1)]
    # Fill dp table (similar to LCS loops)
    for i in range(1, n+1):
        for j in range(1, n+1):
            # If characters match and indices are not same
            if s[i-1] == s[j-1] and i != j:
                dp[i][j] = 1 + dp[i-1][j-1]
            # If characters do not match
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[n][n]
