class Solution:

    '''
        have the track of prev element 
        if the current element is greater than the prev element then
            decrement the value of both n and k  as it is included
        else
            you can make the current prev element and include it 
    '''

    def func(self,prev,n,k) : 

        if n<=0 :
            if k == 0 :
                return 1 
            else :
                return 0 
            
        if self.dp[prev][n][k] != -1 :
            return self.dp[prev][n][k]

        cnt = 0
        for ele in range(1,self.m+1) :
            # include 
            if ele > prev :
                if n>0 and k>0 :
                    cnt += (self.func(ele,n-1,k-1))%self.mod

            else :    # start with new
                if n>0:
                    cnt += (self.func(prev,n-1,k))%self.mod

        self.dp[prev][n][k] = cnt%self.mod 
        return cnt

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        self.m = m 
        self.mod = 10**9 + 7
        self.dp = [[[-1 for _ in range(k+1)] for __ in range(n+1)] for ___ in range(m+1)]
        return self.func(-1 , n ,k)%self.mod

        
