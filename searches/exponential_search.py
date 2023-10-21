"""
This is pure Python implementation of exponential search.

Resources used:
https://en.wikipedia.org/wiki/Exponential_search

For doctests run following command:
python3 -m doctest -v expontial_search.py

For manual testing run:
python3 expontial_search.py
"""

def binary_search(arr, left, right, target) -> int:
    """
    Binary search function to find the position of the target in the array.

    Args:
        arr (list): The sorted array to search in.
        left (int): The left index of the subarray to search.
        right (int): The right index of the subarray to search.
        target (int): The target element to find.

    Returns:
        int: The index of the target element if found, or -1 if not found.
    """
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr, n, x) -> int:
    """
    Exponential search function to find the position of the target in the array.

    Args:
        arr (list): The sorted array to search in.
        n (int): The number of elements in the array.
        x (int): The target element to find.

    Returns:
        int: The index of the target element if found, or -1 if not found.
    """
    if arr[0] == x:
        return 0

    i = 1
    while i < n and arr[i] <= x:
        i *= 2

    return binary_search(arr, i // 2, min(i, n - 1), x)

# Driver Code
arr = [2, 3, 4, 10, 40]
n = len(arr)
x = 10
result = exponential_search(arr, n, x)
if result == -1:
    print("Element not found in the array")
else:
    print(f"Element is present at index {result}")
