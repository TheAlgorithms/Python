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


def binary_search(collection: list, val: int, start: int, end: int) -> int:
    """
    A pure Python implementation of the binary search  algorithm.

    :param collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of found item

    Examples:
    >>> binary_search([0, 5, 7, 10, 15], 0, 0, 4)
    0

    >>> binary_search([0, 5, 7, 10, 15], 15, 0, 4)
    5

    >>> binary_search([0, 5, 7, 10, 15], 5, 0, 4)
    2

    """
    if start == end:
        if collection[start] > val:
            return start
        else:
            return start + 1
    if start > end:
        return start
    mid = (start + end) // 2
    if collection[mid] < val:
        return binary_search(collection, val, mid + 1, end)
    elif collection[mid] > val:
        return binary_search(collection, val, start, mid - 1)
    else:
        return mid


def binary_insertion_sort(collection: list) -> list:
    """A pure Python implementation of the binary insertion sort algorithm

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> binary_insertion_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> binary_insertion_sort([]) == sorted([])
    True
    >>> binary_insertion_sort([-2, -5, -45]) == sorted([-2, -5, -45])
    True
    >>> binary_insertion_sort(['d', 'a', 'e', 'c']) == sorted(['d', 'a', 'e', 'c'])
    True
    >>> import random
    >>> collection = random.sample(range(-50, 50), 100)
    >>> binary_insertion_sort(collection) == sorted(collection)
    True
    >>> import string
    >>> collection = random.choices(string.ascii_letters + string.digits, k=100)
    >>> binary_insertion_sort(collection) == sorted(collection)
    True
    """
    for index in range(1, len(collection)):
        val = collection[index]
        mid = binary_search(collection, val, 0, index - 1)
        collection = (
            collection[:mid] + [val] + collection[mid:index] + collection[index + 1 :]
        )
    return collection


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(f"{binary_insertion_sort(unsorted) = }")
