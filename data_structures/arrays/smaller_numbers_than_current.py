# Count the number of elements smaller than each element in the input list. Reference :
# https://cassandriel.medium.com/leetcode-1365-how-many-numbers-are-smaller-than-the-current-number-1c8354ee5d84


class SmallerNumbersThanCurrent:
    def smaller_numbers_than_current(self, nums: list[int]) -> list[int]:
        """
        Count the number of elements smaller than each element in the input list.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            list[int]: A list containing the count of elements smaller than each element
            in the input list.

        Examples:
            >>> solution = SmallerNumbersThanCurrent()
            >>> solution.smaller_numbers_than_current([8, 1, 2, 2, 3])
            [4, 0, 1, 1, 3]
            >>> solution.smaller_numbers_than_current([6, 5, 4, 8])
            [2, 1, 0, 3]
            >>> solution.smaller_numbers_than_current([7, 7, 7, 7])
            [0, 0, 0, 0]
        """
        count = [0] * 101
        res = []

        for num in nums:
            count[num] += 1

        for i in range(len(nums)):
            total = sum(count[: nums[i]])
            res.append(total)

        return res
