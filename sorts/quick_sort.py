"""
A pure Python implementation of the quick sort algorithm

For doctests run following command:
python3 -m doctest -v quick_sort.py

For manual testing run:
python3 quick_sort.py
"""

from __future__ import annotations

from random import randrange


def quick_sort(collection: list) -> list:
    """A pure Python implementation of quicksort algorithm.

    :param collection: a mutable collection of comparable items
    :return: the same collection ordered in ascending order

    Time Complexity:
    Best Case: O(n log n)
    Average case: O(n log n)
    Worst Case: O(n^2)

    Space Complexity:
    Best Case: O(log n) for In-place implementation
    Worst Case: O(n)

    Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> quick_sort([])
    []
    >>> quick_sort([-2, 5, 0, -45])
    [-45, -2, 0, 5]
    """
    # Base case: if the collection has 0 or 1 elements, it is already sorted
    if len(collection) < 2:
        return collection

    # Randomly select a pivot index and remove the pivot element from the collection
    pivot_index = randrange(len(collection))
    pivot = collection.pop(pivot_index)

    # Initialise empty lists to store the elements

    lesser = []  # Stores elements less than or equal to the pivot
    greater = []  # Stores elements greater than the pivot

    # Loop through the collections and partition
    for item in collection:
        if item <= pivot:
            lesser.append(item)
        else:
            greater.append(item)

    # Recursively sort the lesser and greater groups, and combine with the pivot
    return [*quick_sort(lesser), pivot, *quick_sort(greater)]


if __name__ == "__main__":
    # Get user input and convert it into a list of integers
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]

    # Print the result of sorting the user-provided list
    print(quick_sort(unsorted))
