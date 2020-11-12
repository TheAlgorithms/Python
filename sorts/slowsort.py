"""
Slowsort is a sorting algorithm. It is of humorous nature and not useful.
It's based on the principle of multiply and surrender,
a tongue-in-cheek joke of divide and conquer.
It was published in 1986 by Andrei Broder and Jorge Stolfi
in their paper Pessimal Algorithms and Simplexity Analysis
(a parody of optimal algorithms and complexity analysis).

Source: https://en.wikipedia.org/wiki/Slowsort
"""

from typing import Optional


def slowsort(sequence: list, i: Optional[int] = None, j: Optional[int] = None) -> None:
    """
    Sorts sequence[i..j] (both inclusive) in-place.
    i defaults to 0 if not given.
    j defaults to len(sequence) - 1 if not given.
    It returns None.
    >>> sequence = [1, 6, 2, 5, 3, 4, 4, 5]; slowsort(sequence); sequence
    [1, 2, 3, 4, 4, 5, 5, 6]
    >>> sequence = []; slowsort(sequence); sequence
    []
    >>> sequence = [2]; slowsort(sequence); sequence
    [2]
    >>> sequence = [1, 2, 3, 4]; slowsort(sequence); sequence
    [1, 2, 3, 4]
    >>> sequence = [4, 3, 2, 1]; slowsort(sequence); sequence
    [1, 2, 3, 4]
    >>> sequence = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]; slowsort(sequence, 2, 7); sequence
    [9, 8, 2, 3, 4, 5, 6, 7, 1, 0]
    >>> sequence = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]; slowsort(sequence, j = 4); sequence
    [5, 6, 7, 8, 9, 4, 3, 2, 1, 0]
    >>> sequence = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]; slowsort(sequence, i = 5); sequence
    [9, 8, 7, 6, 5, 0, 1, 2, 3, 4]
    """
    if i is None:
        i = 0

    if j is None:
        j = len(sequence) - 1

    if i >= j:
        return

    m = (i + j) // 2

    slowsort(sequence, i, m)
    slowsort(sequence, m + 1, j)

    if sequence[j] < sequence[m]:
        sequence[j], sequence[m] = sequence[m], sequence[j]

    slowsort(sequence, i, j - 1)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
