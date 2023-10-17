from typing import Any


def bubble_sort_iterative(collection: list[Any]) -> list[Any]:
    """Pure implementation of bubble sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> bubble_sort_iterative([0, 5, 2, 3, 2])
    [0, 2, 2, 3, 5]
    >>> bubble_sort_iterative([0, 5, 2, 3, 2]) == sorted([0, 5, 2, 3, 2])
    True
    >>> bubble_sort_iterative([]) == sorted([])
    True
    >>> bubble_sort_iterative([-2, -45, -5]) == sorted([-2, -45, -5])
    True
    >>> bubble_sort_iterative([-23, 0, 6, -4, 34]) == sorted([-23, 0, 6, -4, 34])
    True
    >>> bubble_sort_iterative(['d', 'a', 'b', 'e']) == sorted(['d', 'a', 'b', 'e'])
    True
    >>> import random
    >>> collection = random.sample(range(-50, 50), 100)
    >>> bubble_sort_iterative(collection) == sorted(collection)
    True
    >>> import string
    >>> collection = random.choices(string.ascii_letters + string.digits, k=100)
    >>> bubble_sort_iterative(collection) == sorted(collection)
    True
    """
    length = len(collection)
    for i in reversed(range(length)):
        swapped = False
        for j in range(i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break  # Stop iteration if the collection is sorted.
    return collection


def bubble_sort_recursive(collection: list[Any]), length: int = 0) -> list[Any]:
    """
    It is similar is bubble sort but recursive.
    :param list_data: mutable ordered sequence of elements
    :param length: length of list data
    :return: the same list in ascending order

    >>> bubble_sort_recursive([0, 5, 2, 3, 2], 5)
    [0, 2, 2, 3, 5]

    >>> bubble_sort_recursive([], 0)
    []

    >>> bubble_sort_recursive([-2, -45, -5], 3)
    [-45, -5, -2]

    >>> bubble_sort_recursive([-23, 0, 6, -4, 34], 5)
    [-23, -4, 0, 6, 34]

    >>> bubble_sort_recursive([-23, 0, 6, -4, 34], 5) == sorted([-23, 0, 6, -4, 34])
    True

    >>> bubble_sort_recursive(['z','a','y','b','x','c'], 6)
    ['a', 'b', 'c', 'x', 'y', 'z']

    >>> bubble_sort_recursive([1.1, 3.3, 5.5, 7.7, 2.2, 4.4, 6.6])
    [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]
    """
    length = length or len(list_data)
    swapped = False
    for i in range(length - 1):
        if list_data[i] > list_data[i + 1]:
            list_data[i], list_data[i + 1] = list_data[i + 1], list_data[i]
            swapped = True

    return list_data if not swapped else bubble_sort_recursive(list_data, length - 1)


if __name__ == "__main__":
    import doctest
    import time

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma:").strip()
    unsorted = [int(item) for item in user_input.split(",")]

    print("Iterative bubble sort:")
    start = time.process_time()
    print(*bubble_sort_iterative(unsorted), sep=",")
    print(f"Processing time (iterative): {(time.process_time() - start) % 1e9 + 7}")

    print("\nRecursive bubble sort:")
    start = time.process_time()
    print(bubble_sort_recursive(unsorted, len(unsorted)))
    print(f"Processing time (recursive): {(time.process_time() - start) % 1e9 + 7}")
