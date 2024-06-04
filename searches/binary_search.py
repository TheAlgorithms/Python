#!/usr/bin/env python3

from bisect import bisect_left, bisect_right


def bisect_left_custom(sorted_collection, item, lo=0, hi=None):
    """
    Custom implementation of bisect_left.
    Finds the position to insert item so that the list remains sorted.
    """
    if hi is None:
        hi = len(sorted_collection)
    while lo < hi:
        mid = (lo + hi) // 2
        if sorted_collection[mid] < item:
            lo = mid + 1
        else:
            hi = mid
    return lo


def bisect_right_custom(sorted_collection, item, lo=0, hi=None):
    """
    Custom implementation of bisect_right.
    Finds the position to insert item so that the list remains sorted.
    """
    if hi is None:
        hi = len(sorted_collection)
    while lo < hi:
        mid = (lo + hi) // 2
        if sorted_collection[mid] <= item:
            lo = mid + 1
        else:
            hi = mid
    return lo


def insort_left_custom(sorted_collection, item, lo=0, hi=None):
    """
    Inserts item into sorted_collection in sorted order (using bisect_left_custom).
    """
    sorted_collection.insert(bisect_left_custom(sorted_collection, item, lo, hi), item)


def insort_right_custom(sorted_collection, item, lo=0, hi=None):
    """
    Inserts item into sorted_collection in sorted order (using bisect_right_custom).
    """
    sorted_collection.insert(bisect_right_custom(sorted_collection, item, lo, hi), item)


def binary_search(sorted_collection, item):
    """
    Standard binary search implementation.
    Returns the index of item if found, else returns -1.
    """
    lo, hi = 0, len(sorted_collection) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_collection[mid] == item:
            return mid
        elif sorted_collection[mid] < item:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def binary_search_std_lib(sorted_collection, item):
    """
    Binary search using Python's standard library bisect module.
    """
    index = bisect_left(sorted_collection, item)
    if index != len(sorted_collection) and sorted_collection[index] == item:
        return index
    return -1


def binary_search_by_recursion(sorted_collection, item, lo=0, hi=None):
    """
    Binary search using recursion.
    """
    if hi is None:
        hi = len(sorted_collection) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if sorted_collection[mid] == item:
        return mid
    elif sorted_collection[mid] > item:
        return binary_search_by_recursion(sorted_collection, item, lo, mid - 1)
    else:
        return binary_search_by_recursion(sorted_collection, item, mid + 1, hi)


def exponential_search(sorted_collection, item):
    """
    Exponential search implementation.
    Useful for unbounded searches.
    """
    if sorted_collection[0] == item:
        return 0
    bound = 1
    while bound < len(sorted_collection) and sorted_collection[bound] < item:
        bound *= 2
    return binary_search_by_recursion(
        sorted_collection, item, bound // 2, min(bound, len(sorted_collection) - 1)
    )


if __name__ == "__main__":
    import doctest
    import timeit

    # Run doctests to validate examples
    doctest.testmod()

    # List of search functions to benchmark
    searches = [
        binary_search_std_lib,
        binary_search,
        exponential_search,
        binary_search_by_recursion,
    ]

    # Test and print results of searching for 10 in a sample list
    for search in searches:
        print(f"{search.__name__}: {search([0, 5, 7, 10, 15], 10) = }")

    print("\nBenchmarks...")
    setup = "collection = list(range(1000))"
    # Benchmark each search function
    for search in searches:
        time = timeit.timeit(
            f"{search.__name__}(collection, 500)",
            setup=setup,
            number=5000,
            globals=globals(),
        )
        print(f"{search.__name__:>26}: {time:.6f}")

    # Interactive part: user inputs a list and a target number
    user_input = input("\nEnter numbers separated by comma: ").strip()
    collection = sorted(int(item) for item in user_input.split(","))
    target = int(input("Enter a single number to be found in the list: "))
    result = binary_search(collection, target)
    if result == -1:
        print(f"{target} was not found in {collection}.")
    else:
        print(f"{target} was found at position {result} of {collection}.")
