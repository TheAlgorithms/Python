class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        i = 0
        max_len, cur_max_len = 1, 1
        nums = list(set(nums))
        nums.sort()
        while i < len(nums) - 1:
            if nums[i + 1] - nums[i] == 1:
                cur_max_len += 1
            else:
                cur_max_len = 1
            i += 1
            if cur_max_len > max_len:
                max_len = cur_max_len
        return max_len if nums != [] else 0