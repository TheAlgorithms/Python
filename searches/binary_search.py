def binary_search(sorted_collection: list[int], item: int) -> int:
    """
    Binary Search Algorithm (Iterative Implementation)

    Searches for an item in a sorted collection using the binary search technique.
    Binary search works by repeatedly dividing the search interval in half.

    Requirements
    ------------
    The input collection must be sorted in ascending order.

    Parameters
    ----------
    sorted_collection : list[int]
        A sorted list of comparable elements.
    item : int
        The value to search for.

    Returns
    -------
    int
        Index of the found item or -1 if the item is not present.

    Time Complexity
    ---------------
    O(log n)

    Space Complexity
    ----------------
    O(1)

    Examples
    --------
    >>> binary_search([0, 5, 7, 10, 15], 0)
    0
    >>> binary_search([0, 5, 7, 10, 15], 15)
    4
    >>> binary_search([0, 5, 7, 10, 15], 5)
    1
    >>> binary_search([0, 5, 7, 10, 15], 6)
    -1
    """
    if list(sorted_collection) != sorted(sorted_collection):
        raise ValueError("sorted_collection must be sorted in ascending order")
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = left + (right - left) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        elif item < current_item:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1
