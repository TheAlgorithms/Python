"""
Kadane's Algorithm is an efficient algorithm used to find the maximum subarray sum in a given array of integers. The algorithm's key insight is to keep track of the maximum subarray sum ending at each position in the array. By doing so, it avoids unnecessary recalculations and efficiently finds the maximum subarray sum.
"""
"""
Here's how Kadane's algorithm works:

1. Initialize two variables, max_current and max_global, to the first element of the array.
2. Iterate through the array, starting from the second element.
3. For each element, update max_current to be the maximum of the current element and the sum of max_current and the current element.
4. Update max_global to be the maximum of max_global and max_current.
5.Repeat steps 3-4 until you've traversed the entire array.
6.max_global will contain the maximum subarray sum.

"""
def kadane_algorithm(arr:list[int])-> int:
"""
    Args:
        arr: The array of integers

    Returns:
        int: maximum sum of the subarray
"""
"""
Some test cases
 kadane_algoitrm([-2, 1, -3, 4, -1, 2, 1, -5, 4])
 >>> 6
 kadane_algoitrm([1, -2, 3, -4, 5])
 >>> 5
 kadane_algoitrm([5, -2, 7, -6, 4])
 >>>10

"""

    max_current = max_global = arr[0]
    
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        max_global = max(max_global, max_current)
    
    return max_global
  
  
  if __name__ == "__main__":
    import doctest

    doctest.testmod()
