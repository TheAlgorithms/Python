def binary_insertion_sort(collection: list) -> list:
    """A Python implementation of insertion sort based on binary search
    :param collection: a mutable collection of comparable items
    :return: the same collection ordered by ascending

    Examples:
    >>> quick_sort([37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54])
    [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]
    >>> quick_sort([])
    []
    >>> quick_sort([-2, 5, 0, -45, 85, 12])
    [-45, -2, 0, 5, 12, 85]
    """

    """
    The binary search algorithm is responsible for search the correct
    position for insertion
    """

    def binary_search(arr: list, val: int, start: int, end: int) -> int:
        while start < end:
            mid = start + int((end - start) / 2)
            if arr[mid] > val:
                end = mid - 1
            elif arr[mid] < val:
                start = mid + 1
            else:
                return mid
        if start == end:
            if arr[start] > val:
                return start
            else:
                return start + 1
        return start

    """
    The insertion sort is responsible for iterating through the list and find
     correct position
    for the item
    """

    def insertion_sort(arr) -> list:
        for i in range(1, len(arr)):
            j = binary_search(arr, arr[i], 0, i - 1)
            arr = arr[:j] + [arr[i]] + arr[j:i] + arr[i + 1 :]
        return arr

    if len(collection) == 0:
        return collection

    return insertion_sort(collection)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(binary_insertion_sort(unsorted))
