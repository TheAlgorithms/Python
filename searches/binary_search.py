def binary_search(sorted_collection: list[int], item: int) -> int:
    """Pure implementation of a binary search algorithm in Python

    Be careful collection must be ascending sorted otherwise, the result will be
    unpredictable

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of the found item or -1 if the item is not found

    Examples:
    >>> binary_search([0, 5, 7, 10, 15], 0)
    0
    >>> binary_search([0, 5, 7, 10, 15], 15)
    4
    >>> binary_search([0, 5, 7, 10, 15], 5)
    1
    >>> binary_search([0, 5, 7, 10, 15], 6)
    -1
    >>> binary_search([1, 2, 3, 3, 3, 4], 3)  # Updated to find first occurrence
    2
    """
    if list(sorted_collection) != sorted(sorted_collection):
        raise ValueError("sorted_collection must be sorted in ascending order")
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = left + (right - left) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            if midpoint > 0 and sorted_collection[midpoint - 1] == item:
                right = midpoint - 1  # Keep searching left
            else:
                return midpoint
        elif item < current_item:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1


def binary_search_with_duplicates(sorted_collection: list[int], item: int) -> list[int]:
    """Pure implementation of a binary search algorithm in Python that supports
    duplicates.

    Resources used:
    https://stackoverflow.com/questions/13197552/using-binary-search-with-sorted-array-with-duplicates

    The collection must be sorted in ascending order; otherwise the result will be
    unpredictable. If the target appears multiple times, this function returns a
    list of all indexes where the target occurs. If the target is not found,
    this function returns an empty list.

    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search for
    :return: a list of indexes where the item is found (empty list if not found)

    Examples:
    >>> binary_search_with_duplicates([0, 5, 7, 10, 15], 0)
    [0]
    >>> binary_search_with_duplicates([0, 5, 7, 10, 15], 15)
    [4]
    >>> binary_search_with_duplicates([1, 2, 2, 2, 3], 2)
    [1, 2, 3]
    >>> binary_search_with_duplicates([1, 2, 2, 2, 3], 4)
    []
    >>> binary_search_with_duplicates([1, 1, 1, 1], 1)  # Example of all same
    [0, 1, 2, 3]
    """
    if list(sorted_collection) != sorted(sorted_collection):
        raise ValueError("sorted_collection must be sorted in ascending order")

    def lower_bound(sorted_collection: list[int], item: int) -> int:
        """
        Returns the index of the first element greater than or equal to the item.

        :param sorted_collection: The sorted list to search.
        :param item: The item to find the lower bound for.
        :return: The index where the item can be inserted while maintaining order.
        """
        left = 0
        right = len(sorted_collection)
        while left < right:
            midpoint = left + (right - left) // 2
            current_item = sorted_collection[midpoint]
            if current_item < item:
                left = midpoint + 1
            else:
                right = midpoint
        return left

    def upper_bound(sorted_collection: list[int], item: int) -> int:
        """
        Returns the index of the first element strictly greater than the item.

        :param sorted_collection: The sorted list to search.
        :param item: The item to find the upper bound for.
        :return: The index where the item can be inserted after all existing instances.
        """
        left = 0
        right = len(sorted_collection)
        while left < right:
            midpoint = left + (right - left) // 2
            current_item = sorted_collection[midpoint]
            if current_item <= item:
                left = midpoint + 1
            else:
                right = midpoint
        return left

    left = lower_bound(sorted_collection, item)
    right = upper_bound(sorted_collection, item)

    if left == len(sorted_collection) or sorted_collection[left] != item:
        return []
    return list(range(left, right))
    