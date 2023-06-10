def longest_zigzag(nums):
    n = len(nums)
    if n <= 1:
        return n
    
    dp = [[1, 1] for _ in range(n)]
    max_length = 1

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i][0] = max(dp[i][0], dp[j][1] + 1)
                max_length = max(max_length, dp[i][0])
            elif nums[i] < nums[j]:
                dp[i][1] = max(dp[i][1], dp[j][0] + 1)
                max_length = max(max_length, dp[i][1])

    return max_length


# Driver code to test the function
nums = [1, 7, 4, 9, 2, 5]
print("Longest Zigzag Subsequence length:", longest_zigzag(nums))
