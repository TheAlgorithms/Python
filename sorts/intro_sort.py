"""
Introspective Sort is a hybrid sort (Quick Sort + Heap Sort + Insertion Sort)
if the size of the list is under 16, use insertion sort
https://en.wikipedia.org/wiki/Introsort
"""

import math
from typing import Any, Protocol


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


def insertion_sort[T: Comparable](
    array: list[T], start: int = 0, end: int = 0
) -> list[T]:
    """
    >>> array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12]
    >>> insertion_sort(array, 0, len(array))
    [1, 2, 4, 6, 7, 8, 8, 12, 14, 14, 22, 23, 27, 45, 56, 79]
    >>> array = [21, 15, 11, 45, -2, -11, 46]
    >>> insertion_sort(array, 0, len(array))
    [-11, -2, 11, 15, 21, 45, 46]
    >>> array = [-2, 0, 89, 11, 48, 79, 12]
    >>> insertion_sort(array, 0, len(array))
    [-2, 0, 11, 12, 48, 79, 89]
    >>> array = ['a', 'z', 'd', 'p', 'v', 'l', 'o', 'o']
    >>> insertion_sort(array, 0, len(array))
    ['a', 'd', 'l', 'o', 'o', 'p', 'v', 'z']
    >>> array = [73.568, 73.56, -45.03, 1.7, 0, 89.45]
    >>> insertion_sort(array, 0, len(array))
    [-45.03, 0, 1.7, 73.56, 73.568, 89.45]
    """
    end = end or len(array)
    for i in range(start, end):
        temp_index = i
        temp_index_value = array[i]
        while temp_index != start and temp_index_value < array[temp_index - 1]:
            array[temp_index] = array[temp_index - 1]
            temp_index -= 1
        array[temp_index] = temp_index_value
    return array


def heapify[T: Comparable](
    array: list[T], index: int, heap_size: int, start: int = 0
) -> None:  # Max Heap
    """
    >>> array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12]
    >>> heapify(array, len(array) // 2, len(array))
    """
    largest = index
    left_index = 2 * (index - start) + 1 + start
    right_index = 2 * (index - start) + 2 + start

    if left_index < start + heap_size and array[largest] < array[left_index]:
        largest = left_index

    if right_index < start + heap_size and array[largest] < array[right_index]:
        largest = right_index

    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        heapify(array, largest, heap_size, start)


