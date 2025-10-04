from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [0] * (2 * l)
        for i in range(l):
            res[i] = nums[i]
            res[i+l] = nums[i]
        return res
        