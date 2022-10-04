"""
A pure Python implementation of the binary insertion sort algorithm

Binary insertion sort is a sorting algorithm which is similar to the insertion sort,
but instead of using linear search to find the location where an element should be
inserted, we use binary search. Thus, we reduce the comparative value of inserting
a single element from O (N) to O (log N).

For doctests run following command:
python3 -m doctest -v binary_insertion_sort.py

For manual testing run:
python3 binary_insertion_sort.py
"""

import sys

sys.path.append("../searches")
from binary_search import bisect_left


def binary_insertion_sort(collection: list[int]) -> list[int]:
    """A pure Python implementation of the binary insertion sort algorithm

    :param collection: a mutable collection of comparable items in any order
    :return: the same collection ordered by ascending

    Examples:
    >>> binary_insertion_sort([1, 2, 3, 2, 4, 5])
    [1, 2, 2, 3, 4, 5]
    >>> binary_insertion_sort([0.1, -2.4, 4.4, 2.2])
    [-2.4, 0.1, 2.2, 4.4]
    >>> binary_insertion_sort([]) == sorted([])
    True
    >>> binary_insertion_sort([-2, 5, 0, -45])
    [-45, -2, 0, 5]
    >>> binary_insertion_sort(['d', 'a', 'b', 'c']) == sorted(['d', 'a', 'b', 'c'])
    True
    >>> import random
    >>> collection = random.sample(range(-100, 100), 200)
    >>> binary_insertion_sort(collection) == sorted(collection)
    True
    >>> import string
    >>> collection = random.choices(string.ascii_letters + string.digits, k=100)
    >>> binary_insertion_sort(collection) == sorted(collection)
    True
    """
    for ind, val in enumerate(collection[1:]):
        mid = bisect_left(collection, val, 0, ind + 1)
        collection = (
            collection[:mid] + [val] + collection[mid : ind + 1] + collection[ind + 2 :]
        )
    return collection


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("integers", type=int, nargs="+", help="integers to sort")
    args = parser.parse_args()

    print(f"Unsorted: {args.integers}")
    print(f"Sorted: {binary_insertion_sort(args.integers)}")
