"""
Boyer-Moore-Horspool string-search algorithm.

A simplification of the Boyer-Moore algorithm that keeps only the
bad-character shift table (Horspool's variant).  It still runs in
sub-linear time on average (roughly O(n / m) for random text) while
worst case is O(n * m).  Memory is O(sigma) where sigma is the size
of the alphabet that appears in the pattern.

Reference: https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore%E2%80%93Horspool_algorithm
"""

from __future__ import annotations


def _build_shift_table(pattern: str) -> dict[str, int]:
    """
    Build the bad-character shift table for ``pattern``.

    For every character in the pattern except the last one, the table
    stores the distance from that character to the end of the pattern.
    Characters that do not appear in the pattern fall back to ``len(pattern)``
    at lookup time.

    >>> _build_shift_table("abcab")
    {'a': 1, 'b': 3, 'c': 2}
    >>> _build_shift_table("a")
    {}
    >>> _build_shift_table("")
    {}
    >>> _build_shift_table("aaaa")
    {'a': 1}
    """
    pattern_length = len(pattern)
    table: dict[str, int] = {}
    for index in range(pattern_length - 1):
        table[pattern[index]] = pattern_length - 1 - index
    return table


def boyer_moore_horspool_search(text: str, pattern: str) -> int:
    """
    Return the index of the first occurrence of ``pattern`` in ``text``
    or ``-1`` if the pattern does not appear.

    An empty pattern matches at position ``0`` (the same convention used by
    :py:meth:`str.find`).

    >>> boyer_moore_horspool_search("ABAAABCD", "ABC")
    4
    >>> boyer_moore_horspool_search("hello world", "world")
    6
    >>> boyer_moore_horspool_search("hello world", "Python")
    -1
    >>> boyer_moore_horspool_search("aaaaa", "aa")
    0
    >>> boyer_moore_horspool_search("anything", "")
    0
    >>> boyer_moore_horspool_search("", "x")
    -1
    >>> sample = "the quick brown fox jumps over the lazy dog"
    >>> boyer_moore_horspool_search(sample, "fox") == sample.find("fox")
    True
    >>> boyer_moore_horspool_search(sample, "cat") == sample.find("cat")
    True
    """
    pattern_length = len(pattern)
    text_length = len(text)
    if pattern_length == 0:
        return 0
    if pattern_length > text_length:
        return -1

    shift_table = _build_shift_table(pattern)
    skip = 0
    while text_length - skip >= pattern_length:
        index = pattern_length - 1
        while index >= 0 and pattern[index] == text[skip + index]:
            index -= 1
        if index < 0:
            return skip
        skip += shift_table.get(text[skip + pattern_length - 1], pattern_length)
    return -1


def boyer_moore_horspool_search_all(text: str, pattern: str) -> list[int]:
    """
    Return every starting index where ``pattern`` occurs in ``text``.

    Overlapping matches are reported (e.g. ``"aaa"`` contains ``"aa"``
    at indices ``0`` and ``1``).  An empty pattern matches at every
    position from ``0`` to ``len(text)`` inclusive, mirroring
    :py:meth:`str.find` and :py:func:`re.finditer` conventions.

    >>> boyer_moore_horspool_search_all("ababcabab", "ab")
    [0, 2, 5, 7]
    >>> boyer_moore_horspool_search_all("aaaa", "aa")
    [0, 1, 2]
    >>> boyer_moore_horspool_search_all("abcdef", "gh")
    []
    >>> boyer_moore_horspool_search_all("abc", "")
    [0, 1, 2, 3]
    >>> boyer_moore_horspool_search_all("", "abc")
    []
    """
    pattern_length = len(pattern)
    text_length = len(text)
    if pattern_length == 0:
        return list(range(text_length + 1))
    if pattern_length > text_length:
        return []

    shift_table = _build_shift_table(pattern)
    matches: list[int] = []
    skip = 0
    while text_length - skip >= pattern_length:
        index = pattern_length - 1
        while index >= 0 and pattern[index] == text[skip + index]:
            index -= 1
        if index < 0:
            matches.append(skip)
            skip += 1
        else:
            skip += shift_table.get(text[skip + pattern_length - 1], pattern_length)
    return matches


if __name__ == "__main__":
    import doctest

    doctest.testmod()
