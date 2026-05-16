"""
Task:
Given an array of integers citations where citations[i] is the number of
citations a researcher received for their ith paper, return compute the
researcher's h-index.

According to the definition of h-index on Wikipedia: A scientist has an
index h if h of their n papers have at least h citations each, and the other
n - h papers have no more than h citations each.

If there are several possible values for h, the maximum one is taken as the
h-index.

H-Index link: https://en.wikipedia.org/wiki/H-index

Implementation notes:
Use sorting of array

Leetcode link: https://leetcode.com/problems/h-index/description/

n = len(citations)
Runtime Complexity: O(n * log(n))
Space  Complexity: O(1)

"""


def h_index(citations: list[int]) -> int:
    """
    Return H-index of citations

    >>> h_index([3, 0, 6, 1, 5])
    3
    >>> h_index([1, 3, 1])
    1
    >>> h_index([1, 2, 3])
    2
    >>> h_index('test')
    Traceback (most recent call last):
        ...
    ValueError: The citations should be a list of non negative integers.
    >>> h_index([1,2,'3'])
    Traceback (most recent call last):
        ...
    ValueError: The citations should be a list of non negative integers.
    >>> h_index([1,2,-3])
    Traceback (most recent call last):
        ...
    ValueError: The citations should be a list of non negative integers.
    """

    # validate:
    if not isinstance(citations, list) or not all(
        isinstance(item, int) and item >= 0 for item in citations
    ):
        raise ValueError("The citations should be a list of non negative integers.")

    citations.sort()
    len_citations = len(citations)

    for i in range(len_citations):
        if citations[len_citations - 1 - i] <= i:
            return i

    return len_citations


if __name__ == "__main__":
    import doctest

    doctest.testmod()
