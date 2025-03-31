"""
Given an integer array, the task is to find the maximum product of any subarray.
Input: arr[] = {-1, -3, -10, 0, 60}
Output: 60
Explanation: The subarray with maximum product is {60}.
"""


def max_product(arr):
    result = 0

    for x in range(len(arr)):
        current_product = 1
        for y in range(x, len(arr)):
            current_product *= arr[y]
            result = max(result, current_product)
    return result


# Test the function with the provided input
print(max_product([-1, -3, -10, 0, 60]))  # Expected output: 60
