#############################
# Author: Hosein Rajabi
# File: longest_palindromic_substring.py
# comments: This function finds the longest palindromic substring( not subsequence)
#           using bottom-up dynamic programming approach
# link: https://leetcode.com/problems/longest-palindromic-substring/description/
#############################
from __future__ import annotations


def longest_palindromic_substring(s: str) -> str:
    """
    >>> longest_palindromic_substring("a")
    'a'
    >>> longest_palindromic_substring("aa")
    'aa'
    >>> longest_palindromic_substring("abba")
    'abba'
    >>> longest_palindromic_substring("aaaccaa")
    'aaccaa'
    """
    length = len(s)

    # table dp represents longest palindrom starting from i to j
    dp = [[False for _ in range(length)] for _ in range(length)]

    # the main diagonal of the dp table is all True. Each character is a palindromic.
    for i in range(length):
        dp[i][i] = True

    max_length = 1

    # to keep track of the longest palindromic start position
    start = 0
    for i in range(length - 1, -1, -1):
        for j in range(i + 1, length):
            if s[i] == s[j]:
                if j - i == 1 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if j - i + 1 > max_length:
                        start = i
                        max_length = j - i + 1
    return s[start : start + max_length]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
