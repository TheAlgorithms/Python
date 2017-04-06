"""
This is a pure python implementation of the quick sort algorithm

For doctests run following command:
python -m doctest -v quick_sort.py
or
python3 -m doctest -v quick_sort.py

For manual testing run:
python quick_sort.py
"""
from __future__ import print_function


def quick_sort(ARRAY):
    """Pure implementation of quick sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> quick_sort([])
    []

    >>> quick_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    ARRAY_LENGTH = len(ARRAY)
    if( ARRAY_LENGTH <= 1):
        return ARRAY
    else:
        PIVOT = ARRAY[0]
        GREATER = [ element for element in ARRAY[1:] if element > PIVOT ]
        LESSER = [ element for element in ARRAY[1:] if element <= PIVOT ]
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)


if __name__ == '__main__':
    import sys

    # For python 2.x and 3.x compatibility: 3.x has not raw_input builtin
    # otherwise 2.x's input builtin function is too "smart"
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function('Enter numbers separated by a comma:\n')
    unsorted = [ int(item) for item in user_input.split(',') ]
    print( quick_sort(unsorted) )
