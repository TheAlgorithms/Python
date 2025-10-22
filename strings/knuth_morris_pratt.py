"""
Implementation of the Knuth-Morris-Pratt (KMP) string searching algorithm.
The KMP algorithm searches for all occurrences of a "pattern" within a main "text"
by employing the observation that when a mismatch occurs, the pattern itself
embodies sufficient information to determine where the next match could begin,
thus bypassing re-examination of previously matched characters.

This results in an optimal time complexity of O(n + m), where n is the length
of the text and m is the length of the pattern.

Source: https://en.wikipedia.org/wiki/Knuth–Morris–Pratt_algorithm
"""

from __future__ import annotations


def _compute_lps_array(pattern: str) -> list[int]:
    """
    Computes the Longest Proper Prefix Suffix (LPS) array for the KMP algorithm.
    The LPS array for a pattern of length m is an array lps of size m where lps[i]
    is the length of the longest proper prefix of pattern[0...i] that is also a
    suffix of pattern[0...i].

    A "proper prefix" is a prefix of the string, but not the whole string.
    A "proper suffix" is a suffix of the string, but not the whole string.

    :param pattern: The pattern string to compute the LPS array for.
    :return: The LPS array, which is used to guide the search.

    >>> _compute_lps_array("aabaabaaa")
    [0, 1, 0, 1, 2, 3, 4, 5, 2]
    >>> _compute_lps_array("ababaca")
    [0, 0, 1, 2, 3, 0, 1]
    >>> _compute_lps_array("AAAA")
    [0, 1, 2, 3]
    >>> _compute_lps_array("abcde")
    [0, 0, 0, 0, 0]
    """
    m = len(pattern)
    lps = [0] * m
    length = 0  # Length of the previous longest prefix suffix
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def knuth_morris_pratt_search(text: str, pattern: str) -> list[int]:
    """
    Finds all occurrences of a pattern in a text using the KMP algorithm.

    :param text: The text to search in.
    :param pattern: The pattern to search for.
    :return: A list of starting indices of all occurrences of the pattern.
             Returns an empty list if the pattern is not found or is empty.

    >>> # Test cases from the original file
    >>> knuth_morris_pratt_search("alskfjaldsabc1abc1abc12k23adsfabcabc", "abc1abc12")
    [10]
    >>> knuth_morris_pratt_search("alskfjaldsk23adsfabcabc", "abc1abc12")
    []
    >>> knuth_morris_pratt_search("ABABZABABYABABX", "ABABX")
    [10]
    >>> knuth_morris_pratt_search("ABAAAAAB", "AAAB")
    [4]
    >>> knuth_morris_pratt_search("abcxabcdabxabcdabcdabcy", "abcdabcy")
    [15]
    >>> # More comprehensive test cases
    >>> knuth_morris_pratt_search("AABAACAADAABAABA", "AABA")
    [0, 9, 12]
    >>> knuth_morris_pratt_search("knuth_morris_pratt", "kn")
    [0]
    >>> knuth_morris_pratt_search("knuth_morris_pratt", "h_m")
    [4]
    >>> knuth_morris_pratt_search("knuth_morris_pratt", "rr")
    [12]
    >>> knuth_morris_pratt_search("knuth_morris_pratt", "tt")
    [16]
    >>> knuth_morris_pratt_search("knuth_morris_pratt", "not there")
    []
    >>> knuth_morris_pratt_search("test", "")
    []
    """
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []

    lps = _compute_lps_array(pattern)
    found_indices = []
    i = 0  # index for text
    j = 0  # index for pattern

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            found_indices.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return found_indices


if __name__ == "__main__":
    import doctest

    doctest.testmod()
