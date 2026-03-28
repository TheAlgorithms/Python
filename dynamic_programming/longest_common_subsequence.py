"""
LCS Problem Statement: Given two sequences, find the length of longest subsequence
present in both of them.  A subsequence is a sequence that appears in the same relative
order, but not necessarily continuous.
Example:"abc", "abg" are subsequences of "abcdefgh".
"""


def longest_common_subsequence_string(u: str, v: str) -> str:
    """
    Return the longest common subsequence of two strings using
    dynamic programming reconstruction.

    >>> longest_common_subsequence_string("AGGTAB", "GXTXAYB")
    'GTAB'
    >>> longest_common_subsequence_string("abcde", "ace")
    'ace'
    >>> longest_common_subsequence_string("abc", "abc")
    'abc'
    >>> longest_common_subsequence_string("abc", "def")
    ''
    >>> longest_common_subsequence_string("", "abc")
    ''
    """
    m, n = len(u), len(v)

    # Build the DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if u[i - 1] == v[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to reconstruct the actual subsequence
    lcs: list[str] = []
    i, j = m, n
    while i > 0 and j > 0:
        if u[i - 1] == v[j - 1]:
            lcs.append(u[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(lcs))

if __name__ == "__main__":
    a = "AGGTAB"
    b = "GXTXAYB"
    expected_subseq = "GTAB"

    subseq = longest_common_subsequence_string(a, b)
    print("sub-sequence =", subseq)
    assert subseq == expected_subseq

    import doctest
    doctest.testmod()
