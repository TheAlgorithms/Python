class Solution:
    def __init__(self):
        self.dp = {}
    def count_set_bits(self, n):
        count = 0
        while n > 0:
            count += n & 1
            n >>= 1
        return count
    def helper(self, s, k, i, mask, is_change):
        n = len(s)
        if i == n:
            return 1
        curr_state = (i << 27) | (mask << 1) | is_change
        if curr_state in self.dp:
            return self.dp[curr_state]
        result = 0
        val = ord(s[i]) - ord('a')
        count = self.count_set_bits(mask | (1 << val))
        temp = 0
        if count > k:
            temp = 1 + self.helper(s, k, i + 1, 1 << val, is_change)
        else:
            temp = self.helper(s, k, i + 1, mask | (1 << val), is_change)
        result = max(result, temp)
        if is_change == 0:
            for j in range(26):
                count = self.count_set_bits(mask | (1 << j))
                if count > k:
                    temp = 1 + self.helper(s, k, i + 1, 1 << j, 1)
                else:
                    temp = self.helper(s, k, i + 1, mask | (1 << j), 1)
                result = max(result, temp)
        self.dp[curr_state] = result
        return result    
    def max_partitions_after_operations(self, s, k):
         """
        :type s: str
        :type k: int
        :rtype: int
        """
        return self.helper(s, k, 0, 0, 0)


# Time Complexity: O(n × 2²⁷)
# Auxiliary Space: O(n × 2²⁷)
