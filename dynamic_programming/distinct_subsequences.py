"""
author: Aayush Soni
Given two strings s and t, return the number of distinct subsequences
of s which equals t.
Input: s = "babgbag", t = "bag"
Output: 5
Leetcode link: https://leetcode.com/problems/distinct-subsequences/description/
"""


def count_distinct_subsequences(input_str: str, target_str: str) -> int:
    """
    Calculate the number of distinct subsequences of `input_str`
    that equal `target_str`.

    :param input_str: The input string `input_str`.
    :param target_str: The target string `target_str`.
    :return: The number of distinct subsequences of `input_str`
    that equal `target_str`.

    This function uses dynamic programming to solve the problem.

    Time complexity: O(m * n),
    Space complexity: O(m * n).
    where `m` is the length of `target_str`, and `n` is the length of
    `input_str`.

    >>> count_distinct_subsequences("babgbag", "bag")
    5
    >>> count_distinct_subsequences("rabbbit", "rabbit")
    3
    """

    target_len = len(target_str)  # Length of target string `target_str`
    input_len = len(input_str)  # Length of input string `input_str`

    if target_len > input_len:
        return 0

    # Create a matrix to store counts of subsequences.
    # dp[i][j] stores the count of occurrences of `target_str[1..i]` in
    # `input_str[1..j]`.
    dp = [[0 for _ in range(input_len + 1)] for __ in range(target_len + 1)]

    # Initialize the matrix.
    for i in range(target_len + 1):
        dp[i][0] = 0
    for j in range(input_len + 1):
        dp[0][j] = 1

    # Fill `dp` using dynamic programming
    for i in range(1, target_len + 1):
        for j in range(1, input_len + 1):
            if target_str[i - 1] != input_str[j - 1]:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

    return dp[target_len][input_len]


if __name__ == "__main__":
    input_str = "babgbag"
    target_str = "bag"
    result = count_distinct_subsequences(input_str, target_str)
    print(f"{result}")
