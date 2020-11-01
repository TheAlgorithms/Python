"""
Finding the peak of a unimodal list using divide and conquer.
A unimodal array is defined as follows: array is increasing up to index p,
then decreasing afterwards. (for p >= 1)
An obvious solution can be performed in O(n),
to find the maximum of the array.
(From Kleinberg and Tardos. Algorithm Design.
Addison Wesley 2006: Chapter 5 Solved Exercise 1)
"""
from typing import List


def peak(lst: List[int]) -> int:
    """
    Return the peak value of `lst`.
    >>> peak([1, 2, 3, 4, 5, 4, 3, 2, 1])
    5
    >>> peak([1, 10, 9, 8, 7, 6, 5, 4])
    10
    >>> peak([1, 9, 8, 7])
    9
    >>> peak([1, 2, 3, 4, 5, 6, 7, 0])
    7
    >>> peak([1, 2, 3, 4, 3, 2, 1, 0, -1, -2])
    4
    """
    # middle index
    m = len(lst) // 2

    # choose the middle 3 elements
    three = lst[m - 1 : m + 2]

    # if middle element is peak
    if three[1] > three[0] and three[1] > three[2]:
        return three[1]

    # if increasing, recurse on right
    elif three[0] < three[2]:
        if len(lst[:m]) == 2:
            m -= 1
        return peak(lst[m:])

    # decreasing
    else:
        if len(lst[:m]) == 2:
            m += 1
        return peak(lst[:m])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
