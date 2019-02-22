"""
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
"""
def MF_knapsack(i,wt,val,j):
    '''
    This code involves the concept of memory functions. Here we solve the subproblems which are needed
    unlike the below example
    F is a 2D array with -1s filled up
    '''
    global F  # a global dp table for knapsack
    if F[i][j] < 0:
        if j < wt[i - 1]:
            val = MF_knapsack(i - 1,wt,val,j)
        else:
            val = max(MF_knapsack(i - 1,wt,val,j),MF_knapsack(i - 1,wt,val,j - wt[i - 1]) + val[i - 1])
        F[i][j] = val
    return F[i][j]

def knapsack(W, wt, val, n):
    dp = [[0 for i in range(W+1)]for j in range(n+1)]

    for i in range(1,n+1):
        for w in range(1,W+1):
            if(wt[i-1]<=w):
                dp[i][w] = max(val[i-1]+dp[i-1][w-wt[i-1]],dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][w]

if __name__ == '__main__':
    '''
    Adding test case for knapsack
    '''
    val = [3,2,4,4]
    wt = [4,3,2,3]
    n = 4
    w = 6
    F = [[0]*(w + 1)] + [[0] + [-1 for i in range(w + 1)] for j in range(n + 1)]
    print(knapsack(w,wt,val,n))
    print(MF_knapsack(n,wt,val,w))  # switched the n and w 
    
