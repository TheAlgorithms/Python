class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            a = nums.count(nums[i])
            d[a] = nums[i]
        for i, j in d.items():
            if i == 1:
                return j
