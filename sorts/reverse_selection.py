"""
A pure Python implementation of the Reverse Selection Sort algorithm

This algorithm progressively sorts the array by reversing subarrays

For doctests run following command:
python3 -m doctest -v reverse_selection_sort.py

For manual testing run:
python3 reverse_selection_sort.py
"""


def reverse_subarray(arr: list, start: int, end: int) -> None:
    """
    Reverse a subarray in-place.

    :param arr: the array containing the subarray to be reversed
    :param start: the starting index of the subarray
    :param end: the ending index of the subarray

    Examples:
    >>> lst = [1, 2, 3, 4, 5]
    >>> reverse_subarray(lst, 1, 3)
    >>> lst
    [1, 4, 3, 2, 5]

    >>> lst = [1]
    >>> reverse_subarray(lst, 0, 0)
    >>> lst
    [1]

    >>> lst = [1, 2]
    >>> reverse_subarray(lst, 0, 1)
    >>> lst
    [2, 1]
    """
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def reverse_selection_sort(collection: list) -> list:
    """
    A pure implementation of reverse selection sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection sorted in ascending order

    Examples:
    >>> reverse_selection_sort([1, 9, 5, 21, 17, 6])
    [1, 5, 6, 9, 17, 21]

    >>> reverse_selection_sort([])
    []

    >>> reverse_selection_sort([-3, -17, -48])
    [-48, -17, -3]

    >>> reverse_selection_sort([1, 1, 1, 1])
    [1, 1, 1, 1]

    >>> reverse_selection_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    """
    n = len(collection)
    for i in range(n - 1):
        # Find the minimum element in the unsorted portion
        min_idx = i
        for j in range(i + 1, n):
            if collection[j] < collection[min_idx]:
                min_idx = j

        # If the minimum is not at the start of the unsorted portion,
        # reverse the subarray to bring it to the front
        if min_idx != i:
            reverse_subarray(collection, i, min_idx)

    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(reverse_selection_sort(unsorted))
