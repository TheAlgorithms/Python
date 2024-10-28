
def max_subarray_circular(nums: list[int]) -> int:
    """
    Find the maximum possible sum of a subarray in a circular array.
    
    Args:
        nums: List of integers representing the circular array
        
    Returns:
        Maximum sum possible considering the array as circular
        
    Examples:
        >>> max_subarray_circular([1, -2, 3, -2])
        3
        >>> max_subarray_circular([5, -3, 5])
        10
        >>> max_subarray_circular([-3, -2, -3])
        -2
    """
    if not nums:
        return 0
        
    # Case 1: Get the maximum sum using Kadane's algorithm
    def kadane(arr):
        curr_sum = max_sum = arr[0]
        for num in arr[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum
    
    # Case 1: The maximum sum without wrapping
    max_straight = kadane(nums)
    
    # If all numbers are negative, return the maximum straight sum
    if max_straight < 0:
        return max_straight
    
    # Case 2: The maximum sum with wrapping
    # This can be found by subtracting the minimum sum subarray from total sum
    total = sum(nums)
    # Invert the array and find the maximum sum to get the minimum sum
    max_inverted = kadane([-x for x in nums])
    max_wrapped = total + max_inverted  # Adding because we inverted the numbers
    
    return max(max_straight, max_wrapped)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

"""
This module implements an algorithm to find the maximum sum of a subarray in a circular array.
A circular array means the array can wrap around itself.

For example:
[1, -2, 3, -2] -> Maximum sum is 3
[5, -3, 5] -> Maximum sum is 10 because [5, 5] is possible with wrapping
[-3, -2, -3] -> Maximum sum is -2

Time Complexity: O(n)
Space Complexity: O(1)
"""