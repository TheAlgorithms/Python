def longest_common_subsequence(s1: str, s2: str) -> str:
    """
    Returns the Longest Common Subsequence (LCS) of two strings.

    The LCS is the longest sequence of characters that appear in both strings in the
    same relative order, but not necessarily contiguously.

    Args:
        s1: The first string.
        s2: The second string.

    Returns:
        The longest common subsequence as a string.

    Example:
    >>> longest_common_subsequence("ABCBDAB", "BDCAB")
    'BCAB'
    >>> longest_common_subsequence("XMJYAUZ", "MZJAWXU")
    'MJAU'
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill DP table
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    # Backtrack to get LCS string
    i, j = m, n
    lcs_chars = []
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_chars.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(lcs_chars))


if __name__ == "__main__":
    # Basic tests
    print(longest_common_subsequence("ABCBDAB", "BDCAB"))  # BCAB
    print(longest_common_subsequence("XMJYAUZ", "MZJAWXU"))  # MJAU
