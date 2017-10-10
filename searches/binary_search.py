"""
This is pure python implementation of binary search algorithm

For doctests run following command:
python -m doctest -v binary_search.py
or
python3 -m doctest -v binary_search.py

For manual testing run:
python binary_search.py
"""
from __future__ import print_function
import bisect


def binary_search(sorted_collection, item):
    """Pure implementation of binary search algorithm in Python

    Be careful collection must be sorted, otherwise result will be
    unpredictable

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

    """
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

    Be careful collection must be sorted, otherwise result will be
    unpredictable

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

    """
    index = bisect.bisect_left(sorted_collection, item)
    if index != len(sorted_collection) and sorted_collection[index] == item:
        return index
    return None

def binary_search_by_recursion(sorted_collection, item, left, right):

    """Pure implementation of binary search algorithm in Python by recursion

    Be careful collection must be sorted, otherwise result will be
    unpredictable
    First recursion should be started with left=0 and right=(len(sorted_collection)-1)

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

    """
    midpoint = left + (right - left) // 2

    if sorted_collection[midpoint] == item:
        return midpoint
    elif sorted_collection[midpoint] > item:
        return binary_search_by_recursion(sorted_collection, item, left, midpoint-1)
    else:
        return binary_search_by_recursion(sorted_collection, item, midpoint+1, right)

def __assert_sorted(collection):
    """Check if collection is sorted, if not - raises :py:class:`ValueError`

    :param collection: collection
    :return: True if collection is sorted
    :raise: :py:class:`ValueError` if collection is not sorted

    Examples:
    >>> __assert_sorted([0, 1, 2, 4])
    True

    >>> __assert_sorted([10, -1, 5])
    Traceback (most recent call last):
    ...
    ValueError: Collection must be sorted
    """
    if collection != sorted(collection):
        raise ValueError('Collection must be sorted')
    return True


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
    try:
        __assert_sorted(collection)
    except ValueError:
        sys.exit('Sequence must be sorted to apply binary search')

    target_input = input_function(
        'Enter a single number to be found in the list:\n'
    )
    target = int(target_input)
    result = binary_search(collection, target)
    if result is not None:
        print('{} found at positions: {}'.format(target, result))
    else:
        print('Not found')
