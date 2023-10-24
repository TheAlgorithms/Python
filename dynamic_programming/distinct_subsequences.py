"""
author: Aayush Soni
Given two strings s and t, return the number of distinct subsequences
of s which equals t.
Input: s = "babgbag", t = "bag"
Output: 5
Leetcode link: https://leetcode.com/problems/distinct-subsequences/description/
"""


def count_distinct_subsequences(s: str, t: str) -> int:
    """
    Calculate the number of distinct subsequences of `s` that equal `t`.

    :param s: The input string `s`.
    :param t: The target string `t`.
    :return: The number of distinct subsequences of `s` that equal `t`.

    This function uses dynamic programming to solve the problem.

    Time complexity: O(m * n).
    Space complexity: O(m * n).
    where `m` is the length of `t`, and `n` is the length of `s`.

    >>> count_distinct_subsequences("babgbag", "bag")
    5
    >>> count_distinct_subsequences("rabbbit", "rabbit")
    3
    """

    t_len = len(t)  # Length of target string `t`
    s_len = len(s)  # Length of input string `s`

    if t_len > s_len:
        return 0

    # Create a matrix to store counts of subsequences.
    # dp[i][j] stores the count of occurrences of `t[1..i]` in `s[1..j]`.
    dp = [[0 for _ in range(s_len + 1)] for __ in range(t_len + 1)]

    # Initialize the matrix.
    for i in range(t_len + 1):
        dp[i][0] = 0
    for j in range(s_len + 1):
        dp[0][j] = 1

    # Fill `dp` using dynamic programming
    for i in range(1, t_len + 1):
        for j in range(1, s_len + 1):
            if t[i - 1] != s[j - 1]:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

    return dp[t_len][s_len]


if __name__ == "__main__":
    input_str = "babgbag"
    target_str = "bag"
    result = count_distinct_subsequences(input_str, target_str)
    print(f"{result}")
