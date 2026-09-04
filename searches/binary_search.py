#!/usr/bin/env python3
"""
Pure Python implementations of binary search algorithms.

For doctests run:
    python3 -m doctest -v binary_search.py

For manual testing run:
    python3 binary_search.py
"""

import bisect
from collections.abc import Sequence
from itertools import pairwise
from typing import TypeVar

__all__ = [
    "bisect_left",
    "bisect_right",
    "insort_left",
    "insort_right",
    "binary_search",
    "binary_search_std_lib",
    "binary_search_with_duplicates",
    "binary_search_by_recursion",
    "exponential_search",
]

# ---------------------------------------------------------------------------
# Generic comparable type
# ---------------------------------------------------------------------------

T = TypeVar("T")  # Must support < via __lt__; mirrors what bisect itself accepts.


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _check_sorted(collection: Sequence) -> None:
    """Raise ValueError if *collection* is not sorted in ascending order.

    O(n) — uses adjacent-pair comparison, never allocates a sorted copy.
    """
    if any(a > b for a, b in pairwise(collection)):
        raise ValueError("collection must be sorted in ascending order")


# ---------------------------------------------------------------------------
# bisect_left / bisect_right
# ---------------------------------------------------------------------------


def bisect_left(
    sorted_collection: Sequence[T],
    item: T,
    lo: int = 0,
    hi: int = -1,
) -> int:
    """Return the leftmost index where *item* can be inserted to keep order.

    Mirrors :func:`bisect.bisect_left`.

    :param sorted_collection: ascending-sorted sequence of comparable items
    :param item: value to locate
    :param lo: lower search bound (inclusive)
    :param hi: upper search bound (exclusive); defaults to len(collection)
    :return: index *i* such that ``collection[lo:i] < item <= collection[i:hi]``

    Examples:
    >>> bisect_left([0, 5, 7, 10, 15], 0)
    0
    >>> bisect_left([0, 5, 7, 10, 15], 6)
    2
    >>> bisect_left([0, 5, 7, 10, 15], 20)
    5
    >>> bisect_left([0, 5, 7, 10, 15], 15, 1, 3)
    3
    >>> bisect_left([0, 5, 7, 10, 15], 6, 2)
    2
    """
    if hi < 0:
        hi = len(sorted_collection)

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if sorted_collection[mid] < item:
            lo = mid + 1
        else:
            hi = mid

    return lo


def bisect_right(
    sorted_collection: Sequence[T],
    item: T,
    lo: int = 0,
    hi: int = -1,
) -> int:
    """Return the rightmost index where *item* can be inserted to keep order.

    Mirrors :func:`bisect.bisect_right`.

    :param sorted_collection: ascending-sorted sequence of comparable items
    :param item: value to locate
    :param lo: lower search bound (inclusive)
    :param hi: upper search bound (exclusive); defaults to len(collection)
    :return: index *i* such that ``collection[lo:i] <= item < collection[i:hi]``

    Examples:
    >>> bisect_right([0, 5, 7, 10, 15], 0)
    1
    >>> bisect_right([0, 5, 7, 10, 15], 15)
    5
    >>> bisect_right([0, 5, 7, 10, 15], 6)
    2
    >>> bisect_right([0, 5, 7, 10, 15], 15, 1, 3)
    3
    >>> bisect_right([0, 5, 7, 10, 15], 6, 2)
    2
    """
    if hi < 0:
        hi = len(sorted_collection)

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if sorted_collection[mid] <= item:
            lo = mid + 1
        else:
            hi = mid

    return lo


# ---------------------------------------------------------------------------
# insort helpers
# ---------------------------------------------------------------------------


def insort_left(
    sorted_collection: list[T],
    item: T,
    lo: int = 0,
    hi: int = -1,
) -> None:
    """Insert *item* into *sorted_collection* before any equal values.

    Mirrors :func:`bisect.insort_left`.

    Examples:
    >>> col = [0, 5, 7, 10, 15]
    >>> insort_left(col, 6)
    >>> col
    [0, 5, 6, 7, 10, 15]
    >>> col = [(0, 0), (5, 5), (7, 7), (10, 10), (15, 15)]
    >>> item = (5, 5)
    >>> insort_left(col, item)
    >>> col
    [(0, 0), (5, 5), (5, 5), (7, 7), (10, 10), (15, 15)]
    >>> item is col[1]
    True
    >>> item is col[2]
    False
    """
    sorted_collection.insert(bisect_left(sorted_collection, item, lo, hi), item)


