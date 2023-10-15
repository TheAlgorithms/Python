from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        Count the number of elements smaller than each element in the input list.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            List[int]: A list containing the count of elements smaller than each element in the input list.

        Examples:
            >>> solution = Solution()
            >>> solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3])
            [4, 0, 1, 1, 3]
            >>> solution.smallerNumbersThanCurrent([6, 5, 4, 8])
            [2, 1, 0, 3]
            >>> solution.smallerNumbersThanCurrent([7, 7, 7, 7])
            [0, 0, 0, 0]
        """
        count = [0] * 101
        res = []

        for num in nums:
            count[num] += 1

        for i in range(len(nums)):
            total = sum(count[:nums[i]])
            res.append(total)

        return res