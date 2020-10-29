# Goldmine Problem.

#Question Problem : https://leetcode.com/problems/path-with-maximum-gold/

n = int(input().strip())
m = int(input().strip())
arr = [[0]*m for _ in range(n)]
print(arr)
for i in range(n):
    arr[i] = [int(j) for j in input().strip().split(" ")]

dp = [[0]*m for _ in range(n)]

for col in range(m - 1, -1, -1):
    for row in range(n-1,-1,-1):

        if col == m - 1:
            dp[row][col] = arr[row][col]
        elif row == 0:
            dp[row][col] = arr[row][col] + max(dp[row][col + 1], dp[row + 1][col + 1])
        elif row == n - 1:
            dp[row][col] = arr[row][col] + max(dp[row][col + 1], dp[row - 1][col + 1])
        else:
            dp[row][col] = arr[row][col] + max(dp[row][col + 1], dp[row + 1][col + 1], dp[row - 1][col + 1])

maximum = 0
for i in range(n):
    if dp[i][0] > maximum:
        maximum = dp[i][0]
print(maximum)


