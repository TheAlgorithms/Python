"""
Given an Array of size N and a value K,
around which we need to right rotate the array.
How do you quickly print the right rotated array?

Input: Array[] = {1, 3, 5, 7, 9}, K = 2.
Output: 7 9 1 3 5
Explanation:
After 1st rotation – {9, 1, 3, 5, 7}After 2nd rotation – {7, 9, 1, 3, 5}
"""


def right_rotate(arr, k):
    n = len(arr)
    k = k % n
    arr = arr[n - k :] + arr[: n - k]
    return arr


# Test the function with the provided input
print(right_rotate([1, 3, 5, 7, 9], 2))  # Expected output: [7, 9, 1, 3, 5]
