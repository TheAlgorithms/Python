def max_sum_subarray(arr, k):
    # Edge case: if the window size is greater than the array length
    if len(arr) < k:
        return None

    # Compute the sum of the first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window from left to right
    for i in range(k, len(arr)):
        # Subtract the element going out of the window and add the new element coming into the window
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


# Example usage:

# Example 1: Larger array
arr1 = [4, 3, 10, 2, 8, 6, 7, 1, 9]
k1 = 4
print(
    "Example 1: Maximum sum of subarray of length", k1, "is", max_sum_subarray(arr1, k1)
)

# Example 2: All elements are negative
arr2 = [-2, -3, -1, -5, -6]
k2 = 2
print(
    "Example 2: Maximum sum of subarray of length", k2, "is", max_sum_subarray(arr2, k2)
)

# Example 3: Array with all elements equal
arr3 = [5, 5, 5, 5, 5, 5]
k3 = 3
print(
    "Example 3: Maximum sum of subarray of length", k3, "is", max_sum_subarray(arr3, k3)
)

# Example 4: Small array
arr4 = [1, 2]
k4 = 2
print(
    "Example 4: Maximum sum of subarray of length", k4, "is", max_sum_subarray(arr4, k4)
)

# Example 5: k greater than the array length
arr5 = [7, 8, 9]
k5 = 5
print(
    "Example 5: Maximum sum of subarray of length", k5, "is", max_sum_subarray(arr5, k5)
)
