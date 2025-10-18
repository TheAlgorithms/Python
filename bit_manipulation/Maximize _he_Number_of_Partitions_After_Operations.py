# Topics: Bit Manuputation, Bit-Mask, DP


class Solution:
    def __init__(self):
        self.dp = {}
    
    def countSetBits(self, n):
        count = 0
        while n > 0:
            count += n & 1
            n >>= 1
        return count
    
    def helper(self, s, k, i, mask, isChange):
        n = len(s)
        if i == n:
            return 1
        
        currState = (i << 27) | (mask << 1) | isChange
        
        if currState in self.dp:
            return self.dp[currState]
        
        result = 0
        val = ord(s[i]) - ord('a')
        
        count = self.countSetBits(mask | (1 << val))
        temp = 0
        if count > k:
            temp = 1 + self.helper(s, k, i + 1, 1 << val, isChange)
        else:
            temp = self.helper(s, k, i + 1, mask | (1 << val), isChange)
        result = max(result, temp)
        
        if isChange == 0:
            for j in range(26):
                count = self.countSetBits(mask | (1 << j))
                if count > k:
                    temp = 1 + self.helper(s, k, i + 1, 1 << j, 1)
                else:
                    temp = self.helper(s, k, i + 1, mask | (1 << j), 1)
                result = max(result, temp)
        
        self.dp[currState] = result
        return result
    
    def maxPartitionsAfterOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        return self.helper(s, k, 0, 0, 0)

 #  Time Complexity: O(n × 2²⁷)
 # Auxiliary Space: O(n × 2²⁷)
