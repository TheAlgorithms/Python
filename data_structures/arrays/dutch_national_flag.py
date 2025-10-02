def dutch_national_flag(arr):
    """
    Sorts an array containing only 0s, 1s and 2s

    Args:
        arr(list): The input array (containing only 0s, 1s and 2s)

    Returns:
        list: Sorted array
    """

    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


if __name__ == "__main__":
    arr = [2, 0, 2, 1, 2, 0, 1]
    print("Sorted array: ", dutch_national_flag(arr))
