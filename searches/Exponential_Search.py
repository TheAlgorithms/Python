# Python program to perform Exponential Search
from bisect import bisect_left


# Binary search function
def binary_search(arr, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Exponential search function
def exponential_search(arr, target):
    n = len(arr)

    # If the target is at the first position
    if arr[0] == target:
        return 0

    # Find the range for binary search by repeatedly doubling the index
    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    # Perform binary search within the found range
    return binary_search(arr, i // 2, min(i, n - 1), target)


# Example usage
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40, 50, 60, 70, 80, 90, 100]
    target = 10

    result = exponential_search(arr, target)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the array")
