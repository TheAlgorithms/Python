"""
This is pure python implementation of counting sort algorithm
For doctests run following command:
python -m doctest -v counting_sort.py
or
python3 -m doctest -v counting_sort.py
For manual testing run:
python counting_sort.py
"""

from __future__ import print_function


def counting_sort(collection):
    """Pure implementation of counting sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> counting_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> counting_sort([])
    []
    >>> counting_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    length = len(collection)
    maximum = max(collection)
    minimum = min(collection)
    counting_arr_length = maximum + 1 + abs(minimum)
    counting_arr = [0] * counting_arr_length
    for i in range(counting_arr_length):
        for j in range(length):
            if collection[j] == i + minimum:
                counting_arr[i] += 1

    j = 0
    for i in range(counting_arr_length):
        for k in range(counting_arr[i]):
            collection[j] = i + minimum
            j += 1

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
print(counting_sort(unsorted))