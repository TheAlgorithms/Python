"""
Slowsort is a sorting algorithm. It is of humorous nature and not useful.
It's based on the principle of multiply and surrender, a tongue-in-cheek joke of divide and conquer.
It was published in 1986 by Andrei Broder and Jorge Stolfi
in their paper Pessimal Algorithms and Simplexity Analysis
(a parody of optimal algorithms and complexity analysis).

Source: https://en.wikipedia.org/wiki/Slowsort
"""

from math import floor

def slowsort(A : list, i : int = None, j : int = None) -> None:
    """
    Sorts A[i..j] (both inclusive) in-place.
    i defaults to 0 if not given.
    j defaults to len(A) - 1 if not given.
    It returns None.
    >>> a = [1, 6, 2, 5, 3, 4, 4, 5]; slowsort(a); a
    [1, 2, 3, 4, 4, 5, 5, 6]
    >>> a = []; slowsort(a); a
    []
    >>> a = [2]; slowsort(a); a
    [2]
    >>> a = [1, 2, 3, 4]; slowsort(a); a
    [1, 2, 3, 4]
    >>> a = [4, 3, 2, 1]; slowsort(a); a
    [1, 2, 3, 4]
    >>> a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]; slowsort(a, 2, 7); a
    [9, 8, 2, 3, 4, 5, 6, 7, 1, 0]
    >>> a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]; slowsort(a, j = 4); a
    [5, 6, 7, 8, 9, 4, 3, 2, 1, 0]
    >>> a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]; slowsort(a, i = 5); a
    [9, 8, 7, 6, 5, 0, 1, 2, 3, 4]
    """
    if i is None:
        i = 0
    
    if j is None:
        j = len(A) - 1
    
    if i >= j:
        return
    
    m = floor((i + j) / 2)
    
    slowsort(A, i, m)
    slowsort(A, m + 1, j)
    
    if A[j] < A[m]:
        A[j], A[m] = A[m], A[j]
    
    slowsort(A, i, j - 1)
