class Solution:
    def perform_swap(self, arr, i):
        if i > len(arr) or i <= 0:
            return

        tmp = arr[i - 1]
        arr[i - 1] = i
        if tmp == i:
            return
        self.perform_swap(arr, tmp)

    def firstMissingPositive(self, nums: List[int]) -> int:
        for num in nums:
            self.perform_swap(nums, num)
        for i, num in enumerate(nums, start=1):
            if num != i:
                return i
        
        return len(nums) + 1
