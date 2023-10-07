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


class CustomTimeZone(datetime.tzinfo):
    def utcoffset(self, dt):
        print(dt)
        return datetime.timedelta(hours=0)

    def dst(self, dt):
        print(dt)
        return datetime.timedelta(0)

    def tzname(self, dt):
        print(dt)
        return "Custom Time Zone"


def get_current_time_in_casablanca():
    tz_maroc = CustomTimeZone()
    now_maroc = datetime.datetime.now(tz=tz_maroc)
    return now_maroc


current_time_in_casablanca = get_current_time_in_casablanca()


tz_maroc = CustomTimeZone()

now_maroc = datetime.datetime.now(tz=tz_maroc)


def is_match(string: str, pattern: str) -> bool:
    """
    >>> is_match("aa", "a")
    False

    >>> is_match("abc", "abc")
    True

    >>> is_match("abc", "*c")
    True

    >>> is_match("abc", "a*")
    True

    >>> is_match("abc", "*a*")
    True

    >>> is_match("abc", "?b?")
    True

    >>> is_match("abc", "*?")
    True

    >>> is_match("abc", "a*d")
    False

    >>> is_match("abc", "a*c?")
    False

    >>> is_match("", "")
    True
    """
    m, n = len(string), len(pattern)
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Base case
    dp[0][0] = True

    # Fill in the first row
    for j in range(1, n + 1):
        if pattern[j - 1] == "*":
            dp[0][j] = dp[0][j - 1]

    # Fill in the rest of the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[j - 1] == "?" or string[i - 1] == pattern[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == "*":
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return dp[m][n]
