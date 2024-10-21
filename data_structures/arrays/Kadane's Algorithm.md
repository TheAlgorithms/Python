---
title: "Kadane's Algorithm"
sidebar_label: "Introduction to Kadane's Algorithm"
description: "Kadane's Algorithm efficiently finds the maximum sum of a contiguous subarray. It is a fundamental algorithm for solving problems involving subarray sums."
tags: [basic-dsa, data-structures, Kadane's Algorithm]
---

### Definition:

Kadane’s Algorithm is used to find the **maximum sum of a contiguous subarray** within a given array. It efficiently handles both positive and negative numbers and works in **O(n)** time, making it a crucial tool for solving optimization problems related to arrays.

### Characteristics:

- **Linear Time Complexity**:

  - The algorithm processes the array in a single pass, ensuring **O(n)** time complexity.

- **Handles Negative Numbers**:

  - It can deal with arrays containing both positive and negative numbers, ensuring the correct maximum sum is found.

- **Space Complexity: O(1)**
  - Only a few extra variables are used, making the space usage constant.

### Python Implementation:

```python
def max_subarray(nums):
    """
    Find the maximum sum of a contiguous subarray using Kadane's Algorithm.
    Args:
        nums (list): List of integers.
    Returns:
        int: Maximum sum of any contiguous subarray.
    """
    max_sum = curr_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

# Example usage
if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_subarray(arr)
    print("Maximum subarray sum:", result)  # Output: 6
```
