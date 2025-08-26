"""
Given an integer array nums and a non-negative integer k, rotate
nums to the right by k places.

LeetCode Link: https://leetcode.com/problems/rotate-array/

4 Different Implementations
"""

from collections import deque


# Time: O(n * k)     Space: O(1)
def rotate_array_nk_time(nums: list[int], k: int) -> list[int]:
    """
    Takes the last k integers, and one by one, inserts them at the start of the array.

    >>> rotate_array_nk_time([-1, 7, 25, 6], 3)
    [7, 25, 6, -1]
    >>> rotate_array_nk_time([4, 14, 2, -6, -9, 1, -37], 2)
    [1, -37, 4, 14, 2, -6, -9]
    >>> rotate_array_nk_time([19, -2, 5, 5, 11], 5)
    [19, -2, 5, 5, 11]
    >>> rotate_array_nk_time([1, 2, 4, 1, 2, 4], 3)
    [1, 2, 4, 1, 2, 4]
    >>> rotate_array_nk_time([8, -7, 22, -6], 9)
    [-6, 8, -7, 22]
    """

    length = len(nums)
    k = k % length
    curr = length - k
    for i in range(k):
        dummy = nums[curr]
        for j in range(curr - 1, i - 1, -1):
            nums[j + 1] = nums[j]

        nums[i] = dummy
        curr += 1

    return nums


# Time: O(n)     Space: O(n)
def rotate_array_n_space(nums: list[int], k: int) -> list[int]:
    """
    Creates new array consisting of last k integers in nums followed by remaining
    integers in nums.

    >>> rotate_array_n_space([-1, 7, 25, 6], 3)
    [7, 25, 6, -1]
    >>> rotate_array_n_space([4, 14, 2, -6, -9, 1, -37], 2)
    [1, -37, 4, 14, 2, -6, -9]
    >>> rotate_array_n_space([19, -2, 5, 5, 11], 5)
    [19, -2, 5, 5, 11]
    >>> rotate_array_n_space([1, 2, 4, 1, 2, 4], 3)
    [1, 2, 4, 1, 2, 4]
    >>> rotate_array_n_space([8, -7, 22, -6], 9)
    [-6, 8, -7, 22]
    """

    length = len(nums)
    k = k % length

    return nums[length - k :] + nums[: length - k]


# Time: O(n)     Space: O(k)
def rotate_array_k_space(nums: list[int], k: int) -> list[int]:
    """
    Uses a deque buffer of size k to shift each integer in nums by k places.

    >>> rotate_array_k_space([-1, 7, 25, 6], 3)
    [7, 25, 6, -1]
    >>> rotate_array_k_space([4, 14, 2, -6, -9, 1, -37], 2)
    [1, -37, 4, 14, 2, -6, -9]
    >>> rotate_array_k_space([19, -2, 5, 5, 11], 5)
    [19, -2, 5, 5, 11]
    >>> rotate_array_k_space([1, 2, 4, 1, 2, 4], 3)
    [1, 2, 4, 1, 2, 4]
    >>> rotate_array_k_space([8, -7, 22, -6], 9)
    [-6, 8, -7, 22]
    """

    length = len(nums)
    k = k % length
    buffer = deque(nums[length - k :])
    for i in range(length):
        buffer.append(nums[i])
        nums[i] = buffer.popleft()

    return nums


# Time: O(n)     Space: O(1)
def rotate_array_constant_space(nums: list[int], k: int) -> list[int]:
    """
    Reverse whole array. Then reverse first k elements. Then reverse remaining elements.

    >>> rotate_array_constant_space([-1, 7, 25, 6], 3)
    [7, 25, 6, -1]
    >>> rotate_array_constant_space([4, 14, 2, -6, -9, 1, -37], 2)
    [1, -37, 4, 14, 2, -6, -9]
    >>> rotate_array_constant_space([19, -2, 5, 5, 11], 5)
    [19, -2, 5, 5, 11]
    >>> rotate_array_constant_space([1, 2, 4, 1, 2, 4], 3)
    [1, 2, 4, 1, 2, 4]
    >>> rotate_array_constant_space([8, -7, 22, -6], 9)
    [-6, 8, -7, 22]
    """

    length = len(nums)
    k = k % length

    def reverse(left: int, right: int) -> None:
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1

    reverse(0, length - 1)
    reverse(0, k - 1)
    reverse(k, length - 1)

    return nums


if __name__ == "__main__":
    import doctest

    doctest.testmod()
