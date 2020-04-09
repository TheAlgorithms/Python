'''
When you drop an egg from any floor of the building, the egg will either break or survive the fall. If the egg survives, then it would have survived any lesser fall. If the egg breaks, then any greater fall would have broken it as well. The eggs are all identical and interchangeable.

So find minimum no of attempts
'''



def eggDrop(n, k): 
    dp= [[0 for x in range(k+1)] for x in range(n+1)]
    for i in range (0,k+1):
        dp[0][i]=0
        dp[1][i]=i
    for i in range (0,n+1):
        dp[i][0]=0
        dp[i][1]=1
    
    for i in range (2,n+1):
        for j in range (2,k+1):
            dp[i][j]=100000000
            for k in range (1, j+1):
                tmp=max(dp[i-1][x-1], dp[i][j-x])  #if you break at xth floor then you have x-1 floors and i-1 e#ggs if you doesn't break at xth floor then j-x floors and i eggs remaining
                if (tmp<dp[i][j]):
                    dp[i][j]=tmp
                
    return dp[n][k]
