"""
Partition a set into two subsets such that the difference of subset sums is minimum
"""
def findMin(arr):
    n = len(arr)
    s = sum(arr)

    dp = [[False for x in range(s+1)]for y in range(n+1)]

    for i in range(1, n+1):
        dp[i][0] = True

    for i in range(1, s+1):
        dp[0][i] = False

    for i in range(1, n+1):
        for j in range(1, s+1):
            dp[i][j]= dp[i][j-1]

            if (arr[i-1] <= j):
                dp[i][j] = dp[i][j] or dp[i-1][j-arr[i-1]]

    for j in range(int(s/2), -1, -1):
        if dp[n][j] == True:
            diff = s-2*j
            break;

    return diff
