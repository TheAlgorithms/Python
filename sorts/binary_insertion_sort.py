"""
This is a pure Python implementation of the binary insertion sort algorithm

For doctests run following command:
python -m doctest -v binary_insertion_sort.py
or
python3 -m doctest -v binary_insertion_sort.py

For manual testing run:
python binary_insertion_sort.py
"""


def binary_insertion_sort(collection: list) -> list:
    """Pure implementation of the binary insertion sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

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
        val = collection[i]
        low = 0
        high = i - 1

        while low <= high:
            mid = (low + high) // 2
            if val < collection[mid]:
                high = mid - 1
            else:
                low = mid + 1
        for j in range(i, low, -1):
            collection[j] = collection[j - 1]
        collection[low] = val
    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(binary_insertion_sort(unsorted))