def insort_right(
    sorted_collection: list[T],
    item: T,
    lo: int = 0,
    hi: int = -1,
) -> None:
    """Insert *item* into *sorted_collection* after any equal values.

    Mirrors :func:`bisect.insort_right`.

    Examples:
    >>> col = [0, 5, 7, 10, 15]
    >>> insort_right(col, 6)
    >>> col
    [0, 5, 6, 7, 10, 15]
    >>> col = [(0, 0), (5, 5), (7, 7), (10, 10), (15, 15)]
    >>> item = (5, 5)
    >>> insort_right(col, item)
    >>> col
    [(0, 0), (5, 5), (5, 5), (7, 7), (10, 10), (15, 15)]
    >>> item is col[1]
    False
    >>> item is col[2]
    True
    """
    sorted_collection.insert(bisect_right(sorted_collection, item, lo, hi), item)


# ---------------------------------------------------------------------------
# Core binary search variants
# ---------------------------------------------------------------------------


def binary_search(sorted_collection: Sequence[T], item: T) -> int:
    """Iterative binary search.  Returns -1 when *item* is absent.

    :param sorted_collection: ascending-sorted sequence
    :param item: value to find
    :return: index of *item*, or ``-1`` if not found

    Examples:
    >>> binary_search([0, 5, 7, 10, 15], 0)
    0
    >>> binary_search([0, 5, 7, 10, 15], 15)
    4
    >>> binary_search([0, 5, 7, 10, 15], 5)
    1
    >>> binary_search([0, 5, 7, 10, 15], 6)
    -1
    >>> binary_search([], 1)
    -1
    """
    _check_sorted(sorted_collection)
    left, right = 0, len(sorted_collection) - 1

    while left <= right:
        mid = left + (right - left) // 2
        current = sorted_collection[mid]
        if current == item:
            return mid
        if item < current:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def binary_search_std_lib(sorted_collection: Sequence[T], item: T) -> int:
    """Binary search via the standard-library :mod:`bisect` module.

    IMPROVEMENT: replaced O(n log n) ``sorted()`` copy with O(n) pairwise check.

    :param sorted_collection: ascending-sorted sequence
    :param item: value to find
    :return: index of *item*, or ``-1`` if not found

    Examples:
    >>> binary_search_std_lib([0, 5, 7, 10, 15], 0)
    0
    >>> binary_search_std_lib([0, 5, 7, 10, 15], 15)
    4
    >>> binary_search_std_lib([0, 5, 7, 10, 15], 5)
    1
    >>> binary_search_std_lib([0, 5, 7, 10, 15], 6)
    -1
    """
    _check_sorted(sorted_collection)
    index = bisect.bisect_left(sorted_collection, item)
    if index < len(sorted_collection) and sorted_collection[index] == item:
        return index
    return -1


def binary_search_with_duplicates(sorted_collection: Sequence[T], item: T) -> list[int]:
    """Binary search that returns *all* indices where *item* appears.

    IMPROVEMENT: reuses the module-level ``bisect_left`` / ``bisect_right``
    instead of redefining equivalent inner functions.

    :param sorted_collection: ascending-sorted sequence
    :param item: value to find
    :return: sorted list of every index where *item* occurs (empty if absent)

    Examples:
    >>> binary_search_with_duplicates([0, 5, 7, 10, 15], 0)
    [0]
    >>> binary_search_with_duplicates([0, 5, 7, 10, 15], 15)
    [4]
    >>> binary_search_with_duplicates([1, 2, 2, 2, 3], 2)
    [1, 2, 3]
    >>> binary_search_with_duplicates([1, 2, 2, 2, 3], 4)
    []
    """
    _check_sorted(sorted_collection)
    left = bisect_left(sorted_collection, item)
    if left == len(sorted_collection) or sorted_collection[left] != item:
        return []
    right = bisect_right(sorted_collection, item)
    return list(range(left, right))


