"""A merge sort which accepts comparable items and recursively
splits them in half, then sorts and combines the halves.

https://en.wikipedia.org/wiki/Merge_sort
"""

from collections.abc import Iterable
from typing import Protocol


class Comparable(Protocol):
    def __lt__(self, other: object, /) -> bool: ...


def merge[T: Comparable](collection: Iterable[T]) -> list[T]:
    """Return a new list of ``collection`` sorted in ascending order.

    The input is copied, so the original iterable is left unchanged.
    Items must be mutually comparable with ``<``.

    >>> merge([10,9,8,7,6,5,4,3,2,1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> merge([1,2,3,4,5,6,7,8,9,10])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> merge([10,22,1,2,3,9,15,23])
    [1, 2, 3, 9, 10, 15, 22, 23]
    >>> merge([100])
    [100]
    >>> merge([])
    []
    >>> merge(["c", "a", "b"])
    ['a', 'b', 'c']
    >>> merge([2.5, -1, 0.0])
    [-1, 0.0, 2.5]
    >>> values = [3, 1, 2]
    >>> merge(values)
    [1, 2, 3]
    >>> values
    [3, 1, 2]
    >>> merge(("b", "c", "a"))
    ['a', 'b', 'c']
    >>> merge([1, "a"])
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'int' and 'str'
    """
    arr = list(collection)
    if len(arr) > 1:
        middle_length = len(arr) // 2  # Finds the middle of the array
        # Sort each half into a new list, then combine those halves in ``arr``.
        left_array = merge(arr[:middle_length])
        right_array = merge(arr[middle_length:])
        left_size = len(left_array)
        right_size = len(right_array)
        left_index = 0  # Left Counter
        right_index = 0  # Right Counter
        index = 0  # Position Counter
        while (
            left_index < left_size and right_index < right_size
        ):  # Runs until the lowers size of the left and right are sorted.
            if left_array[left_index] < right_array[right_index]:
                arr[index] = left_array[left_index]
                left_index += 1
            else:
                arr[index] = right_array[right_index]
                right_index += 1
            index += 1
        while (
            left_index < left_size
        ):  # Adds the left over elements in the left half of the array
            arr[index] = left_array[left_index]
            left_index += 1
            index += 1
        while (
            right_index < right_size
        ):  # Adds the left over elements in the right half of the array
            arr[index] = right_array[right_index]
            right_index += 1
            index += 1
    return arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
