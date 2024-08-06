def longestConsecutiveAP(arr):
    n = len(arr)
    if n <= 2:
        return n  # If there are 2 or fewer elements, the answer is n.

    # Create a dictionary to store the length of the longest AP ending at index i with common difference d.
    dp = {}

    longestLength = 2  # Initialize with a minimum length of 2

    # Initialize dp for common difference 0 (single element).
    for i in range(n):
        dp[i] = {}
        dp[i][0] = 1

    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            diff = arr[i] - arr[j]
            if diff in dp[j]:
                dp[i][diff] = dp[j][diff] + 1  # Increment the length of the current AP

                # Update the longest length
                longestLength = max(longestLength, dp[i][diff])

    return longestLength


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    result = longestConsecutiveAP(arr)
    print(result)
