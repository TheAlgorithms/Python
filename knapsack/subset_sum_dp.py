def is_subset_sum_dp(arr, target):
    # length
    n = len(arr)
  
    # (n+1) x (target+1) DP table
    dp = []
    for i in range(n + 1):
        row = []
        for j in range(target + 1):
            row.append(False)
        dp.append(row)

    # Initialize the table: If target is 0, answer is True
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j - arr[i-1]]

    return dp[n][target]

# Test cases
arr = [3, 34, 4, 12, 5, 2]
target = 9
print(is_subset_sum_dp(arr, target))  # Output: True

arr = [3, 34, 4, 12, 5, 2]
target = 30
print(is_subset_sum_dp(arr, target))  # Output: False
