"""
This is a pure python implementation of the merge sort algorithm

For doctests run following command:
python -m doctest -v merge_sort.py
or
python3 -m doctest -v merge_sort.py

For manual testing run:
python merge_sort.py
"""
from __future__ import print_function


def merge_sort(collection):
    """Pure implementation of the merge sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> merge_sort([])
    []

    >>> merge_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    length = len(collection)
    if length > 1:
        midpoint = length // 2
        left_half = merge_sort(collection[:midpoint])
        right_half = merge_sort(collection[midpoint:])
        i = 0
        j = 0
        k = 0
        left_length = len(left_half)
        right_length = len(right_half)
        while i < left_length and j < right_length:
            if left_half[i] < right_half[j]:
                collection[k] = left_half[i]
                i += 1
            else:
                collection[k] = right_half[j]
                j += 1
            k += 1

        while i < left_length:
            collection[k] = left_half[i]
            i += 1
            k += 1

        while j < right_length:
            collection[k] = right_half[j]
            j += 1
            k += 1

    return collection


if __name__ == '__main__':
    import sys

    # For python 2.x and 3.x compatibility: 3.x has no raw_input builtin
    # otherwise 2.x's input builtin function is too "smart"
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function('Enter numbers separated by a comma:\n')
    unsorted = [int(item) for item in user_input.split(',')]
    print(merge_sort(unsorted))
