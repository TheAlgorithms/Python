'''
You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

You have two robots that can collect cherries for you:

Robot #1 is located at the top-left corner (0, 0), and
Robot #2 is located at the top-right corner (0, cols - 1).
Return the maximum number of cherries collection using both robots by following the rules below:

1. From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
2. When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
3. When both robots stay in the same cell, only one takes the cherries.
4. Both robots cannot move outside of the grid at any moment.
5. Both robots should reach the bottom row in grid.

Problem Statement:- https://leetcode.com/problems/cherry-pickup-ii

'''

		
from typing import List
from collections import defaultdict

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.dp = defaultdict(int)
        return self.recurse(grid, 0, 0, len(grid[0])-1) 

    
    def recurse(self, grid, r, c1, c2):
        # Reached the end
        if r == len(grid): return 0
        
        # Both robots can't share same tile
        if c1 == c2: return float('-inf')

        if 0 <= r < len(grid) and 0 <= c1 < len(grid[0]) and 0 <= c2 < len(grid[0]):
            res = 0
            for y1 in [c1-1, c1, c1+1]:
                for y2 in [c2-1, c2, c2+1]:
                    if self.dp.get((r+1, y1, y2)): val = self.dp[(r+1, y1, y2)]
                    else: val = self.recurse(grid, r+1, y1, y2)
                    res = max(res, val)
                    
            self.dp[(r, c1, c2)] = grid[r][c1] + grid[r][c2] + res
            return grid[r][c1] + grid[r][c2] + res

        
        return float('-inf')

grid = [
    [3, 1, 1],
    [2, 5, 1],
    [1, 5, 3]
]

solution = Solution()
result = solution.cherryPickup(grid)
print(result)  # Output: 19
