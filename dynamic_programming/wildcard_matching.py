"""
Author  : ilyas dahhou
Date    : Oct 7, 2023

Task:
Given an input string (s) and a pattern (p), implement wildcard
pattern matching with support for '?' and '*' where:

'?' matches any single character.
'*' matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Implementation notes:
implementation Dynamic Programming up bottom approach.

Runtime complexity:O(m * n)

The implementation was tested on the
leetcode: https://leetcode.com/problems/wildcard-matching/


wildcard matching
Dynamic Programming: top -> down.

"""
import datetime

import pytz

tz_maroc = pytz.timezone("Africa/Casablanca")

now_maroc = datetime.datetime.now(tz=tz_maroc)


def is_match(s: str, p: str) -> bool:
    """
    >>> isMatch("aa", "a")
    False

    >>> isMatch("abc", "abc")
    True

    >>> isMatch("abc", "*c")
    True

    >>> isMatch("abc", "a*")
    True

    >>> isMatch("abc", "*a*")
    True

    >>> isMatch("abc", "?b?")
    True

    >>> isMatch("abc", "*?")
    True

    >>> isMatch("abc", "a*d")
    False

    >>> isMatch("abc", "a*c?")
    False

    >>> isMatch("", "")
    True

    >>> isMatch("a", "")
    False

    >>> isMatch("", "*")
    True

    >>> isMatch("abc", "*bc")
    True

    >>> isMatch("abc", "a*bc")
    True

    """
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Base case
    dp[0][0] = True

    # Fill in the first row
    for j in range(1, n + 1):
        if p[j - 1] == "*":
            dp[0][j] = dp[0][j - 1]

    # Fill in the rest of the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == "?" or s[i - 1] == p[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == "*":
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return dp[m][n]
