def rotated_binary_search(arr: list[int], key: int) -> int:
    """
    Performs binary search on a rotated sorted list.

    Parameters:
    arr (list[int]): A rotated sorted list of integers.
    key (int): The element to search for.

    Returns:
    int: The index of the key in the list, or -1 if the key is not found.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if the mid element is the key
        if arr[mid] == key:
            return mid

        # Check which side is sorted
        if arr[low] <= arr[mid]:  # Left side is sorted
            if arr[low] <= key < arr[mid]:  # Key is in the sorted left side
                high = mid - 1
            else:  # Key is in the right side
                low = mid + 1
        else:  # Right side is sorted
            if arr[mid] < key <= arr[high]:  # Key is in the sorted right side
                low = mid + 1
            else:  # Key is in the left side
                high = mid - 1

    return -1  # Key not found
