"""
Problem Statement- Find the sum of contiguous subarray having the largest sum. 
Example- [6,9,-1,3,-7,-5,10]   Output- 17 
Time Complexity- O(n) 
Approach- To look for all positive contiguous segments of the array(s).
And keep track of maximum sum contiguous segment among all positive segments(res).
Each time compare s with res and update res if it is greater than res 
"""


# Function to find the maximum contiguous subarray
def max_subarray_sum(nums: list) -> int:
    """
    >>> max_subarray_sum([6 , 9, -1, 3, -7, -5, 10])
    17
    """
    if not nums:
        return 0
    n = len(nums)

    res, s, s_pre = nums[0], nums[0], nums[0]
    for i in range(1, n):
        s = max(nums[i], s_pre + nums[i])
        s_pre = s
        res = max(res, s)
    return res


# Driver function to check the above function
if __name__ == "__main__":
    nums = [6, 9, -1, 3, -7, -5, 10]
    print(max_subarray_sum(nums))
