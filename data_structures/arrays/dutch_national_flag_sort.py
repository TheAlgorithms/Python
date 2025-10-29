"""
Sorts an array consisting of 0s, 1s, and 2s using the Dutch National Flag algorithm.

This algorithm sorts the array in a single pass with O(n) time complexity and O(1) space complexity.
It uses three pointers to partition the array into sections for 0s, 1s, and 2s.

https://en.wikipedia.org/wiki/Dutch_national_flag_problem
"""

def dutch_flag_sort(arr: list[int]) -> None:
    """
    Sorts an array of 0s, 1s, and 2s in-place.

    Args:
        arr: The list to sort, containing only 0, 1, or 2.

    Returns:
        None

    Raises:
        ValueError: If the array contains values other than 0, 1, or 2.

    Examples:
        >>> arr = [2, 0, 2, 1, 1, 0]
        >>> dutch_flag_sort(arr)
        >>> arr
        [0, 0, 1, 1, 2, 2]
        >>> arr = [2, 0, 1]
        >>> dutch_flag_sort(arr)
        >>> arr
        [0, 1, 2]
        >>> arr = []
        >>> dutch_flag_sort(arr)
        >>> arr
        []
        >>> arr = [1]
        >>> dutch_flag_sort(arr)
        >>> arr
        [1]
        >>> arr = [0, 0, 0]
        >>> dutch_flag_sort(arr)
        >>> arr
        [0, 0, 0]
        >>> arr = [2, 2, 2]
        >>> dutch_flag_sort(arr)
        >>> arr
        [2, 2, 2]
        >>> arr = [1, 1, 1]
        >>> dutch_flag_sort(arr)
        >>> arr
        [1, 1, 1]
        >>> arr = [0, 1, 2, 0, 1, 2]
        >>> dutch_flag_sort(arr)
        >>> arr
        [0, 0, 1, 1, 2, 2]
        >>> arr = [2, 1, 0, 2, 1, 0]
        >>> dutch_flag_sort(arr)
        >>> arr
        [0, 0, 1, 1, 2, 2]
        >>> arr = [3]
        >>> dutch_flag_sort(arr)
        Traceback (most recent call last):
        ...
        ValueError: Array contains invalid value: 3
        >>> arr = [-1, 0, 1]
        >>> dutch_flag_sort(arr)
        Traceback (most recent call last):
        ...
        ValueError: Array contains invalid value: -1
        >>> arr = [0, 1, 2, 3]
        >>> dutch_flag_sort(arr)
        Traceback (most recent call last):
        ...
        ValueError: Array contains invalid value: 3
        >>> arr = (2, 0, 1)
        >>> dutch_flag_sort(arr)
        Traceback (most recent call last):
        ...
        TypeError: 'tuple' object does not support item assignment
        >>> arr = [2, 0, '1']
        >>> dutch_flag_sort(arr)
        Traceback (most recent call last):
        ...
        ValueError: Array contains invalid value: 1
    """
    if not arr:
        return
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            raise ValueError(f"Array contains invalid value: {arr[mid]}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()



does it require any improvements? 
