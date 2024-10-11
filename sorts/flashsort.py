"""
This is a Python implementation of the flashsort algorithm.

For doctests run the following command:
python3 -m doctest -v flashsort.py

For manual testing run:
python3 flashsort.py
"""

def flash_sort(collection: list) -> list:
    """A pure Python implementation of the flash sort algorithm.

    :param collection: a mutable collection of comparable items in any order
    :return: the same collection in ascending order

    Examples:
    >>> flash_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> flash_sort([])
    []
    >>> flash_sort([-2, 5, 0, -45])
    [-45, -2, 0, 5]
    >>> collections = ([], [0, 5, 3, 2, 2], [-2, 5, 0, -45])
    >>> all(sorted(collection) == flash_sort(collection) for collection in collections)
    True
    """

    n = len(collection)
    if n < 2:
        return collection

    max_value = max(collection)
    min_value = min(collection)

    m = int(n / 2) 
    L = [0] * m
    if max_value == min_value:
        return collection  

    for value in collection:
        class_index = int(m * (value - min_value) / (max_value - min_value))
        if class_index >= m:
            class_index = m - 1
        L[class_index] += 1

    for i in range(1, m):
        L[i] += L[i - 1]

    output = [0] * n
    for i in range(n - 1, -1, -1):
        value = collection[i]
        class_index = int(m * (value - min_value) / (max_value - min_value))
        if class_index >= m:
            class_index = m - 1
        output[L[class_index] - 1] = value
        L[class_index] -= 1
    for i in range(n):
        collection[i] = output[i]

    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(flash_sort(unsorted))
