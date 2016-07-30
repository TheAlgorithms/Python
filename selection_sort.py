"""
This is pure python implementation of selection sort algorithm

For doctests run following command:
python -m doctest -v selection_sort.py
or
python3 -m doctest -v selection_sort.py
"""
from __future__ import print_function

def selection_sort(sortable):
    """Pure implementation of selection sort algorithm in Python

    Examples:
    >>> selection_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> selection_sort([])
    []

    >>> selection_sort([-2, -5, -45])
    [-45, -5, -2]

    :param sortable: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    """
    length = len(sortable)
    for i in range(length):
        least = i
        for k in range(i + 1, length):
            if sortable[k] < sortable[least]:
                least = k
        sortable[least], sortable[i] = (
            sortable[i], sortable[least]
        )
    return sortable


if __name__ == '__main__':
    import sys
    # For python 2.x and 3.x compatibility: 3.x has not raw_input builtin
    # otherwise 2.x's input builtin function is too "smart"
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function('Enter numbers separated by coma:\n')
    unsorted = [int(item) for item in user_input.split(',')]
    print(selection_sort(unsorted))