def heap_sort[T: Comparable](
    array: list[T], start: int = 0, end: int | None = None
) -> list[T]:
    """
    >>> heap_sort([4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12])
    [1, 2, 4, 6, 7, 8, 8, 12, 14, 14, 22, 23, 27, 45, 56, 79]
    >>> heap_sort([-2, -11, 0, 0, 0, 87, 45, -69, 78, 12, 10, 103, 89, 52])
    [-69, -11, -2, 0, 0, 0, 10, 12, 45, 52, 78, 87, 89, 103]
    >>> heap_sort(['b', 'd', 'e', 'f', 'g', 'p', 'x', 'z', 'b', 's', 'e', 'u', 'v'])
    ['b', 'b', 'd', 'e', 'e', 'f', 'g', 'p', 's', 'u', 'v', 'x', 'z']
    >>> heap_sort([6.2, -45.54, 8465.20, 758.56, -457.0, 0, 1, 2.879, 1.7, 11.7])
    [-457.0, -45.54, 0, 1, 1.7, 2.879, 6.2, 11.7, 758.56, 8465.2]
    """
    if end is None:
        end = len(array)
    n = end - start

    for i in range(start + n // 2, start - 1, -1):
        heapify(array, i, n, start)

    for i in range(start + n - 1, start, -1):
        array[i], array[start] = array[start], array[i]
        heapify(array, start, i - start, start)

    return array


def median_of_3[T: Comparable](
    array: list[T], first_index: int, middle_index: int, last_index: int
) -> T:
    """
    >>> array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12]
    >>> median_of_3(array, 0, ((len(array) - 0) // 2) + 1, len(array) - 1)
    12
    >>> array = [13, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12]
    >>> median_of_3(array, 0, ((len(array) - 0) // 2) + 1, len(array) - 1)
    13
    >>> array = [4, 2, 6, 8, 1, 7, 8, 22, 15, 14, 27, 79, 23, 45, 14, 16]
    >>> median_of_3(array, 0, ((len(array) - 0) // 2) + 1, len(array) - 1)
    14
    """
    if (array[middle_index] < array[first_index]) != (
        array[last_index] < array[first_index]
    ):
        return array[first_index]
    elif (array[first_index] < array[middle_index]) != (
        array[last_index] < array[middle_index]
    ):
        return array[middle_index]
    else:
        return array[last_index]


def partition[T: Comparable](array: list[T], low: int, high: int, pivot: T) -> int:
    """
    >>> array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12]
    >>> partition(array, 0, len(array), 12)
    8
    >>> array = [21, 15, 11, 45, -2, -11, 46]
    >>> partition(array, 0, len(array), 15)
    3
    >>> array = ['a', 'z', 'd', 'p', 'v', 'l', 'o', 'o']
    >>> partition(array, 0, len(array), 'p')
    5
    >>> array = [6.2, -45.54, 8465.20, 758.56, -457.0, 0, 1, 2.879, 1.7, 11.7]
    >>> partition(array, 0, len(array), 2.879)
    6
    """
    i = low
    j = high
    while True:
        while array[i] < pivot:
            i += 1
        j -= 1
        while pivot < array[j]:
            j -= 1
        if i >= j:
            return i
        array[i], array[j] = array[j], array[i]
        i += 1


def sort[T: Comparable](array: list[T]) -> list[T]:
    """
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> sort([4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12])
    [1, 2, 4, 6, 7, 8, 8, 12, 14, 14, 22, 23, 27, 45, 56, 79]
    >>> sort([-1, -5, -3, -13, -44])
    [-44, -13, -5, -3, -1]
    >>> sort([])
    []
    >>> sort([5])
    [5]
    >>> sort([-3, 0, -7, 6, 23, -34])
    [-34, -7, -3, 0, 6, 23]
    >>> sort([1.7, 1.0, 3.3, 2.1, 0.3 ])
    [0.3, 1.0, 1.7, 2.1, 3.3]
    >>> sort(['d', 'a', 'b', 'e', 'c'])
    ['a', 'b', 'c', 'd', 'e']
    >>> sort([1, 'a'])  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    TypeError: ...
    """
    if len(array) == 0:
        return array
    max_depth = 2 * math.ceil(math.log2(len(array)))
    size_threshold = 16
    return intro_sort(array, 0, len(array), size_threshold, max_depth)


def intro_sort[T: Comparable](
    array: list[T], start: int, end: int, size_threshold: int, max_depth: int
) -> list[T]:
    """
    >>> array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12]
    >>> max_depth = 2 * math.ceil(math.log2(len(array)))
    >>> intro_sort(array, 0, len(array), 16, max_depth)
    [1, 2, 4, 6, 7, 8, 8, 12, 14, 14, 22, 23, 27, 45, 56, 79]
    >>> values = [100, 4, 3, 2, 1, -100]
    >>> intro_sort(values, start=1, end=5, size_threshold=2, max_depth=0)
    [100, 1, 2, 3, 4, -100]
    """
    while end - start > size_threshold:
        if max_depth == 0:
            return heap_sort(array, start, end)
        max_depth -= 1
        pivot = median_of_3(array, start, start + ((end - start) // 2) + 1, end - 1)
        p = partition(array, start, end, pivot)
        intro_sort(array, p, end, size_threshold, max_depth)
        end = p
    return insertion_sort(array, start, end)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    user_input = input("Enter numbers separated by a comma : ").strip()
    unsorted = [float(item) for item in user_input.split(",")]
    print(f"{sort(unsorted) = }")
