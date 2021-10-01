# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
# which minimizes the sum of all numbers along its path.You can only move either down or right at any point in time.


def minPathSum(grid):
        m=len(grid)
        n=len(grid[0])
        for i in range(0,m):
            for j in range(0,n):
                if i>0 and j>0:
                    grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
                elif i>0:
                    grid[i][j]+=grid[i-1][j]
                elif j>0:
                    grid[i][j]+=grid[i][j-1]
        return grid[m-1][n-1]

if __name__ == "__main__":
    grid=[[1,3,1],[1,5,1],[4,2,1]]
    print(minPathSum(grid))
