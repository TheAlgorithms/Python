#!/usr/bin/env python3

"""
Binary search algorithms for sorted collections

For doctests run the following command:
python3 -m doctest -v binary_search.py

For manual testing run:
python3 binary_search.py
"""
from __future__ import annotations
from typing import List

import bisect


def bisect_left(sorted_collection: List[int], item: int, lo: int = 0, hi: int = -1) -> int:
    """
    Locates the first element in a sorted array that is larger or equal to a given
    value.

    :param sorted_collection: an ascending sorted list of comparable items
    :param item: item to bisect
    :param lo: lowest index to consider
    :param hi: past the highest index to consider
    :return: index i such that all values in sorted_collection[lo:i] are < item and all
        values in sorted_collection[i:hi] are >= item.
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


def bisect_right(sorted_collection: List[int], item: int, lo: int = 0, hi: int = -1) -> int:
    """
    Locates the first element in a sorted array that is larger than a given value.

    :param sorted_collection: an ascending sorted list of comparable items
    :param item: item to bisect
    :param lo: lowest index to consider
    :param hi: past the highest index to consider
    :return: index i such that all values in sorted_collection[lo:i] are <= item and
        all values in sorted_collection[i:hi] are > item.
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


def insort_left(sorted_collection: List[int], item: int, lo: int = 0, hi: int = -1) -> None:
    """
    Inserts a given value into a sorted array before other values with the same value.

    :param sorted_collection: an ascending sorted list of comparable items
    :param item: item to insert
    :param lo: lowest index to consider
    :param hi: past the highest index to consider
    """
    sorted_collection.insert(bisect_left(sorted_collection, item, lo, hi), item)


def insort_right(sorted_collection: List[int], item: int, lo: int = 0, hi: int = -1) -> None:
    """
    Inserts a given value into a sorted array after other values with the same value.

    :param sorted_collection: an ascending sorted list of comparable items
    :param item: item to insert
    :param lo: lowest index to consider
    :param hi: past the highest index to consider
    """
    sorted_collection.insert(bisect_right(sorted_collection, item, lo, hi), item)


def binary_search(sorted_collection: List[int], item: int) -> int:
    """Pure implementation of a binary search algorithm in Python

    Be careful, the collection must be ascending sorted; otherwise, the result will be
    unpredictable.

    :param sorted_collection: an ascending sorted list of comparable items
    :param item: item value to search
    :return: index of the found item or -1 if the item is not found
    """
    if sorted_collection != sorted(sorted_collection):
        raise ValueError("sorted_collection must be sorted in ascending order")
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = left + (right - left) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        elif item < current_item:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1


def binary_search_std_lib(sorted_collection: List[int], item: int) -> int:
    """Pure implementation of a binary search algorithm in Python using stdlib

    Be careful, the collection must be ascending sorted; otherwise, the result will be
    unpredictable.

    :param sorted_collection: an ascending sorted list of comparable items
    :param item: item value to search
    :return: index of the found item or -1 if the item is not found
    """
    if sorted_collection != sorted(sorted_collection):
        raise ValueError("sorted_collection must be sorted in ascending order")
    index = bisect.bisect_left(sorted_collection, item)
    if index != len(sorted_collection) and sorted_collection[index] == item:
        return index
    return -1


def binary_search_by_recursion(
    sorted_collection: List[int], item: int, left: int = 0, right: int = -1
) -> int:
    """Pure implementation of a binary search algorithm in Python by recursion

    Be careful, the collection must be ascending sorted; otherwise, the result will be
    unpredictable. The first recursion should be started with left=0 and right=(len(sorted_collection)-1).

    :param sorted_collection: an ascending sorted list of comparable items
    :param item: item value to search
    :param left: lowest index to consider
    :param right: highest index to consider
    :return: index of the found item or -1 if the item is not found
    """
    if right < 0:
        right = len(sorted_collection) - 1
    if sorted_collection != sorted(sorted_collection):
        raise ValueError("sorted_collection must be sorted in ascending order")
    if right < left:
        return -1

    midpoint = left + (right - left) // 2

    if sorted_collection[midpoint] == item:
        return midpoint
    elif sorted_collection[midpoint] > item:
        return binary_search_by_recursion(sorted_collection, item, left, midpoint - 1)
    else:
        return binary_search_by_recursion(sorted_collection, item, midpoint + 1, right)


def exponential_search(sorted_collection: List[int], item: int) -> int:
    """Pure implementation of an exponential search algorithm in Python

    Be careful, the collection must be ascending sorted; otherwise, the result will be
    unpredictable.

    :param sorted_collection: an ascending sorted list of comparable items
    :param item: item value to search
    :return: index of the found item or -1 if the item is not found

    the order of this algorithm is O(log I) where I is the index position of the item if it exists
    """
    if sorted_collection != sorted(sorted_collection):
        raise ValueError("sorted_collection must be sorted in ascending order")
    bound = 1
    while bound < len(sorted_collection) and sorted_collection[bound] < item:
        bound *= 2
    left = bound // 2
    right = min(bound, len(sorted_collection) - 1)
    last_result = binary_search_by_recursion(
        sorted_collection=sorted_collection, item=item, left=left, right=right
    )
    if last_result is None:
        return -1
    return last_result


searches = (  # Fastest to slowest...
    binary_search_std_lib,
    binary_search,
    exponential_search,
    binary_search_by_recursion,
)

if __name__ == "__main__":
    import doctest
    import timeit

    doctest.testmod()
    for search in searches:
        name = f"{search.__name__:>26}"
        print(f"{name}: {search([0, 5, 7, 10, 15], 10) = }")

    print("\nBenchmarks...")
    setup = "collection = list(range(1000))"
    for search in searches:
        name = search.__name__
        print(
            f"{name:>26}:",
            timeit.timeit(
                f"{name}(collection, 500)", setup=setup, number=5_000, globals=globals()
            ),
        )

    user_input = input("\nEnter numbers separated by a comma: ").strip()
    collection = sorted(int(item) for item in user_input.split(","))
    target = int(input("Enter a single number to be found in the list: "))
    result = binary_search(sorted_collection=collection, item=target)
    if result == -1:
        print(f"{target} was not found in {collection}.")
    else:
        print(f"{target} was found at position {result} of {collection}.")
