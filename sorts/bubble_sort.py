from typing import Any

"""
Bubble Sort Algorithms

This module provides iterative and optimized implementations
of the Bubble Sort algorithm.

Time Complexity:
    Best Case: O(n)
    Average Case: O(n^2)
    Worst Case: O(n^2)

Space Complexity:
    O(1)
"""


def bubble_sort_iterative(collection: list[Any]) -> list[Any]:
    """
    Bubble Sort (Iterative)

    Sorts a list in ascending order using the bubble sort algorithm.

    :param collection: A mutable list of comparable elements
    :return: Sorted list
    """

    n = len(collection)
    if n < 2:
        return collection

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):  # removed unnecessary start=0
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
                swapped = True

        if not swapped:
            break

    return collection


def bubble_sort_optimized(collection: list[Any]) -> list[Any]:
    """
    Optimized Bubble Sort

    Uses the last swap position to reduce unnecessary comparisons
    when part of the list is already sorted.

    :param collection: A mutable list of comparable elements
    :return: Sorted list
    """

    n = len(collection)
    if n < 2:
        return collection

    while n > 1:
        last_swap = 0
        for i in range(1, n):
            if collection[i - 1] > collection[i]:
                collection[i - 1], collection[i] = collection[i], collection[i - 1]
                last_swap = i
        n = last_swap

    return collection
