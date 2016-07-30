"""
This is pure python implementation of binary search algorithm

For doctests run following command:
python -m doctest -v selection_sort.py
or
python3 -m doctest -v selection_sort.py

For manual testing run:
python binary_search.py
"""
from __future__ import print_function
import bisect


def assert_sorted(collection):
    """Check if collection is sorted. If not raises :py:class:`ValueError`

    :param collection: collection
    :return: True if collection is sorted
    :raise: :py:class:`ValueError` if collection is not sorted

    Examples:
    >>> assert_sorted([0, 1, 2, 4])
    True

    >>> assert_sorted([10, -1, 5])
    Traceback (most recent call last):
    ...
    ValueError: Collection must be sorted
    """
    if collection != sorted(collection):
        raise ValueError('Collection must be sorted')
    return True


def binary_search(sorted_collection, item):
    """Pure implementation of binary search algorithm in Python

    :param sorted_collection: some sorted collection with comparable items
    :param item: item value to search
    :return: index of found item or None if item is not found

    Examples:
    >>> binary_search([0, 5, 7, 10, 15], 0)
    0

    >>> binary_search([0, 5, 7, 10, 15], 15)
    4

    >>> binary_search([0, 5, 7, 10, 15], 5)
    1

    >>> binary_search([0, 5, 7, 10, 15], 6)

    >>> binary_search([5, 2, 1, 5], 2)
    Traceback (most recent call last):
    ...
    ValueError: Collection must be sorted
    """
    assert_sorted(sorted_collection)
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = (left + right) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        else:
            if item < current_item:
                right = midpoint - 1
            else:
                left = midpoint + 1
    return None


def binary_search_std_lib(sorted_collection, item):
    """Pure implementation of binary search algorithm in Python using stdlib

    :param sorted_collection: some sorted collection with comparable items
    :param item: item value to search
    :return: index of found item or None if item is not found

    Examples:
    >>> binary_search_std_lib([0, 5, 7, 10, 15], 0)
    0

    >>> binary_search_std_lib([0, 5, 7, 10, 15], 15)
    4

    >>> binary_search_std_lib([0, 5, 7, 10, 15], 5)
    1

    >>> binary_search_std_lib([0, 5, 7, 10, 15], 6)

    >>> binary_search_std_lib([5, 2, 1, 5], 2)
    Traceback (most recent call last):
    ...
    ValueError: Collection must be sorted
    """
    assert_sorted(sorted_collection)
    index = bisect.bisect_left(sorted_collection, item)
    if index != len(sorted_collection) and sorted_collection[index] == item:
        return index
    return None


if __name__ == '__main__':
    import sys
    # For python 2.x and 3.x compatibility: 3.x has not raw_input builtin
    # otherwise 2.x's input builtin function is too "smart"
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function('Enter numbers separated by coma:\n')
    collection = [int(item) for item in user_input.split(',')]

    target_input = input_function(
        'Enter a single number to be found in the list:\n'
    )
    target = int(target_input)
    result = binary_search(collection, target)
    if result is not None:
        print('{} found at positions: {}'.format(target, result))
    else:
        print('Not found')
