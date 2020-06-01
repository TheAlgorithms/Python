"""

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3

Output: [5,6,7,1,2,3,4]

Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

"""

def rotate(nums, rotate_index):
    """
    :type nums: List[int]
    :type rotate_index: int
    :return: List[int]
    """
    nums[:] = nums[len(nums) - rotate_index:] + nums[:len(nums) - rotate_index]
    return nums