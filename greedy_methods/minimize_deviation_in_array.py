"""
You are given an array nums of n positive integers.

You can perform two types of operations on any
element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation
on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation
on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between
any two elements in the array.

Return the minimum deviation the array can have after performing
some number of operations.
"""

from heapq import heapify, heappop, heappush


class Solution:
    def minimum_deviation(self, nums: list[int]) -> int:
        """
        Function to find the minimum deviation of an array after performing operations.

        Args:
            nums (List[int]): A list of positive integers.

        Returns:
            temp_mindeviation (int): The minimum deviation of array after operations.

        Examples:
            >>> solution = Solution()
            >>> solution.minimum_deviation([1, 2, 3, 4])
            1
            >>> solution.minimum_deviation([5, 10, 20, 30, 30])
            5
            >>> solution.minimum_deviation([8, 8, 8, 8, 8])
            0
        """
        heapque = [-n * 2 if n % 2 else -n for n in nums]
        heapify(heapque)
        temp_min = -min(heapque, key=lambda num: -num)
        temp_mindeviation = -heapque[0] - temp_min

        while heapque and heapque[0] % 2 == 0:
            n = heappop(heapque) // 2
            heappush(heapque, n)
            temp_min = min(temp_min, -n)
            temp_mindeviation = min(temp_mindeviation, -heapque[0] - temp_min)

        return temp_mindeviation


if __name__ == "__main__":
    import doctest

    doctest.testmod()
