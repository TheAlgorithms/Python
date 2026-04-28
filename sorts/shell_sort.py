"""
Shell sort implementation.

Reference:
https://en.wikipedia.org/wiki/Shellsort#Pseudocode
"""


def shell_sort(collection: list[int]) -> list[int]:
    """
    Sort a list of integers in ascending order using Shell sort.

    :param collection: A list of integers to sort
    :return: The same list sorted in ascending order

    >>> shell_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> shell_sort([])
    []
    >>> shell_sort([-2, -5, -45])
    [-45, -5, -2]
    >>> shell_sort([3, "a"])  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    TypeError
    """
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        for index in range(gap, len(collection)):
            insert_value = collection[index]
            current_index = index

            while (
                current_index >= gap
                and collection[current_index - gap] > insert_value
            ):
                collection[current_index] = collection[current_index - gap]
                current_index -= gap

            collection[current_index] = insert_value

    return collection