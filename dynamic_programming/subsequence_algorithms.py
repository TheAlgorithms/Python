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
def longest_subsequence(array: list[int]) -> list[int]:  # This function is recursive
    """
    Some examples
    >>> longest_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80])
    [10, 22, 33, 41, 60, 80]
    >>> longest_subsequence([4, 8, 7, 5, 1, 12, 2, 3, 9])
    [1, 2, 3, 9]
    >>> longest_subsequence([9, 8, 7, 6, 5, 7])
    [8]
    >>> longest_subsequence([1, 1, 1])
    [1, 1, 1]
    >>> longest_subsequence([])
    []
    """
    array_length = len(array)
    # If the array contains only one element, we return it (it's the stop condition of
    # recursion)
    if array_length <= 1:
        return array
        # Else
    pivot = array[0]
    is_found = False
    i = 1
    longest_subseq: list[int] = []
    while not is_found and i < array_length:
        if array[i] < pivot:
            is_found = True
            temp_array = [element for element in array[i:] if element >= array[i]]
            temp_array = longest_subsequence(temp_array)
            if len(temp_array) > len(longest_subseq):
                longest_subseq = temp_array
        else:
            i += 1

    temp_array = [element for element in array[1:] if element >= pivot]
    temp_array = [pivot, *longest_subsequence(temp_array)]
    if len(temp_array) > len(longest_subseq):
        return temp_array
    else:
        return longest_subseq

# Longest Common Subsequence (LCS)
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
