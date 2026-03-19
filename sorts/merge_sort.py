"""
This is a pure Python implementation of the merge sort algorithm.

For doctests run following command:
python -m doctest -v merge_sort.py
or
python3 -m doctest -v merge_sort.py
For manual testing run:
python merge_sort.py
"""

from typing import Any


def merge_sort(collection: list[Any]) -> list[Any]:
    """
    Sorts a list using the merge sort algorithm.

    :param collection: A mutable ordered collection with comparable items.
    :return: The same collection ordered in ascending order.

    Time Complexity: O(n log n)
    Space Complexity: O(n)

    Examples:
    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> merge_sort([])
    []
    >>> merge_sort([-2, -5, -45])
    [-45, -5, -2]
    >>> merge_sort([1])
    [1]
    >>> merge_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> merge_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> merge_sort([3, 3, 3, 3])
    [3, 3, 3, 3]
    >>> merge_sort(['d', 'a', 'b', 'e', 'c'])
    ['a', 'b', 'c', 'd', 'e']
    >>> merge_sort([1.1, 0.5, 3.3, 2.2])
    [0.5, 1.1, 2.2, 3.3]
    >>> import random
    >>> collection_arg = random.sample(range(-50, 50), 100)
    >>> merge_sort(collection_arg) == sorted(collection_arg)
    True
    """

    def merge(left: list[Any], right: list[Any]) -> list[Any]:
        """
        Merge two sorted lists into a single sorted list using index-based
        traversal instead of pop(0) to achieve O(n) merge performance.

        :param left: Left sorted collection
        :param right: Right sorted collection
        :return: Merged sorted result

        >>> merge([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
        >>> merge([], [1, 2])
        [1, 2]
        >>> merge([1], [])
        [1]
        >>> merge([], [])
        []
        """
        result: list[Any] = []
        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        # Append any remaining elements from either list
        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result

    if len(collection) <= 1:
        return collection
    mid_index = len(collection) // 2
    return merge(merge_sort(collection[:mid_index]), merge_sort(collection[mid_index:]))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    try:
        user_input = input("Enter numbers separated by a comma:\n").strip()
        unsorted = [int(item) for item in user_input.split(",")]
        sorted_list = merge_sort(unsorted)
        print(*sorted_list, sep=",")
    except ValueError:
        print("Invalid input. Please enter valid integers separated by commas.")
