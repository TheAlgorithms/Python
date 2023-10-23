"""
author: Aayush Soni
Given two strings s and t, return the number of distinct subsequences of s which equals t.
Input: s = "babgbag", t = "bag"
Output: 5
Explanation: As shown below, there are 5 ways you can generate "bag" from s.
>>> "babgbag"
>>> "babgbag"
>>> "babgbag"
>>> "babgbag"
>>> "babgbag"
Leetcode link: https://leetcode.com/problems/distinct-subsequences/description/
"""


def countDistinctSubsequences(s: str, t: str) -> int:
    """
    This function calculates the number of distinct subsequences of s that equal t.

    :param s: The input string s.
    :param t: The target string t.
    :return: The number of distinct subsequences of s that equal t.

    >>> countDistinctSubsequences("babgbag", "bag")
    5
    >>> countDistinctSubsequences("rabbbit", "rabbit")
    3
    """

    m = len(t)  # Length of t
    n = len(s)  # Length of s

    # If t is longer than s, it can't be a subsequence.
    if m > n:
        return 0

    # Create a matrix to store counts of subsequences.
    # dp[i][j] stores the count of occurrences of t(1..i) in s(1..j).
    dp = [[0 for _ in range(n + 1)] for __ in range(m + 1)]

    # Initialize the first column with all 0s.
    # An empty string can't have another string as a subsequence.
    for i in range(1, m + 1):
        dp[i][0] = 0

    # Initialize the first row with all 1s.
    # An empty string is a subsequence of all strings.
    for j in range(n + 1):
        dp[0][j] = 1

    # Fill dp[][] in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If the last characters don't match,
            # the value is the same as the value without the last character in s.
            if t[i - 1] != s[j - 1]:
                dp[i][j] = dp[i][j - 1]

            # If the last characters match,
            # the value is obtained by considering two cases:
            # a) All subsequences without the last character in s.
            # b) All subsequences without the last characters in both s and t.
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

    return dp[m][n]


if __name__ == "__main__":
    s = "babgbag"
    t = "bag"
    result = countDistinctSubsequences(s, t)
    print(f"The number of distinct subsequences of '{t}' in '{s}' is {result}.")
