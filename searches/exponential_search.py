"""
This is pure Python implementation of Exponential search.

Resources used:
https://en.wikipedia.org/wiki/Exponential_search

"""
from binary_search import binary_search_by_recursion


def exponential_search(sorted_collection: list[int], item: int) -> int | None:
    """Pure implementation of exponential search algorithm in Python

    Be careful collection must be ascending sorted, otherwise result will be
    unpredictable

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of found item or None if item is not found

    the order of this algorithm is O(lg I) where I is index position of item if exist

    Examples:
    >>> exponential_search([0, 5, 7, 10, 15], 0)
    0

    >>> exponential_search([0, 5, 7, 10, 15], 15)
    4

    >>> exponential_search([0, 5, 7, 10, 15], 5)
    1

    >>> exponential_search([0, 5, 7, 10, 15], 6)

    """
    bound = 1
    while bound < len(sorted_collection) and sorted_collection[bound] < item:
        bound *= 2
    left = int(bound / 2)
    right = min(bound, len(sorted_collection) - 1)
    return binary_search_by_recursion(
        sorted_collection=sorted_collection, item=item, left=left, right=right
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
