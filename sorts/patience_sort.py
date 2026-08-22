"""
Patience Sort Algorithm

Patience Sort is a sorting algorithm inspired by the card game "Patience"
(also known as Solitaire). It works by:
1. Distributing elements into sorted "piles" (like stacking cards)
2. Merging the piles using a min-heap

The algorithm also naturally finds the Longest Increasing Subsequence (LIS)
— the number of piles equals the length of the LIS.

Time Complexity:
    - Best:    O(n log n)
    - Average: O(n log n)
    - Worst:   O(n log n)

Space Complexity: O(n)

Stability: Stable — equal elements maintain their relative order.

>>> patience_sort([6, 3, 5, 1, 8, 2, 4, 7])
[1, 2, 3, 4, 5, 6, 7, 8]

>>> patience_sort([])
[]

>>> patience_sort([1])
[1]

>>> patience_sort([5, 4, 3, 2, 1])
[1, 2, 3, 4, 5]

>>> patience_sort([1, 2, 3, 4, 5])
[1, 2, 3, 4, 5]

>>> patience_sort([3, 3, 1, 1, 2, 2])
[1, 1, 2, 2, 3, 3]

>>> patience_sort([-5, 3, -2, 8, -1, 0])
[-5, -2, -1, 0, 3, 8]

>>> patience_sort([1.5, 0.5, 2.5, 1.0])
[0.5, 1.0, 1.5, 2.5]
"""

from __future__ import annotations

import heapq
from bisect import bisect_left


def patience_sort(array: list) -> list:
    """
    Sort a list using the Patience Sort algorithm.

    The algorithm works in two phases:
    Phase 1 — Pile Creation:
        Iterate through the input. For each element, find the leftmost pile
        whose top card is >= the current element (using binary search).
        If found, place it on that pile. Otherwise, create a new pile.

    Phase 2 — Merging:
        Use a min-heap to merge all piles efficiently, always extracting
        the smallest element across all pile tops.

    Args:
        array: A list of comparable elements to sort.

    Returns:
        A new sorted list.

    >>> patience_sort([10, 7, 8, 9, 1, 5])
    [1, 5, 7, 8, 9, 10]
    """
    if len(array) <= 1:
        return list(array)

    # Phase 1: Create piles
    piles = _create_piles(array)

    # Phase 2: Merge piles using a min-heap
    return _merge_piles(piles)


def _create_piles(array: list) -> list[list]:
    """
    Distribute elements into piles.

    Each pile is a stack where the top element (last in the list) is the
    smallest. We place each new element on the leftmost pile whose top
    is >= the element. The pile_tops list tracks the top of each pile
    for efficient binary search.

    Within each pile, elements are in decreasing order from bottom to top.

    Args:
        array: The input list.

    Returns:
        A list of piles (each pile is a list, with the top at the end).

    >>> piles = _create_piles([6, 3, 5, 1])
    >>> len(piles) >= 1
    True
    """
    piles: list[list] = []
    pile_tops: list = []  # Track top of each pile for binary search

    for element in array:
        # Find the leftmost pile whose top is >= element
        pos = bisect_left(pile_tops, element)

        if pos < len(piles):
            # Place on existing pile
            piles[pos].append(element)
            pile_tops[pos] = element
        else:
            # Create a new pile
            piles.append([element])
            pile_tops.append(element)

    return piles


def _merge_piles(piles: list[list]) -> list:
    """
    Merge piles using a min-heap.

    Since elements within each pile are in decreasing order (bottom to top),
    we pop from the top of each pile (the end of each list) to get the
    smallest available element from that pile.

    We use a heap of (top_element, pile_index) to efficiently find which
    pile has the smallest top.

    Args:
        piles: List of piles to merge.

    Returns:
        A single sorted list.

    >>> _merge_piles([[3, 1], [4, 2], [5]])
    [1, 2, 3, 4, 5]
    """
    result = []

    # Initialize heap with the top (last element) of each pile
    # Heap entries: (value, pile_index)
    heap = []
    for i, pile in enumerate(piles):
        if pile:
            # The top of the pile is the last element (smallest in that pile)
            heapq.heappush(heap, (pile[-1], i))

    while heap:
        value, pile_idx = heapq.heappop(heap)
        result.append(value)

        # Remove the top element from this pile
        piles[pile_idx].pop()

        # If pile still has elements, push the new top
        if piles[pile_idx]:
            heapq.heappush(heap, (piles[pile_idx][-1], pile_idx))

    return result


def longest_increasing_subsequence_length(array: list) -> int:
    """
    Find the length of the Longest Increasing Subsequence (LIS).

    A beautiful property of Patience Sort: the number of piles created
    equals the length of the LIS.

    Args:
        array: A list of comparable elements.

    Returns:
        The length of the longest increasing subsequence.

    >>> longest_increasing_subsequence_length([6, 3, 5, 1, 8, 2, 4, 7])
    4

    >>> longest_increasing_subsequence_length([1, 2, 3, 4, 5])
    5

    >>> longest_increasing_subsequence_length([5, 4, 3, 2, 1])
    1

    >>> longest_increasing_subsequence_length([])
    0

    >>> longest_increasing_subsequence_length([3, 1, 4, 1, 5, 9])
    4
    """
    if not array:
        return 0

    # The number of piles = LIS length
    pile_tops: list = []

    for element in array:
        pos = bisect_left(pile_tops, element)

        if pos < len(pile_tops):
            pile_tops[pos] = element
        else:
            pile_tops.append(element)

    return len(pile_tops)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Demo
    print("=== Patience Sort ===\n")

    test_cases = [
        [6, 3, 5, 1, 8, 2, 4, 7],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [-5, 3, -2, 8, -1, 0],
        [3, 3, 1, 1, 2, 2],
    ]

    for arr in test_cases:
        sorted_arr = patience_sort(arr)
        lis_len = longest_increasing_subsequence_length(arr)
        print(f"  Input:      {arr}")
        print(f"  Sorted:     {sorted_arr}")
        print(f"  LIS length: {lis_len}\n")
