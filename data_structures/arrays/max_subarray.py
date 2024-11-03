"""
Input: arr[] = {2, 3, -8, 7, -1, 2, 3}
Output: 11
Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.

Input: arr[] = {-2, -4}
Output: –2
Explanation: The subarray {-2} has the largest sum -2.

Input: arr[] = {5, 4, 1, 7, 8}
Output: 25
Explanation: The subarray {5, 4, 1, 7, 8} has the largest sum 25.
"""


def max_subarray(arr):
    result = arr[0]

    for x in range(len(arr)):
        current_sum = 0
        for y in range(x, len(arr)):
            current_sum += arr[y]
            result = max(result, current_sum)
    return result


# Test the function with the provided inputs
print(max_subarray([2, 3, -8, 7, -1, 2, 3]))  # Expected output: 11
print(max_subarray([-2, -4]))  # Expected output: -2
print(max_subarray([5, 4, 1, 7, 8]))  # Expected output: 25
