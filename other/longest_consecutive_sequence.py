# Longest Consecutive Sequence
# https://www.github.com/JehanPatel

# Logic behind the question

# nums = [2, 3, 1, 4, 5]
# 1. num = 2
#    1 is present -> Don't run the inner loop
# 2. num = 3
#    2 is present -> Don't run the inner loop
# 3. curr_num = 1
#    0 is not present -> Run the inner loop
#    a. curr_num = 1, curr_len = 1, while condition: True
#    b. curr_num = 2, curr_len = 2, while condition: True
#    c. curr_num = 3, curr_len = 3, while condition: True
#    d. curr_num = 4, curr_len = 4, while condition: True
#    e. curr_num = 5, curr_len = 5, while condition: False

# Optimal Code

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        num_set = set(nums)
        for num in nums:
            if num - 1 not in num_set:
                curr_num = num
                curr_len = 1
                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_len += 1
                max_len = max(max_len, curr_len)
        return max_len
    
# Time and Space complexity = o(n)    
# refer to leetcode discussion tab for further clarification. 