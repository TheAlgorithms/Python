"""Knuth-Morris-Pratt substring search."""

from typing import List


def kmp_search(text: str, pattern: str) -> List[int]:
    if not pattern:
        return list(range(len(text) + 1))
    lps = _build_lps(pattern)
    matches: List[int] = []
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                matches.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return matches


def _build_lps(pattern: str) -> List[int]:
    lps = [0] * len(pattern)
    length = 0
    idx = 1
    while idx < len(pattern):
        if pattern[idx] == pattern[length]:
            length += 1
            lps[idx] = length
            idx += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[idx] = 0
            idx += 1
    return lps
