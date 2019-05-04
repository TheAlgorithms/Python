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
    if length <= 1:
        return collection

    sorted_result = []
    midpoint = length // 2
    left_half_sorted = merge_sort(collection[:midpoint])
    right_half_sorted = merge_sort(collection[midpoint:])
    while len(left_half_sorted) > 0 and len(right_half_sorted) > 0:
        min_element = (
            left_half_sorted.pop(0) if left_half_sorted[0] <= right_half_sorted[0]
            else right_half_sorted.pop(0)
        )
        sorted_result.append(min_element)

    # If there is some remaining elements, they should be added into the sorted collection's end
    remaining_elements = left_half_sorted if len(left_half_sorted) > 0 else right_half_sorted
    sorted_result += remaining_elements

    # For more generic algorithm, making sure that the output and input types are the same
    for index, element in enumerate(sorted_result):
        collection[index] = element

    return collection


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(merge_sort(unsorted))
