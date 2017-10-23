"""
This is pure python implementation of interpolation search algorithm
"""
from __future__ import print_function
import bisect


def interpolation_search(sorted_collection, item):
    """Pure implementation of interpolation search algorithm in Python
    Be careful collection must be sorted, otherwise result will be
    unpredictable
    :param sorted_collection: some sorted collection with comparable items
    :param item: item value to search
    :return: index of found item or None if item is not found
    """
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        point = left + ((item - sorted_collection[left]) * (right - left)) // (sorted_collection[right] - sorted_collection[left])
        
        #out of range check
        if point<0 or point>=len(sorted_collection):
            return None

        current_item = sorted_collection[point]
        if current_item == item:
            return point
        else:
            if item < current_item:
                right = point - 1
            else:
                left = point + 1
    return None


def interpolation_search_by_recursion(sorted_collection, item, left, right):

    """Pure implementation of interpolation search algorithm in Python by recursion
    Be careful collection must be sorted, otherwise result will be
    unpredictable
    First recursion should be started with left=0 and right=(len(sorted_collection)-1)
    :param sorted_collection: some sorted collection with comparable items
    :param item: item value to search
    :return: index of found item or None if item is not found
    """
    point = left + ((item - sorted_collection[left]) * (right - left)) // (sorted_collection[right] - sorted_collection[left])

    #out of range check
    if point<0 or point>=len(sorted_collection):
        return None

    if sorted_collection[point] == item:
        return point
    elif sorted_collection[point] > item:
        return interpolation_search_by_recursion(sorted_collection, item, left, point-1)
    else:
        return interpolation_search_by_recursion(sorted_collection, item, point+1, right)
      
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
    # For python 2.x and 3.x compatibility: 3.x has no raw_input builtin
    # otherwise 2.x's input builtin function is too "smart"
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function('Enter numbers separated by comma:\n')
    collection = [int(item) for item in user_input.split(',')]
    try:
        __assert_sorted(collection)
    except ValueError:
        sys.exit('Sequence must be sorted to apply interpolation search')

    target_input = input_function(
        'Enter a single number to be found in the list:\n'
    )
    target = int(target_input)
    result = interpolation_search(collection, target)
    if result is not None:
        print('{} found at positions: {}'.format(target, result))
    else:
        print('Not found')