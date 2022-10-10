"""
Dynamic Programming to solve Brust Balloons.py
Tabulation Approach
https://leetcode.com/problems/burst-balloons/description/
"""


def maxCoins(nums):
    """
    >>> maxCoins([3,1,5,8])
    164
    >>> maxCoins([1,5])
    10
    """
    n = len(nums)

    nums.append(1)  # add 1 at the end of array(nums)
    nums.insert(0, 1)  # add 1 at the starting of the array(nums)

    dp = [[0] * (n + 2) for i in range(n + 2)]

    for i in range(n, 0, -1):
        for j in range(1, n + 1):
            if i > j:
                continue

            ma = float("-inf")

            for ind in range(i, j + 1):
                cost = (
                    nums[i - 1] * nums[ind] * nums[j + 1]
                    + dp[i][ind - 1]
                    + dp[ind + 1][j]
                )
                ma = max(ma, cost)
            dp[i][j] = ma

    return dp[1][n]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
