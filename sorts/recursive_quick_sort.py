"""
A pure Python implementation of the recursive quick sort algorithm

This variant of quicksort picks the first element of the collection as the
pivot and recursively sorts the two sub-collections that fall on either
side of that pivot.  It returns a new list with the same items in
non-decreasing order; the input list is never modified (for inputs of
length less than two the very same list object is returned as-is).

For doctests run following command:
python3 -m doctest -v recursive_quick_sort.py

For manual testing run:
python3 recursive_quick_sort.py
"""

from typing import Any, Protocol, TypeVar


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


T = TypeVar("T", bound=Comparable)


def recursive_quick_sort[T: Comparable](collection: list[T]) -> list[T]:
    """A pure Python implementation of the recursive quick sort algorithm.

    The first element of ``collection`` is used as the pivot: every
    remaining item that is less than or equal to the pivot goes into
    the left sub-collection, every greater item into the right one, and
    the two sub-collections are then sorted recursively.

    Complexity Analysis:
        Time Complexity:
            - Best Case:    O(n log n) when the pivot splits evenly
            - Average Case: O(n log n)
            - Worst Case:   O(n^2) when the first element is always an
              extreme of the remaining items (e.g. an already sorted or
              reverse sorted collection)
        Space Complexity:
            - O(n) for the sub-collections built at every recursion level
              (the algorithm does not mutate the input)

    :param collection: some mutable ordered collection with mutually
        comparable items inside
    :return: a list with the same items ordered in ascending order

    Examples:
    >>> recursive_quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> recursive_quick_sort([])
    []
    >>> recursive_quick_sort([5])
    [5]
    >>> recursive_quick_sort([-2, 5, 0, -45])
    [-45, -2, 0, 5]
    >>> recursive_quick_sort([2, 1, 0]) == sorted([2, 1, 0])
    True
    >>> recursive_quick_sort([2.2, 1.1, 0.0]) == sorted([2.2, 1.1, 0.0])
    True
    >>> recursive_quick_sort([2.5, -1, 0.0]) == sorted([2.5, -1, 0.0])
    True
    >>> recursive_quick_sort(['d', 'a', 'b', 'c']) == sorted(['d', 'a', 'b', 'c'])
    True
    >>> recursive_quick_sort(['z', 'a', 'y', 'b', 'x', 'c'])
    ['a', 'b', 'c', 'x', 'y', 'z']
    >>> import random
    >>> collection = random.sample(range(-50, 50), 100)
    >>> recursive_quick_sort(collection) == sorted(collection)
    True
    >>> import string
    >>> collection = random.choices(string.ascii_letters + string.digits, k=100)
    >>> recursive_quick_sort(collection) == sorted(collection)
    True
    >>> recursive_quick_sort([1, "a"])  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError: '<=' not supported between instances of 'str' and 'int'
    """
    if len(collection) <= 1:
        return collection
    return [
        *recursive_quick_sort(
            [item for item in collection[1:] if item <= collection[0]]
        ),
        collection[0],
        *recursive_quick_sort(
            [item for item in collection[1:] if item > collection[0]]
        ),
    ]


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(f"{recursive_quick_sort(unsorted) = }")
