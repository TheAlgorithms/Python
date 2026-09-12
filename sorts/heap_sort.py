"""
A pure Python implementation of the heap sort algorithm.
"""

from typing import Protocol


class Comparable(Protocol):
    def __lt__(self, other: object, /) -> bool: ...


def heapify[T: Comparable](unsorted: list[T], index: int, heap_size: int) -> None:
    """
    :param unsorted: unsorted list containing comparable items
    :param index: index
    :param heap_size: size of the heap
    :return: None
    >>> unsorted = [1, 4, 3, 5, 2]
    >>> heapify(unsorted, 0, len(unsorted))
    >>> unsorted
    [4, 5, 3, 1, 2]
    >>> heapify(unsorted, 0, len(unsorted))
    >>> unsorted
    [5, 4, 3, 1, 2]
    """
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < heap_size and unsorted[largest] < unsorted[left_index]:
        largest = left_index

    if right_index < heap_size and unsorted[largest] < unsorted[right_index]:
        largest = right_index

    if largest != index:
        unsorted[largest], unsorted[index] = (unsorted[index], unsorted[largest])
        heapify(unsorted, largest, heap_size)


def heap_sort[T: Comparable](unsorted: list[T]) -> list[T]:
    """
    A pure Python implementation of the heap sort algorithm.

    :param unsorted: a mutable collection of comparable items
    :return: the same collection ordered by ascending

    Examples:
    >>> heap_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> heap_sort([])
    []
    >>> heap_sort([-2, -5, -45])
    [-45, -5, -2]
    >>> heap_sort([3, 7, 9, 28, 123, -5, 8, -30, -200, 0, 4])
    [-200, -30, -5, 0, 3, 4, 7, 8, 9, 28, 123]
    >>> heap_sort(["banana", "apple", "cherry"])
    ['apple', 'banana', 'cherry']
    >>> heap_sort([3.14, 1.5, 2.7])
    [1.5, 2.7, 3.14]
    >>> heap_sort([1, "two"])  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: ...
    """
    n = len(unsorted)
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    user_input = input("Enter numbers separated by a comma:\n").strip()
    if user_input:
        unsorted = [int(item) for item in user_input.split(",")]
        print(f"{heap_sort(unsorted) = }")
