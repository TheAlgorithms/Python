'''
Given a cost matrix cost[][] and a position (m, n) in cost[][], write a function that returns cost of minimum cost path to reach (m, n) from (0, 0). Each cell of the matrix represents a cost to traverse through that cell. Total cost of a path to reach (m, n) is sum of all the costs on that path (including both source and destination). You can only traverse down, right and diagonally lower cells from a given cell, i.e., from a given cell (i, j), cells (i+1, j), (i, j+1) and (i+1, j+1) can be traversed. You may assume that all costs are positive integers.


Input : 

    [  1 3 2
       4 3 1
       5 6 1
    ]

Output : 8
     1 -> 3 -> 2 -> 1 -> 1
'''

class Solution:
	# @param A : list of list of integers
	# @return an integer
	def minPathSum(self, A):
	    n=len(A)
	    m=len(A[0])
	    dp = [[0]*(m) for i in range(n)]
	    dp[0][0]=A[0][0]
	    
	    for i in range (1,m):
	        dp[0][i]=A[0][i]+dp[0][i-1]
	    for i in range (1,n):
	        dp[i][0]=A[i][0]+dp[i-1][0]
	        
	    for i in range (1, n):
	        for j in range (1,m):
	            dp[i][j]=min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+A[i][j]

        return dp[n-1][m-1]


