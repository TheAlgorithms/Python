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

    for loop_index in range(1, len(collection)):
        insertion_index = loop_index
        while insertion_index > 0 and collection[insertion_index - 1] > collection[insertion_index]:
            collection[insertion_index], collection[insertion_index - 1] = collection[insertion_index - 1], collection[insertion_index]
            insertion_index -= 1

    return collection


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(insertion_sort(unsorted))
