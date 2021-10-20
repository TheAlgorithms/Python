"""
Implementation of regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

"""


def match_pattern(input_string: str, pattern: str) -> bool:
    """
    uses bottom-up dynamic programming solution for matching the input
    string with a given pattern.

    Runtime: O(len(input_string)*len(pattern))

    Arguments
    --------
    input_string: str, any string which should be compared with the pattern
    pattern: str, the string that represents a pattern and may contain
    '.' for single character matches and '*' for zero or more of preceding character
    matches

    Note
    ----
    the pattern cannot start with a '*',
    because there should be at least one character before *

    Returns
    -------
    A Boolean denoting whether the given string follows the pattern

    Examples
    -------
    >>> match_pattern("aab", "c*a*b")
    True
    >>> match_pattern("dabc", "*abc")
    False
    >>> match_pattern("aaa", "aa")
    False
    >>> match_pattern("aaa", "a.a")
    True
    >>> match_pattern("aaab", "aa*")
    False
    >>> match_pattern("aaab", ".*")
    True
    >>> match_pattern("a", "bbbb")
    False
    >>> match_pattern("", "bbbb")
    False
    >>> match_pattern("a", "")
    False
    >>> match_pattern("", "")
    True
    """

    len_string = len(input_string) + 1
    len_pattern = len(pattern) + 1

    # dp is a 2d matrix where dp[i][j] denotes whether prefix string of
    # length i of input_string matches with prefix string of length j of
    # given pattern.
    # "dp" stands for dynamic programming.
    dp = [[0 for i in range(len_pattern)] for j in range(len_string)]

    # since string of zero length match pattern of zero length
    dp[0][0] = 1

    # since pattern of zero length will never match with string of non-zero length
    for i in range(1, len_string):
        dp[i][0] = 0

    # since string of zero length will match with pattern where there
    # is at least one * alternatively
    for j in range(1, len_pattern):
        dp[0][j] = dp[0][j - 2] if pattern[j - 1] == "*" else 0

    # now using bottom-up approach to find for all remaining lengths
    for i in range(1, len_string):
        for j in range(1, len_pattern):
            if input_string[i - 1] == pattern[j - 1] or pattern[j - 1] == ".":
                dp[i][j] = dp[i - 1][j - 1]

            elif pattern[j - 1] == "*":
                if dp[i][j - 2] == 1:
                    dp[i][j] = 1
                elif pattern[j - 2] in (input_string[i - 1], "."):
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = 0
            else:
                dp[i][j] = 0

    return bool(dp[-1][-1])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # inputing the strings
    # input_string = input("input a string :")
    # pattern = input("input a pattern :")

    input_string = "aab"
    pattern = "c*a*b"

    # using function to check whether given string matches the given pattern
    if match_pattern(input_string, pattern):
        print(f"{input_string} matches the given pattern {pattern}")
    else:
        print(f"{input_string} does not match with the given pattern {pattern}")