def binary_search_by_recursion(
    sorted_collection: Sequence[T],
    item: T,
    left: int = 0,
    right: int = -1,
) -> int:
    """Recursive binary search.  Returns -1 when *item* is absent.

    IMPROVEMENT: validation is performed once in the public entry-point and
    delegated to a private recursive helper, eliminating the O(n log n)
    re-validation that previously happened on every recursive call.

    :param sorted_collection: ascending-sorted sequence
    :param item: value to find
    :param left: lower bound index (inclusive); callers should use default
    :param right: upper bound index (inclusive); callers should use default
    :return: index of *item*, or ``-1`` if not found

    Examples:
    >>> binary_search_by_recursion([0, 5, 7, 10, 15], 0)
    0
    >>> binary_search_by_recursion([0, 5, 7, 10, 15], 15)
    4
    >>> binary_search_by_recursion([0, 5, 7, 10, 15], 5)
    1
    >>> binary_search_by_recursion([0, 5, 7, 10, 15], 6)
    -1
    >>> binary_search_by_recursion([], 1)
    -1
    """
    _check_sorted(sorted_collection)
    if right < 0:
        right = len(sorted_collection) - 1
    return _binary_search_recursive(sorted_collection, item, left, right)


def _binary_search_recursive(col: Sequence[T], item: T, left: int, right: int) -> int:
    """Internal recursive helper — no validation overhead."""
    if left > right:
        return -1
    mid = left + (right - left) // 2
    current = col[mid]
    if current == item:
        return mid
    if item < current:
        return _binary_search_recursive(col, item, left, mid - 1)
    return _binary_search_recursive(col, item, mid + 1, right)


# ---------------------------------------------------------------------------
# Exponential search
# ---------------------------------------------------------------------------


def exponential_search(sorted_collection: Sequence[T], item: T) -> int:
    """Exponential search — efficient when the target is near the start.

    Complexity: O(log i) where *i* is the index of *item*.
    Reference: https://en.wikipedia.org/wiki/Exponential_search

    IMPROVEMENT: removed dead ``if last_result is None`` guard (the callee
    never returns ``None``); validation is now done once up-front.

    :param sorted_collection: ascending-sorted sequence
    :param item: value to find
    :return: index of *item*, or ``-1`` if not found

    Examples:
    >>> exponential_search([0, 5, 7, 10, 15], 0)
    0
    >>> exponential_search([0, 5, 7, 10, 15], 15)
    4
    >>> exponential_search([0, 5, 7, 10, 15], 5)
    1
    >>> exponential_search([0, 5, 7, 10, 15], 6)
    -1
    >>> exponential_search([], 1)
    -1
    """
    _check_sorted(sorted_collection)
    n = len(sorted_collection)
    if n == 0:
        return -1

    bound = 1
    while bound < n and sorted_collection[bound] < item:
        bound *= 2

    left = bound // 2
    right = min(bound, n - 1)
    # Use the internal helper to avoid re-validating the (already-checked) collection.
    return _binary_search_recursive(sorted_collection, item, left, right)


# ---------------------------------------------------------------------------
# Benchmark / manual testing
# ---------------------------------------------------------------------------

searches = (  # Fastest to slowest…
    binary_search_std_lib,
    binary_search,
    exponential_search,
    binary_search_by_recursion,
)

if __name__ == "__main__":
    import doctest
    import timeit

    doctest.testmod()

    print("Spot-check results:")
    for search in searches:
        name = f"{search.__name__:>30}"
        print(f"  {name}: {search([0, 5, 7, 10, 15], 10) = }")

    print("\nBenchmarks (5 000 iterations on range(1000), target=500)…")
    setup = "collection = list(range(1000))"
    for search in searches:
        name = search.__name__
        elapsed = timeit.timeit(
            f"{name}(collection, 500)",
            setup=setup,
            number=5_000,
            globals=globals(),
        )
        print(f"  {name:>30}: {elapsed:.4f}s")

    user_input = input("\nEnter numbers separated by comma: ").strip()
    collection = sorted(int(x) for x in user_input.split(","))
    target = int(input("Enter a single number to find: "))
    result = binary_search(collection, target)
    if result == -1:
        print(f"{target} was not found in {collection}.")
    else:
        print(f"{target} was found at index {result} of {collection}.")
