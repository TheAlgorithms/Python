"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that
adjacent houses have security systems connected
and it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, we have to
return the maximum amount of money you can rob tonight without alerting the police.

Source : https://leetcode.com/problems/house-robber?envType=problem-list-v2&envId=dynamic-programming


Example

>>> rob([1,2,3,1])
4

"""

def rob(nums: list[int]) -> int:
    n = len(nums)
    if n < 3:
        return max(nums)
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
    return max(dp)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
