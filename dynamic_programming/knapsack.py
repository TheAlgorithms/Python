"""
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
"""
def knapsack(W, wt, val, n):
    dp = [[0 for i in range(W+1)]for j in range(n+1)]

    for i in range(1,n+1):
        for w in range(1,W+1):
            if(wt[i-1]<=w):
                dp[i][w] = max(val[i-1]+dp[i-1][w-wt[i-1]],dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][w]
if __name__ == "__main__":
    val = [3,2,4,4]
    wt = [4,3,2,3]
    W = 6
    n = 4
    '''
    Should give 8
    '''
    print(knapsack(W,wt,val,n))
   
