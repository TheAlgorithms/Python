"""
Longest Repeating Subsequence (LRS)

Given a string, find the length of the longest repeating subsequence, i.e., the
longest subsequence that occurs at least twice. The two occurrences must use
characters at different positions in the original string.

This is a variation of the Longest Common Subsequence (LCS) problem where we find
the LCS of the string with itself, with the constraint that characters at the same
index position cannot both be used.

Reference: https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
"""


def longest_repeating_subsequence(string: str) -> int:
    """
    Find the length of the longest repeating subsequence in the given string.

    A repeating subsequence is a subsequence that appears at least twice in the
    string, where characters at the same index are not counted as part of both
    subsequences simultaneously.

    Uses dynamic programming with time complexity O(n^2) and space complexity O(n^2),
    where n is the length of the input string.

    Parameters
    ----------
    string : str
        The input string to search for repeating subsequences.

    Returns
    -------
    int
        The length of the longest repeating subsequence.

    Examples
    --------
    >>> longest_repeating_subsequence("aabb")
    2
    >>> longest_repeating_subsequence("aab")
    1
    >>> longest_repeating_subsequence("axxxy")
    2
    >>> longest_repeating_subsequence("abcabc")
    3
    >>> longest_repeating_subsequence("")
    0
    >>> longest_repeating_subsequence("a")
    0
    >>> longest_repeating_subsequence("abcdef")
    0
    >>> longest_repeating_subsequence("aaa")
    2
    >>> longest_repeating_subsequence("aaaa")
    3
    >>> longest_repeating_subsequence(12345)
    Traceback (most recent call last):
        ...
    TypeError: Input must be a string, got int
    """
    if not isinstance(string, str):
        msg = f"Input must be a string, got {type(string).__name__}"
        raise TypeError(msg)

    n = len(string)
    if n == 0:
        return 0

    # dp[i][j] stores the length of the longest repeating subsequence
    # considering string[0..i-1] and string[0..j-1]
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Characters match and are at different positions
            if string[i - 1] == string[j - 1] and i != j:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][n]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
