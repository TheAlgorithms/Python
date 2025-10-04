"""
peak_mountain_array.py
Author: Taha Zulfiquar
Description: Finds the peak index in a mountain array using binary search.
"""


def peak_mountain(arr):
    start, end = 0, len(arr) - 1

    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return start


if __name__ == "__main__":
    arr = [1, 2, 3, 5, 7, 8, 6, 3, 2]
    peak_index = peak_mountain(arr)
    print("The peak index is:", peak_index)
