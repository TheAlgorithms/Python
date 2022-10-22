"""
Longest Common Substring Problem Statement: Given two sequences, find the length
of longest common substring present in both of them. A substring is
necessarily continuous.
Example: "abcdef" and "xabded" have two longest common substrings, "ab" or "de".
Therefore, the length is 2.
"""


def longest_common_substring(t1: str, t2: str) -> int:
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
    """

    assert t1 is not None
    assert t2 is not None

    t1_length = len(t1)
    t2_length = len(t2)

    dp = [[0] * (t2_length + 1) for _ in range(t1_length + 1)]
    ans = 0

    for i in range(1, t1_length + 1):
        for j in range(1, t2_length + 1):
            if t1[i - 1] == t2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                ans = max(ans, dp[i][j])

    return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
