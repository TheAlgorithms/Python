"""
Boyer-Moore string search (bad-character rule) - improved and compatible.

This module provides both a function API `boyer_moore_search(text, pattern)`
and a class `BoyerMooreSearch` with method `bad_character_heuristic()` so it
remains compatible with existing usage while improving correctness, clarity,
and performance.

- Precomputes the bad-character table for O(1) lookup per mismatch.
- Uses a while-loop with proper shifting logic.
- Handles edge-cases (empty pattern matches at all positions).
- Includes doctests for typical cases and edge cases.

Author: your-github-username
License: MIT
"""

from __future__ import annotations

# We intentionally use built-in `dict` and `list` annotations (PEP 585).


def _build_bad_char_table(pattern: str) -> dict[str, int]:
    """Build mapping char -> last index in pattern."""
    table: dict[str, int] = {}
    for i, ch in enumerate(pattern):
        table[ch] = i
    return table


def boyer_moore_search(text: str, pattern: str) -> list[int]:
    """Return list of start indices where pattern occurs in text.

    >>> _build_bad_char_table("abcab")
    {'a': 3, 'b': 4, 'c': 2}
    >>> boyer_moore_search("abacaabaccabacaba", "aba")
    [0, 5, 10, 14]
    >>> boyer_moore_search("aaaaa", "aa")
    [0, 1, 2, 3]
    >>> boyer_moore_search("hello", "world")
    []
    >>> boyer_moore_search("", "")
    [0]
    >>> boyer_moore_search("abc", "")
    [0, 1, 2, 3]
    >>> boyer_moore_search("", "a")
    []
    """
    if pattern == "":
        return list(range(len(text) + 1))
    if text == "" or len(pattern) > len(text):
        return []

    n, m = len(text), len(pattern)
    bad = _build_bad_char_table(pattern)

    results: list[int] = []
    s = 0  # shift of the pattern with respect to text
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            results.append(s)
            # allow overlapping matches: shift by 1 to check next possible start
            s += 1
        else:
            last = bad.get(text[s + j], -1)
            shift = j - last
            s += shift if shift > 0 else 1
    return results


class BoyerMooreSearch:
    """Compatibility wrapper class around boyer_moore_search.

    Example:
    >>> bms = BoyerMooreSearch(text="ABAABA", pattern="AB")
    >>> bms.bad_character_heuristic()
    [0, 3]
    """

    def __init__(self, text: str, pattern: str) -> None:
        self.text = text
        self.pattern = pattern

    def bad_character_heuristic(self) -> list[int]:
        """Return match positions using bad-character heuristic."""
        return boyer_moore_search(self.text, self.pattern)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
