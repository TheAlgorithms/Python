"""
Introspective Sort is hybrid sort (Quick Sort + Heap Sort + Insertion Sort)
if the size of the list is under 16, use insertion sort
"""
import math
import random


def insertion_sort(array: list, start: int, end: int) -> list:
    for i in range(start, end):
        temp_index = i
        temp_index_value = array[i]
        while temp_index != start and temp_index_value < array[temp_index - 1]:
            array[temp_index] = array[temp_index - 1]
            temp_index -= 1
        array[temp_index] = temp_index_value
    return array


def heapify(array: list, index: int, heap_size: int):  # Max Heap
    largest = index
    left_index = 2 * index + 1  # Left Node
    right_index = 2 * index + 2  # Right Node

    if left_index < heap_size and array[largest] < array[left_index]:
        largest = left_index

    if right_index < heap_size and array[largest] < array[right_index]:
        largest = right_index

    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        heapify(array, largest, heap_size)


def heap_sort(array: list) -> list:
    n = len(array)

    for i in range(n // 2, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, 0, i)

    return array


def median_of_3(
    array: list, first_index: int, middle_index: int, last_index: int
) -> int:
    if (array[first_index] > array[middle_index]) != (
        array[first_index] > array[last_index]
    ):
        return array[first_index]
    elif (array[middle_index] > array[first_index]) != (
        array[middle_index] > array[last_index]
    ):
        return array[middle_index]
    else:
        return array[last_index]


def partition(array: list, low: int, high: int, pivot: int) -> int:
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


def sort(array: list):
    max_depth = 2 * math.ceil(math.log2(len(array)))
    size_threshold = 16
    return intro_sort(array, 0, len(array), size_threshold, max_depth)


def intro_sort(array: list, start: int, end: int, size_threshold: int, max_depth: int):
    # if size > 16: heap sort or quick sort
    while end - start > size_threshold:
        if max_depth == 0:
            return heap_sort(array)
        max_depth -= 1
        pivot = median_of_3(array, start, start + ((end - start) // 2) + 1, end)
        p = partition(array, start, end, pivot)
        intro_sort(array, p, end, size_threshold, max_depth)
        end = p
    return insertion_sort(array)


if __name__ == "__main__":
    array = []
    for i in range(30):
        array.append(random.randrange(100))

    assert sort(array) == sorted(array)
