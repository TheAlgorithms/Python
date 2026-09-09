from collections.abc import MutableSequence
from typing import Any, Protocol


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


def selection_sort[T: Comparable](collection: MutableSequence[T]) -> MutableSequence[T]:
    """
    Sorts a list in ascending order using the selection sort algorithm.

    Selection sort divides the input list into a sorted and unsorted region.
    It repeatedly finds the minimum element from the unsorted region and
    places it at the end of the sorted region.

    Time Complexity: O(n²) in all cases
    Space Complexity: O(1)

    :param collection: A mutable sequence of comparable items to be sorted.
    :return: The same sequence sorted in ascending order.

    Examples:
    >>> selection_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> selection_sort([])
    []

    >>> selection_sort([-2, -5, -45])
    [-45, -5, -2]

    >>> selection_sort([1])
    [1]

    >>> selection_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]

    >>> selection_sort(["d", "a", "c", "b"])
    ['a', 'b', 'c', 'd']

    >>> selection_sort([3.2, 1.1, 2.4, 0.5])
    [0.5, 1.1, 2.4, 3.2]
    """
    length = len(collection)
    for i in range(length - 1):
        min_index = i
        for k in range(i + 1, length):
            if collection[k] < collection[min_index]:
                min_index = k
        if min_index != i:
            collection[i], collection[min_index] = collection[min_index], collection[i]
    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    sorted_list = selection_sort(unsorted)
    print("Sorted List:", sorted_list)
