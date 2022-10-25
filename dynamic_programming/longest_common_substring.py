"""
Longest Common Substring Problem Statement: Given two sequences, find the
longest common substring present in both of them. A substring is
necessarily continuous.
Example: "abcdef" and "xabded" have two longest common substrings, "ab" or "de".
Therefore, algorithm should return any one of them.
"""


def longest_common_substring(text1: str, text2: str) -> str:
    """
    Finds the longest common substring between two strings.
    >>> longest_common_substring("", "")
    ''
    >>> longest_common_substring("a","")
    ''
    >>> longest_common_substring("", "a")
    ''
    >>> longest_common_substring("a", "a")
    'a'
    >>> longest_common_substring("abcdef", "bcd")
    'bcd'
    >>> longest_common_substring("abcdef", "xabded")
    'ab'
    >>> longest_common_substring("GeeksforGeeks", "GeeksQuiz")
    'Geeks'
    >>> longest_common_substring("abcdxyz", "xyzabcd")
    'abcd'
    >>> longest_common_substring("zxabcdezy", "yzabcdezx")
    'abcdez'
    >>> longest_common_substring("OldSite:GeeksforGeeks.org", "NewSite:GeeksQuiz.com")
    'Site:Geeks'
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
    ans_index = 0
    ans_length = 0

    for i in range(1, text1_length + 1):
        for j in range(1, text2_length + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                if dp[i][j] > ans_length:
                    ans_index = i
                    ans_length = dp[i][j]

    return text1[ans_index - ans_length : ans_index]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
