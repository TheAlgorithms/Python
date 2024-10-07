"""
Author  : Mehdi ALAOUI

This is a pure Python implementation of Dynamic Programming solutions to:
1. Longest Increasing Subsequence (LIS)
2. Longest Common Subsequence (LCS)

1. LIS Problem: Given an array, find the longest increasing sub-array and return it.
Example: [10, 22, 9, 33, 21, 50, 41, 60, 80] -> [10, 22, 33, 41, 60, 80]

2. LCS Problem: Given two sequences, find the length and content of the longest
common subsequence that appears in both of them. A subsequence appears in the
same relative order but not necessarily continuously.
Example: "programming" and "gaming" -> "gaming"
"""

from __future__ import annotations


# Longest Increasing Subsequence (LIS)
def longest_increasing_subsequence(array: list[int]) -> list[int]:
    """
    Finds the longest increasing subsequence in the array.

    Examples:
    >>> longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80])
    [10, 22, 33, 41, 60, 80]
    >>> longest_increasing_subsequence([4, 8, 7, 5, 1, 12, 2, 3, 9])
    [1, 2, 3, 9]
    >>> longest_increasing_subsequence([9, 8, 7, 6, 5, 7])
    [5, 7]
    >>> longest_increasing_subsequence([1, 1, 1])
    [1]
    >>> longest_increasing_subsequence([])
    []
    """
    if not array:
        return []

    # dp[i] stores the length of the LIS ending at index i
    n = len(array)
    dp = [1] * n
    prev = [-1] * n  # To reconstruct the subsequence

    max_length = 1
    max_index = 0

    for i in range(1, n):
        for j in range(i):
            if array[i] > array[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[i] > max_length:
            max_length = dp[i]
            max_index = i

    # Reconstructing the longest increasing subsequence
    lis = []
    i = max_index
    while i >= 0:
        lis.append(array[i])
        i = prev[i]
        if i == -1:
            break

    return lis[::-1]


# Longest Common Subsequence (LCS)
def longest_common_subsequence(x: str, y: str) -> tuple[int, str]:
    """
    Finds the longest common subsequence between two strings and its length.

    Examples:
    >>> longest_common_subsequence("programming", "gaming")
    (6, 'gaming')
    >>> longest_common_subsequence("physics", "smartphone")
    (2, 'ph')
    >>> longest_common_subsequence("computer", "food")
    (1, 'o')
    >>> longest_common_subsequence("", "abc")
    (0, '')
    >>> longest_common_subsequence("abc", "")
    (0, '')
    >>> longest_common_subsequence("abcdef", "ace")
    (3, 'ace')
    """
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstructing the longest common subsequence
    i, j = m, n
    lcs = []
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            lcs.append(x[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], "".join(reversed(lcs))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage for LIS
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    lis = longest_increasing_subsequence(arr)
    print(f"Longest Increasing Subsequence: {lis}")

    # Example usage for LCS
    str1 = "AGGTAB"
    str2 = "GXTXAYB"
    length, lcs = longest_common_subsequence(str1, str2)
    print(f"Longest Common Subsequence: '{lcs}' with length {length}")
