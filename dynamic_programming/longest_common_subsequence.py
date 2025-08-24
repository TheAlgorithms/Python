"""
LCS Problem Statement: Given two sequences, find the length of longest subsequence
present in both of them.  A subsequence is a sequence that appears in the same relative
order, but not necessarily continuous.
Example:"abc", "abg" are subsequences of "abcdefgh".
"""


def longest_common_subsequence(x: str, y: str):
    """
    Finds the longest common subsequence between two strings. Also returns the
    The subsequence found

    Parameters
    ----------

    x: str, one of the strings
    y: str, the other string

    Returns
    -------
    L[m][n]: int, the length of the longest subsequence. Also equal to len(seq)
    Seq: str, the subsequence found

    >>> longest_common_subsequence("programming", "gaming")
    (6, 'gaming')
    >>> longest_common_subsequence("physics", "smartphone")
    (2, 'ph')
    >>> longest_common_subsequence("computer", "food")
    (1, 'o')
    >>> longest_common_subsequence("", "abc")  # One string is empty
    (0, '')
    >>> longest_common_subsequence("abc", "")  # Other string is empty
    (0, '')
    >>> longest_common_subsequence("", "")  # Both strings are empty
    (0, '')
    >>> longest_common_subsequence("abc", "def")  # No common subsequence
    (0, '')
    >>> longest_common_subsequence("abc", "abc")  # Identical strings
    (3, 'abc')
    >>> longest_common_subsequence("a", "a")  # Single character match
    (1, 'a')
    >>> longest_common_subsequence("a", "b")  # Single character no match
    (0, '')
    >>> longest_common_subsequence("abcdef", "ace")  # Interleaved subsequence
    (3, 'ace')
    >>> longest_common_subsequence("ABCD", "ACBD")  # No repeated characters
    (3, 'ABD')
    """
    # find the length of strings

    assert x is not None
    assert y is not None

    m = len(x)
    n = len(y)

    # declaring the array for storing the dp values
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = 1 if x[i - 1] == y[j - 1] else 0

            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + match)

    seq = ""
    i, j = m, n
    while i > 0 and j > 0:
        match = 1 if x[i - 1] == y[j - 1] else 0

        if dp[i][j] == dp[i - 1][j - 1] + match:
            if match == 1:
                seq = x[i - 1] + seq
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], seq


if __name__ == "__main__":
    a = "AGGTAB"
    b = "GXTXAYB"
    expected_ln = 4
    expected_subseq = "GTAB"

    ln, subseq = longest_common_subsequence(a, b)
    print("len =", ln, ", sub-sequence =", subseq)
    import doctest

    doctest.testmod()
