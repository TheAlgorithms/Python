"""
Python implementation of a sort algorithm.
Best Case Scenario : O(n)
Worst Case Scenario : O(n^2) because native Python functions:min, max and remove are
already O(n)
"""

from typing import Protocol


class Comparable(Protocol):
    def __lt__(self, other: object, /) -> bool: ...


def merge_sort[T: Comparable](collection: list[T]) -> list[T]:
    """Pure implementation of the fastest merge sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: a collection ordered by ascending

    Examples:
    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> merge_sort([])
    []

    >>> merge_sort([-2, -5, -45])
    [-45, -5, -2]

    >>> merge_sort(['d', 'a', 'b', 'e']) == sorted(['d', 'a', 'b', 'e'])
    True

    >>> merge_sort([1.1, 3.3, 5.5, 2.2, 4.4])
    [1.1, 2.2, 3.3, 4.4, 5.5]

    >>> merge_sort([1, "a"])  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    """
    start, end = [], []
    while len(collection) > 1:
        min_one, max_one = min(collection), max(collection)
        start.append(min_one)
        end.append(max_one)
        collection.remove(min_one)
        collection.remove(max_one)
    end.reverse()
    return start + collection + end


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(*merge_sort(unsorted), sep=",")
