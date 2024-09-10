"""
For doctests, run the following command:
python -m doctest -v merge_sort.py
or
python3 -m doctest -v merge_sort.py

For manual testing, run:
python merge_sort.py
"""

from __future__ import annotations
import itertools
import doctest
import sys


def binary_search_insertion(sorted_list: list[int], item: int) -> list[int]:
    """
    Inserts an item into a sorted list while maintaining order.

    >>> binary_search_insertion([1, 2, 7, 9, 10], 4)
    [1, 2, 4, 7, 9, 10]
    """
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        middle = (left + right) // 2
        if left == right:
            if sorted_list[middle] < item:
                left = middle + 1
            break
        elif sorted_list[middle] < item:
            left = middle + 1
        else:
            right = middle - 1
    sorted_list.insert(left, item)
    return sorted_list


def merge(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    """
    Merges two sorted lists into a single sorted list.

    >>> merge([[1, 6], [9, 10]], [[2, 3], [4, 5], [7, 8]])
    [[1, 6], [2, 3], [4, 5], [7, 8], [9, 10]]
    """
    result = []
    while left and right:
        if left[0][0] < right[0][0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right


def sortlist_2d(list_2d: list[list[int]]) -> list[list[int]]:
    """
    Sorts a 2D list based on the first element of each sublist.

    >>> sortlist_2d([[9, 10], [1, 6], [7, 8], [2, 3], [4, 5]])
    [[1, 6], [2, 3], [4, 5], [7, 8], [9, 10]]
    """
    length = len(list_2d)
    if length <= 1:
        return list_2d
    middle = length // 2
    return merge(sortlist_2d(list_2d[:middle]), sortlist_2d(list_2d[middle:]))


def merge_insertion_sort(collection: list[int]) -> list[int]:
    """Pure implementation of merge-insertion sort algorithm in Python

    :param collection: some mutable ordered collection with comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> merge_insertion_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> merge_insertion_sort([99])
    [99]

    >>> merge_insertion_sort([-2, -5, -45])
    [-45, -5, -2]

    Testing with all permutations on range(0,5):
    >>> import itertools
    >>> permutations = list(itertools.permutations([0, 1, 2, 3, 4]))
    >>> all(merge_insertion_sort(p) == [0, 1, 2, 3, 4] for p in permutations)
    True
    """

    if len(collection) <= 1:
        return collection

    two_paired_list = []
    has_last_odd_item = False
    for i in range(0, len(collection), 2):
        if i == len(collection) - 1:
            has_last_odd_item = True
        else:
            if collection[i] < collection[i + 1]:
                two_paired_list.append([collection[i], collection[i + 1]])
            else:
                two_paired_list.append([collection[i + 1], collection[i]])

    sorted_list_2d = sortlist_2d(two_paired_list)
    result = [i[0] for i in sorted_list_2d]
    result.append(sorted_list_2d[-1][1])

    if has_last_odd_item:
        pivot = collection[-1]
        result = binary_search_insertion(result, pivot)

    is_last_odd_item_inserted_before_this_index = False
    for i in range(len(sorted_list_2d) - 1):
        if result[i] == collection[-1] and has_last_odd_item:
            is_last_odd_item_inserted_before_this_index = True
        pivot = sorted_list_2d[i][1]
        if is_last_odd_item_inserted_before_this_index:
            result = result[: i + 2] + binary_search_insertion(result[i + 2 :], pivot)
        else:
            result = result[: i + 1] + binary_search_insertion(result[i + 1 :], pivot)

    return result


def merge_iter(input_list: list[int], low: int, mid: int, high: int) -> list[int]:
    """
    Sorts the left-half and right-half individually then merges them into a result.

    :param input_list: List to be sorted.
    :param low: Starting index of the segment.
    :param mid: Middle index to split the segment.
    :param high: Ending index of the segment.
    :return: Merged sorted list.
    """
    left = input_list[low : mid + 1]
    right = input_list[mid + 1 : high + 1]
    result = []

    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    input_list[low : high + 1] = result
    return input_list


def iter_merge_sort(input_list: list[int]) -> list[int]:
    """
    Return a sorted copy of the input list using iterative merge sort.

    >>> iter_merge_sort([5, 9, 8, 7, 1, 2, 7])
    [1, 2, 5, 7, 7, 8, 9]
    >>> iter_merge_sort([1])
    [1]
    >>> iter_merge_sort([2, 1])
    [1, 2]
    >>> iter_merge_sort([2, 1, 3])
    [1, 2, 3]
    >>> iter_merge_sort([4, 3, 2, 1])
    [1, 2, 3, 4]
    >>> iter_merge_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> iter_merge_sort(['c', 'b', 'a'])
    ['a', 'b', 'c']
    >>> iter_merge_sort([0.3, 0.2, 0.1])
    [0.1, 0.2, 0.3]
    >>> iter_merge_sort(['dep', 'dang', 'trai'])
    ['dang', 'dep', 'trai']
    >>> iter_merge_sort([6])
    [6]
    >>> iter_merge_sort([])
    []
    >>> iter_merge_sort([-2, -9, -1, -4])
    [-9, -4, -2, -1]
    >>> iter_merge_sort([1.1, 1, 0.0, -1, -1.1])
    [-1.1, -1, 0.0, 1, 1.1]
    """
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")

    n = len(input_list)
    if n <= 1:
        return input_list

    width = 1
    while width < n:
        for i in range(0, n, 2 * width):
            low = i
            mid = min(i + width - 1, n - 1)
            high = min(i + 2 * width - 1, n - 1)
            if mid < high:
                merge_iter(input_list, low, mid, high)
        width *= 2

    return input_list


def merge_sort(collection: list[int]) -> list[int]:
    """
    Sorts a list using the merge sort algorithm.

    :param collection: A mutable ordered collection with comparable items.
    :return: The same collection ordered in ascending order.

    Time Complexity: O(n log n)

    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> merge_sort([])
    []
    >>> merge_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    def merge(left: list[int], right: list[int]) -> list[int]:
        """
        Merge two sorted lists into a single sorted list.

        :param left: Left collection
        :param right: Right collection
        :return: Merged result
        """
        result = []
        while left and right:
            result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        result.extend(left)
        result.extend(right)
        return result

    if len(collection) <= 1:
        return collection
    mid_index = len(collection) // 2
    return merge(merge_sort(collection[:mid_index]), merge_sort(collection[mid_index:]))


if __name__ == "__main__":
    if not hasattr(sys, "gettrace") or sys.gettrace() is None:
        doctest.testmod()  # Only run tests if not debugging

    try:
        user_input = input("Enter numbers separated by a comma:\n").strip()
        unsorted = [int(item) for item in user_input.split(",")]

        sorted_list_merge_sort = merge_sort(unsorted)
        sorted_list_iter_merge_sort = iter_merge_sort(
            unsorted.copy()
        )  # Use copy to avoid sorting the same list twice
        sorted_list_merge_insertion_sort = merge_insertion_sort(unsorted.copy())

        print(f"Unsorted list: {unsorted}")
        print(f"Sorted list using merge_sort: {sorted_list_merge_sort}")
        print(f"Sorted list using iter_merge_sort: {sorted_list_iter_merge_sort}")
        print(
            f"Sorted list using merge_insertion_sort: {sorted_list_merge_insertion_sort}"
        )

        print("Merge Sort Result:", *sorted_list_merge_sort, sep=",")
        print("Iterative Merge Sort Result:", *sorted_list_iter_merge_sort, sep=",")
        print(
            "Merge Insertion Sort Result:", *sorted_list_merge_insertion_sort, sep=","
        )
    except ValueError:
        print("Invalid input. Please enter valid integers separated by commas.")
