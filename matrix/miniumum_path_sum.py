class Solution(object):
   def minPathSum(self, grid):
      row = len(grid)-1
      column = len(grid[0])-1
      i=row-1
      j=column-1
      while j>=0:
         grid[row][j]+=grid[row][j+1]
         j-=1
      while i>=0:
         grid[i][column]+=grid[i+1][column]
         i-=1
      j=column-1
      i = row-1
      while i>=0:
         while j>=0:
            grid[i][j] += min(grid[i][j+1],grid[i+1][j])
            j-=1
         j=column-1
         i-=1
      return(grid[0][0])
ob1 = Solution()