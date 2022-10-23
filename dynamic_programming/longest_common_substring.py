"""
Longest Common Substring Problem Statement: Given two sequences, find the length
of longest common substring present in both of them. A substring is
necessarily continuous.
Example: "abcdef" and "xabded" have two longest common substrings, "ab" or "de".
Therefore, the length is 2.
"""


def longest_common_substring(text1: str, text2: str) -> int:
    """
    Finds the length of longest common substring between two strings.

    >>> longest_common_substring("", "")
    0
    >>> longest_common_substring("a","")
    0
    >>> longest_common_substring("", "a")
    0
    >>> longest_common_substring("a", "a")
    1
    >>> longest_common_substring("abcdef", "bcd")
    3
    >>> longest_common_substring("abcdef", "xabded")
    2
    >>> longest_common_substring("GeeksforGeeks", "GeeksQuiz")
    5
    >>> longest_common_substring("abcdxyz", "xyzabcd")
    4
    >>> longest_common_substring("zxabcdezy", "yzabcdezx")
    6
    >>> longest_common_substring("OldSite:GeeksforGeeks.org", "NewSite:GeeksQuiz.com")
    10
    >>> longest_common_substring(1, 1)
    Traceback (most recent call last):
    ...
    ValueError: longest_common_substring() takes two strings for inputs
    """

    if not (isinstance(text1, str) and isinstance(text2, str)):
        raise ValueError("longest_common_substring() takes two strings for inputs")

    text1_length = len(text1)
    text2_length = len(text2)

    dp = [[0] * (text2_length + 1) for _ in range(text1_length + 1)]
    ans = 0

    for i in range(1, text1_length + 1):
        for j in range(1, text2_length + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                ans = max(ans, dp[i][j])

    return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
