"""
https://en.wikipedia.org/wiki/Shellsort#Pseudocode
"""


def shell_sort(collection: list[int]) -> list[int]:
    """
    Sort a list of integers using the Shell Sort algorithm.

    Reference:
    https://en.wikipedia.org/wiki/Shellsort

    >>> shell_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> shell_sort([])
    []
    >>> shell_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        for i in range(gap, len(collection)):
            insert_value = collection[i]
            j = i
            while j >= gap and collection[j - gap] > insert_value:
                collection[j] = collection[j - gap]
                j -= gap
            collection[j] = insert_value

    return collection
