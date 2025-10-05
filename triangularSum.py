class Solution:
    def triangularSum(self, nums):
        current = nums[:]
        while len(current) > 1:
            new_nums = []
            for i in range(len(current) - 1):
                new_nums.append((current[i] + current[i + 1]) % 10)
            current = new_nums
        return current[0]
