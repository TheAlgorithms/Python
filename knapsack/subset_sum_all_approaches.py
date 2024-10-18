"""
Given a set of integers and a target sum, determine if there exists a subset whose sum equals the target. 
Return True if such a subset exists, otherwise return False.
"""
------------------------------------------------------Recursion-Approach-------------------------------------------------------------------------

def is_subset_sum_recursive(arr, n, target):
    # Base cases
    if target == 0:
        return True
    if n == 0:
        return False

    # If last element is greater than target, ignore it
    if arr[n-1] > target:
        return is_subset_sum_recursive(arr, n-1, target)

    # Check if including or excluding the current item achieves the target
    return is_subset_sum_recursive(arr, n-1, target) or is_subset_sum_recursive(arr, n-1, target - arr[n-1])

arr = [3, 34, 4, 12, 5, 2]
target = 9
n = len(arr)
print(is_subset_sum_recursive(arr, n, target))  # Output: True

arr = [3, 34, 4, 12, 5, 2]
target = 30
n = len(arr)
print(is_subset_sum_recursive(arr, n, target))  # Output: False

-------------------------------------------------------Memoization-Approach-------------------------------------------------------------------------

def is_subset_sum_memo(arr, n, target, memo):
    # Base cases
    if target == 0:
        return True
    if n == 0:
        return False

    # If this subproblem has already been solved
    if memo[n][target] is not None:
        return memo[n][target]

    # If last element is greater than target, ignore it
    if arr[n-1] > target:
        memo[n][target] = subset_sum_memo(arr, n-1, target, memo)
    else:
        # Check if including or excluding the current item achieves the target
        memo[n][target] = subset_sum_memo(arr, n-1, target, memo) or subset_sum_memo(arr, n-1, target - arr[n-1], memo)

    return memo[n][target]

# Helper function
def subset_sum_memo_helper(arr, target):
    n = len(arr)
    memo = [[None] * (target + 1) for _ in range(n + 1)]
    return is_subset_sum_memo(arr, n, target, memo)

arr = [3, 34, 4, 12, 5, 2]
target = 9
print(subset_sum_memo_helper(arr, target))  # Output: True

arr = [3, 34, 4, 12, 5, 2]
target = 30
print(subset_sum_memo_helper(arr, target))  # Output: False

-------------------------------------------------------Top-Down-Approach--------------------------------------------------------------------

def is_subset_sum_dp(arr, target):
    n = len(arr)
    # Create a (n+1) x (target+1) DP table
    dp = [[False] * (target + 1) for _ in range(n + 1)]

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

arr = [3, 34, 4, 12, 5, 2]
target = 9
print(is_subset_sum_dp(arr, target))  # Output: True

arr = [3, 34, 4, 12, 5, 2]
target = 30
print(is_subset_sum_dp(arr, target))  # Output: False
