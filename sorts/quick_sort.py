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


def quick_sort(collection):
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
    length = len(collection)
    if length <= 1:
        return collection
    else:
        pivot = collection[0]
        # Modify the list comprehensions to reduce the number of judgments, the speed has increased by more than 50%.
        greater = []
        lesser = []
        for element in collection[1:]:
            if element > pivot:
                greater.append(element)
            else:
                lesser.append(element)
        # greater = [element for element in collection[1:] if element > pivot]
        # lesser = [element for element in collection[1:] if element <= pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [ int(item) for item in user_input.split(',') ]
    print( quick_sort(unsorted) )
