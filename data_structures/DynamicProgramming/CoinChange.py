'''
Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def coinchange2(self, a, B):
        n=len(a)
        m=B
        dp = [0]*(m+1)
        mod=1000007
        dp[0]=1
        
        for i in range (0,n):
            for j in range (1,m+1):
                if(a[i] <= j) :
                    dp[j] = ((dp[j] % mod) + ( dp[j-a[i]] % mod)) % mod
                    
        return dp[m]

