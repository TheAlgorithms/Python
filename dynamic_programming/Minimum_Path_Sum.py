class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
    
        n = len(grid)
        m = len(grid[0])
       
        # Edit the first row:
        for i in range(1, m):
            grid[0][i] = grid[0][i-1] + grid[0][i]
        
        # Edit the first col:
        for i in range(1, n):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        
        # Edit the remaining values in the grid accordingly!
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        
        
        return grid[-1][-1]