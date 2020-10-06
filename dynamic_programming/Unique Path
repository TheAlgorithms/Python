class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for j in range(0, n)] for i in range(0, m)]
            
        for i in range(0, m):
            dp[i][0] = 1
        
        for j in range(0, n):
            dp[0][j] = 1
            
        for i in range(1, m):            
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                
        
        return dp[m - 1][n - 1]
