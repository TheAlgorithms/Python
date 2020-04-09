'''
Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.

Insert
Remove
Replace
All of the above operations are of equal cost.

Examples:

Input:   str1 = "geek", str2 = "gesek"
Output:  1
We can convert str1 into str2 by inserting a 's'.

Input:   str1 = "cat", str2 = "cut"
Output:  1
We can convert str1 into str2 by replacing 'a' with 'u'.

Input:   str1 = "sunday", str2 = "saturday"
Output:  3
Last three and first characters are same.  We basically
need to convert "un" to "atur".  This can be done using
below three operations. 
Replace 'n' with 'r', insert t, insert a
'''



class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def minDistance(self, A, B):
	    n=len(A)
	    m=len(B)
        dp = [[0]*(m+1) for i in range(n+1)]
    # m=colums n=rows
	    
	   
	    for i in range (0,m+1):
	        dp[0][i]=i
        for i in range (0,n+1):
            dp[i][0]=i
        
        
        
        for i in range (1, n+1):
            for j in range (1,m+1):
                if(A[i-1]==B[j-1]):
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=1+min(dp[i-1][j],dp[i][j-1], dp[i-1][j-1])
        
        return dp[n][m]
