"""
This module implements an algorithm to find the maximum element in all possible
windows of size k in an array using a deque for O(n) time complexity.

For example:
[1, 3, -1, -3, 5, 3, 6, 7], k=3 -> [3, 3, 5, 5, 6, 7]
Window position        Max
---------------       -----
[1  3  -1] -3  5  3  6  7   ->  3
 1 [3  -1  -3] 5  3  6  7   ->  3
 1  3 [-1  -3  5] 3  6  7   ->  5
 1  3  -1 [-3  5  3] 6  7   ->  5
 1  3  -1  -3 [5  3  6] 7   ->  6
 1  3  -1  -3  5 [3  6  7]  ->  7

Time Complexity: O(n)
Space Complexity: O(k)
"""

from collections import deque
from typing import List


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    """
    Find maximum elements in all possible windows of size k.
    
    Args:
        nums: List of integers
        k: Size of the sliding window
        
    Returns:
        List of maximum elements from each window
        
    Examples:
        >>> max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
        [3, 3, 5, 5, 6, 7]
        >>> max_sliding_window([1], 1)
        [1]
        >>> max_sliding_window([1, -1], 1)
        [1, -1]
        >>> max_sliding_window([1, 2, 3, 4], 4)
        [4]
    """
    if not nums or k <= 0:
        return []
    if k == 1:
        return nums
    
    result = []
    # Deque will store indices of potential maximum values
    window = deque()
    
   
    for i in range(k):
        
        while window and nums[i] >= nums[window[-1]]:
            window.pop()
        window.append(i)
    
   
    for i in range(k, len(nums)):
        # First element in deque is the largest in previous window
        result.append(nums[window[0]])
        
        # Remove elements outside current window
        while window and window[0] <= i - k:
            window.popleft()
            
        # Remove smaller elements from back
        while window and nums[i] >= nums[window[-1]]:
            window.pop()
            
        window.append(i)
    
    # Add maximum element of last window
    result.append(nums[window[0]])
    
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()