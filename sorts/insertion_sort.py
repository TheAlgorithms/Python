"""
This is a pure python implementation of the insertion sort algorithm

For doctests run following command:
python -m doctest -v insertion_sort.py
or
python3 -m doctest -v insertion_sort.py

For manual testing run:
python insertion_sort.py
"""
from __future__ import print_function


def insertion_sort(collection):
    """Pure implementation of the insertion sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> insertion_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> insertion_sort([])
    []

    >>> insertion_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    length = len(collection)
    for i in range(length):
        current_item = collection[i]
        j = i - 1
        while j >= 0 and current_item < collection[j]:
            collection[j+1] = collection[j]
            j -= 1
        collection[j+1] = current_item

    return collection


if __name__ == '__main__':
    import sys

    # For python 2.x and 3.x compatibility: 3.x has not raw_input builtin
    # otherwise 2.x's input builtin function is too "smart"
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function('Enter numbers separated by a comma:\n')
    unsorted = [int(item) for item in user_input.split(',')]
    print(insertion_sort(unsorted))
