"""
This is a pure Python implementation of the bozosort algorithm.

Bozosort chooses two elements at random and swaps them. It does
this repeatedly until the list is sorted.

For more info, check "Bozosort": https://en.wikipedia.org/wiki/Bogosort#Related_algorithms

For doctests run following command:
python -m doctest -v bozo_sort.py
or
python3 -m doctest -v bozo_sort.py

For manual testing run:
python bozo_sort.py
"""

import random


def bozo_sort(array: list) -> list:
    """
    Pure Python implementation of the bozosort algorithm.
    Examples:
    >>> bozo_sort([1, 14, 20, 9, 5])
    [1, 5, 9, 14, 20]
    >>> bozo_sort([8, 16, 0, 4, 10])
    [0, 4, 8, 10, 16]
    """

    while array != sorted(array):
        index_a = random.randint(0, len(array) - 1)
        index_b = random.randint(0, len(array) - 1)

        array[index_a], array[index_b] = array[index_b], array[index_a]

    return array


if __name__ == "__main__":
    user_array = input("Enter numbers separated by spaces: ")
    unsorted = [int(i) for i in user_array.split(" ")]

    print(bozo_sort(unsorted))
