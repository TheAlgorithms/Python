"""
Sort an array into a wave array using an optimized approach.
A wave array is an array where
arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4]...

Reference: https://www.geeksforgeeks.org/sort-array-wave-form-2

Author : Arunkumar (Arunsiva003)
Date: 9th October 2023
"""


def sort_into_wave_optimized(arr: list[int]) -> list[int]:
    """
    Args:
        arr : The input array to be sorted into a wave array.

    Returns:
        list : The sorted wave array.

    Examples:
        >>> sort_into_wave_optimized([1, 2, 3, 4, 5])
        [2, 1, 4, 3, 5]
        >>> sort_into_wave_optimized([4, 2, 8, 1, 6, 3])
        [2, 1, 8, 3, 6, 4]
    """
    n = len(arr)

    for i in range(0, n, 2):
        # If the current element is smaller than the previous element (i-1),
        # swap them to make arr[i] <= arr[i-1]
        if i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]

        # If the current element is smaller than the next element (i+1),
        # swap them to make arr[i] <= arr[i+1]
        if i < n - 1 and arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


if __name__ == "__main__":
    input_arr = [1, 2, 3, 4, 5]
    print("Sorted Wave Array:", sort_into_wave_optimized(input_arr))
