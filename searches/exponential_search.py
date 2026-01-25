"""
Exponential Search Algorithm

Time Complexity:
- Best Case: O(1)
- Average/Worst Case: O(log i), where i is the index of the first element >= target

Use Case:
Efficient for searching in sorted arrays where the target is near the beginning.

Author: Michael Alexander Montoya
"""


def exponential_search(arr, target):
    if len(arr) == 0:
        return -1

    if arr[0] == target:
        return 0

    # Find range for binary search by repeated doubling
    index = 1
    while index < len(arr) and arr[index] <= target:
        index *= 2

    # Perform binary search in the found range
    return binary_search(arr, target, index // 2, min(index, len(arr) - 1))


def binary_search(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Example usage:
if __name__ == "__main__":
    array = [1, 3, 5, 7, 9, 13, 17, 21, 24, 27, 30]
    target = 13
    result = exponential_search(array, target)
    print(f"Target {target} found at index: {result}")
