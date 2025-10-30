'''
Leetcode Problem:673. Number of Longest Increasing Subsequence
Link: https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/

Given an integer array nums, return the number of longest increasing subsequences.
Notice that the sequence has to be strictly increasing.

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.
 

Constraints:

1 <= nums.length <= 2000
-10**6 <= nums[i] <= 10**6
The answer is guaranteed to fit inside a 32-bit integer.
'''


def findNumberOfLIS(nums):
    n = len(nums)
    if n == 0:
        return 0

    length = [1] * n
    count = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = count[j]
                elif length[j] + 1 == length[i]:
                    count[i] += count[j]

    max_len = max(length)
    return sum(c for l, c in zip(length, count) if l == max_len)


# For testing...
n=int(input())
nums=list(map(int,input().split()))
print(findNumberOfLIS(nums))
