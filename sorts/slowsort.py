"""
Slowsort is a sorting algorithm. It is of humorous nature and not useful.
It's based on the principle of multiply and surrender,
a tongue-in-cheek joke of divide and conquer.
It was published in 1986 by Andrei Broder and Jorge Stolfi
in their paper Pessimal Algorithms and Simplexity Analysis
(a parody of optimal algorithms and complexity analysis).

Source: https://en.wikipedia.org/wiki/Slowsort
"""

from __future__ import annotations


def slowsort(sequence: list, start: int | None = None, end: int | None = None) -> None:
    """
    Sorts sequence[start..end] (both inclusive) in-place.
    start defaults to 0 if not given.
    end defaults to len(sequence) - 1 if not given.
    It returns None.
    >>> seq = [1, 6, 2, 5, 3, 4, 4, 5]; slowsort(seq); seq
    [1, 2, 3, 4, 4, 5, 5, 6]
    >>> seq = []; slowsort(seq); seq
    []
    >>> seq = [2]; slowsort(seq); seq
    [2]
    >>> seq = [1, 2, 3, 4]; slowsort(seq); seq
    [1, 2, 3, 4]
    >>> seq = [4, 3, 2, 1]; slowsort(seq); seq
    [1, 2, 3, 4]
    >>> seq = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]; slowsort(seq, 2, 7); seq
    [9, 8, 2, 3, 4, 5, 6, 7, 1, 0]
    >>> seq = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]; slowsort(seq, end = 4); seq
    [5, 6, 7, 8, 9, 4, 3, 2, 1, 0]
    >>> seq = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]; slowsort(seq, start = 5); seq
    [9, 8, 7, 6, 5, 0, 1, 2, 3, 4]
    """
    if start is None:
        start = 0

    if end is None:
        end = len(sequence) - 1

    if start >= end:
        return

    mid = (start + end) // 2

    slowsort(sequence, start, mid)
    slowsort(sequence, mid + 1, end)

    if sequence[end] < sequence[mid]:
        sequence[end], sequence[mid] = sequence[mid], sequence[end]

    slowsort(sequence, start, end - 1)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
