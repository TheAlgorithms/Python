"""
This is pure Python implementation of interpolation search algorithm
"""


def interpolation_search(sorted_collection: list[int], item: int) -> int | None:
    """
    Searches for an item in a sorted collection by interpolation search algorithm.

    Args:
        sorted_collection: sorted list of integers
        item: item value to search

    Returns:
        int: The index of the found item, or None if the item is not found.
    Examples:
    >>> interpolation_search([1, 2, 3, 4, 5], 2)
    1
    >>> interpolation_search([1, 2, 3, 4, 5], 4)
    3
    >>> interpolation_search([1, 2, 3, 4, 5], 6) is None
    True
    >>> interpolation_search([], 1) is None
    True
    >>> interpolation_search([100], 100)
    0
    >>> interpolation_search([1, 2, 3, 4, 5], 0) is None
    True
    >>> interpolation_search([1, 2, 3, 4, 5], 7) is None
    True
    >>> interpolation_search([1, 2, 3, 4, 5], 2)
    1
    >>> interpolation_search([1, 2, 3, 4, 5], 0) is None
    True
    >>> interpolation_search([1, 2, 3, 4, 5], 7) is None
    True
    >>> interpolation_search([1, 2, 3, 4, 5], 2)
    1
    >>> interpolation_search([5, 5, 5, 5, 5], 3) is None
    True
    """
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        # avoid divided by 0 during interpolation
        if sorted_collection[left] == sorted_collection[right]:
            if sorted_collection[left] == item:
                return left
            return None

        point = left + ((item - sorted_collection[left]) * (right - left)) // (
            sorted_collection[right] - sorted_collection[left]
        )

        # out of range check
        if point < 0 or point >= len(sorted_collection):
            return None

        current_item = sorted_collection[point]
        if current_item == item:
            return point
        if point < left:
            right = left
            left = point
        elif point > right:
            left = right
            right = point
        elif item < current_item:
            right = point - 1
        else:
            left = point + 1
    return None


def interpolation_search_by_recursion(
    sorted_collection: list[int], item: int, left: int = 0, right: int | None = None
) -> int | None:
    """Pure implementation of interpolation search algorithm in Python by recursion
    Be careful collection must be ascending sorted, otherwise result will be
    unpredictable
    First recursion should be started with left=0 and right=(len(sorted_collection)-1)

    Args:
        sorted_collection: some sorted collection with comparable items
        item: item value to search
        left: left index in collection
        right: right index in collection

    Returns:
        index of item in collection or None if item is not present

    Examples:
    >>> interpolation_search_by_recursion([0, 5, 7, 10, 15], 0)
    0
    >>> interpolation_search_by_recursion([0, 5, 7, 10, 15], 15)
    4
    >>> interpolation_search_by_recursion([0, 5, 7, 10, 15], 5)
    1
    >>> interpolation_search_by_recursion([0, 5, 7, 10, 15], 100) is None
    True
    >>> interpolation_search_by_recursion([5, 5, 5, 5, 5], 3) is None
    True
    """
    if right is None:
        right = len(sorted_collection) - 1
    # avoid divided by 0 during interpolation
    if sorted_collection[left] == sorted_collection[right]:
        if sorted_collection[left] == item:
            return left
        return None

    point = left + ((item - sorted_collection[left]) * (right - left)) // (
        sorted_collection[right] - sorted_collection[left]
    )

    # out of range check
    if point < 0 or point >= len(sorted_collection):
        return None

    if sorted_collection[point] == item:
        return point
    if point < left:
        return interpolation_search_by_recursion(sorted_collection, item, point, left)
    if point > right:
        return interpolation_search_by_recursion(sorted_collection, item, right, left)
    if sorted_collection[point] > item:
        return interpolation_search_by_recursion(
            sorted_collection, item, left, point - 1
        )
    return interpolation_search_by_recursion(sorted_collection, item, point + 1, right)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
