"""

Problem: Find First and Last Position of Element in Sorted Array
Description:
Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
Leetcode ref:
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

"""


def search_range(nums: list[int], target: int) -> list[int]:
    """
    >>> search_range([5,7,7,8,8,10],8)
    [3, 4]
    >>> search_range([5,7,7,8,8,10],6)
    [-1, -1]
    >>> search_range([],3)
    [-1, -1]
    >>> search_range([5,7,8,9,9],7)
    [1, 1]
    """

    def binary_search(nums: list, target: int, left: bool) -> int:
        """
        >>> binary_search([1, 2, 3, 4, 5], 3, leftmost=True)
        2
         >>> binary_search([1, 2, 3, 4, 5], 0, leftmost=False)
        -1
        """

        low, high = 0, len(nums) - 1
        index = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid
                if left:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return index

    left_index = binary_search(nums, target, left=True)
    right_index = binary_search(nums, target, left=False)

    return [left_index, right_index]


if __name__ == "__main__":
    from doctest import testmod

    testmod()