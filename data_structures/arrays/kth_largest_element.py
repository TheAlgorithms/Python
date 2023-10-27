"""
Given an array of integers and an integer k, find the kth largest element in the array.

https://stackoverflow.com/questions/251781
"""


def partition(arr: list[int], low: int, high: int) -> int:
    """
    Partitions list based on the pivot element.

    This function rearranges the elements in the input list 'elements' such that
    all elements greater than or equal to the chosen pivot are on the right side
    of the pivot, and all elements smaller than the pivot are on the left side.

    Args:
        arr: The list to be partitioned
        low: The lower index of the list
        high: The higher index of the list

    Returns:
        int: The index of pivot element after partitioning

        Examples:
        >>> partition([3, 1, 4, 5, 9, 2, 6, 5, 3, 5], 0, 9)
        4
        >>> partition([7, 1, 4, 5, 9, 2, 6, 5, 8], 0, 8)
        1
        >>> partition(['apple', 'cherry', 'date', 'banana'], 0, 3)
        2
        >>> partition([3.1, 1.2, 5.6, 4.7], 0, 3)
        1
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def kth_largest_element(arr: list[int], position: int) -> int:
    """
    Finds the kth largest element in a list.
    Should deliver similar results to:
    ```python
    def kth_largest_element(arr, position):
        return sorted(arr)[-position]
    ```

    Args:
        nums: The list of numbers.
        k: The position of the desired kth largest element.

    Returns:
        int: The kth largest element.

    Examples:
        >>> kth_largest_element([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 3)
        5
        >>> kth_largest_element([2, 5, 6, 1, 9, 3, 8, 4, 7, 3, 5], 1)
        9
        >>> kth_largest_element([2, 5, 6, 1, 9, 3, 8, 4, 7, 3, 5], -2)
        Traceback (most recent call last):
        ...
        ValueError: Invalid value of 'position'
        >>> kth_largest_element([9, 1, 3, 6, 7, 9, 8, 4, 2, 4, 9], 110)
        Traceback (most recent call last):
        ...
        ValueError: Invalid value of 'position'
        >>> kth_largest_element([1, 2, 4, 3, 5, 9, 7, 6, 5, 9, 3], 0)
        Traceback (most recent call last):
        ...
        ValueError: Invalid value of 'position'
        >>> kth_largest_element(['apple', 'cherry', 'date', 'banana'], 2)
        'cherry'
        >>> kth_largest_element([3.1, 1.2, 5.6, 4.7,7.9,5,0], 2)
        5.6
        >>> kth_largest_element([-2, -5, -4, -1], 1)
        -1
        >>> kth_largest_element([], 1)
        -1
        >>> kth_largest_element([3.1, 1.2, 5.6, 4.7, 7.9, 5, 0], 1.5)
        Traceback (most recent call last):
        ...
        ValueError: The position should be an integer
        >>> kth_largest_element((4, 6, 1, 2), 4)
        Traceback (most recent call last):
        ...
        TypeError: 'tuple' object does not support item assignment
    """
    if not arr:
        return -1
    if not isinstance(position, int):
        raise ValueError("The position should be an integer")
    if not 1 <= position <= len(arr):
        raise ValueError("Invalid value of 'position'")
    low, high = 0, len(arr) - 1
    while low <= high:
        if low > len(arr) - 1 or high < 0:
            return -1
        pivot_index = partition(arr, low, high)
        if pivot_index == position - 1:
            return arr[pivot_index]
        elif pivot_index > position - 1:
            high = pivot_index - 1
        else:
            low = pivot_index + 1
    return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
