#The problem is there is a robot on an m x n grid. The robot is initially located at the top-left corner of grid the robot tries to move to the bottom-right corner. The robot can only move either down or right at any point in time.Return number of all  possible unique paths robot can take.
class Solution:
    def uniquePaths(self, m, n):
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            dp[i][0] = 1

        for i in range(n):
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
