"""
A variant of insertion sort that may yield in better performance if the
cost of comparisons exceeds the cost of swaps.

https://en.wikipedia.org/wiki/Insertion_sort#Variants
"""

from bisect import bisect


def binary_insertion_sort(collection: list) -> list:
    """
    Sorts a list using the binary insertion sort algorithm.

    :param collection: A mutable ordered collection with comparable items.
    :return: The same collection ordered in ascending order.

    Examples:
    >>> binary_insertion_sort([0, 4, 1234, 4, 1])
    [0, 1, 4, 4, 1234]
    >>> binary_insertion_sort([]) == sorted([])
    True
    >>> binary_insertion_sort([-1, -2, -3]) == sorted([-1, -2, -3])
    True
    >>> lst = ['d', 'a', 'b', 'e', 'c']
    >>> binary_insertion_sort(lst) == sorted(lst)
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

    n = len(collection)
    for i in range(1, n):
        value_to_insert = collection[i]
        insertion_pos = bisect(collection[:i], value_to_insert)
        for j in range(i, insertion_pos, -1):
            collection[j] = collection[j - 1]
        collection[insertion_pos] = value_to_insert
    return collection


if __name__ == "__main":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    try:
        unsorted = [int(item) for item in user_input.split(",")]
    except ValueError:
        print("Invalid input. Please enter valid integers separated by commas.")
        raise
    print(f"{binary_insertion_sort(unsorted) = }")
