"""
Tournament Sort

Tournament sort is a comparison-based sorting algorithm that uses a priority
queue implemented as a tournament tree (also called a selection tree). It works
by repeatedly finding the minimum element from the remaining unsorted input
using a binary tree structure, similar to a single-elimination sports tournament.

The algorithm has two phases:
1. Build phase: Construct a tournament tree from the input to find the minimum.
2. Replacement phase: Replace the winner with infinity, rebuild the tree, and
   repeat to extract elements in sorted order.

Time Complexity:  O(n log n) for all cases
Space Complexity: O(n)

Reference:
    https://en.wikipedia.org/wiki/Tournament_sort
"""

from __future__ import annotations

import math


def tournament_sort(arr: list[int]) -> list[int]:
    """
    Sort a list of integers using tournament sort.

    Builds a tournament tree to repeatedly select the minimum element,
    producing a sorted list in ascending order.

    Args:
        arr: A list of integers to sort.

    Returns:
        A new sorted list in ascending order.

    >>> tournament_sort([5, 3, 8, 1, 9, 2])
    [1, 2, 3, 5, 8, 9]

    >>> tournament_sort([])
    []

    >>> tournament_sort([1])
    [1]

    >>> tournament_sort([4, 4, 4])
    [4, 4, 4]

    >>> tournament_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> tournament_sort(list(range(10, 0, -1))) == sorted(range(10, 0, -1))
    True
    """
    n = len(arr)
    if n <= 1:
        return list(arr)

    # Number of leaf nodes (next power of 2 >= n)
    num_leaves = 2 ** math.ceil(math.log2(n)) if n > 1 else 1

    # Build the leaf level: pad with infinity for missing positions
    inf = float("inf")
    leaves: list[float] = list(arr) + [inf] * (num_leaves - n)

    # Build internal nodes bottom-up; tree[0] unused, tree[1] = root
    # Leaves occupy indices [num_leaves, 2*num_leaves - 1]
    tree: list[float] = [inf] * (2 * num_leaves)
    for i in range(num_leaves):
        tree[num_leaves + i] = leaves[i]

    # Fill internal nodes: each parent = min of two children
    for i in range(num_leaves - 1, 0, -1):
        tree[i] = min(tree[2 * i], tree[2 * i + 1])

    result: list[int] = []

    for _ in range(n):
        # The root holds the current minimum
        minimum = tree[1]
        result.append(int(minimum))

        # Find and remove the winning leaf
        idx = 1
        while idx < num_leaves:
            left = 2 * idx
            right = 2 * idx + 1
            idx = left if tree[left] == minimum else right

        # Replace the winner with infinity and update ancestors
        tree[idx] = inf
        idx //= 2
        while idx >= 1:
            tree[idx] = min(tree[2 * idx], tree[2 * idx + 1])
            idx //= 2

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    user_input = input("Enter numbers separated by commas: ").strip()
    unsorted = [int(x) for x in user_input.split(",")]
    print(f"Unsorted: {unsorted}")
    print(f"Sorted:   {tournament_sort(unsorted)}")
