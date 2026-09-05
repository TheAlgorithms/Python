"""
Author  : ilyas dahhou
Date    : Oct 7, 2023

Task:
Given an input string and a pattern, implement wildcard pattern matching with support
for '?' and '*' where:
'?' matches any single character.
'*' matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Runtime complexity: O(m * n)

The implementation was tested on the
leetcode: https://leetcode.com/problems/wildcard-matching/
"""


def is_match(string: str, pattern: str) -> bool:
    """
    >>> is_match("", "")
    True
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
    >>> is_match('baaabab','*****ba*****ba')
    False
    >>> is_match('baaabab','*****ba*****ab')
    True
    >>> is_match('aa','*')
    True
    """
    dp = [[False] * (len(pattern) + 1) for _ in string + "1"]
    dp[0][0] = True
    # Fill in the first row
    for j, char in enumerate(pattern, 1):
        if char == "*":
            dp[0][j] = dp[0][j - 1]
    # Fill in the rest of the DP table
    for i, s_char in enumerate(string, 1):
        for j, p_char in enumerate(pattern, 1):
            if p_char in (s_char, "?"):
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == "*":
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    return dp[len(string)][len(pattern)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{is_match('baaabab','*****ba*****ab') = }")
