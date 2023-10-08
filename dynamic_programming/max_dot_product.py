"""
Author  : Yash Kesharwani
Date    : October 8, 2023

This is a pure Python implementation of Dynamic Programming solution to
The max dot product of 2 sequence.

The problem is :
Given two arrays nums1 and nums2.
Return the maximum dot product between non-empty subsequences of
nums1 and nums2 with the same length.
"""


class MaxDotProductOf2Sequence:
    def solve(self, i, j, nums1, nums2, n, m, dp):
        if i == n or j == m:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        ans = float("-inf")
        take = nums1[i] * nums2[j] + self.solve(i + 1, j + 1, nums1, nums2, n, m, dp)
        nottake2 = self.solve(i + 1, j, nums1, nums2, n, m, dp)
        nottake1 = self.solve(i, j + 1, nums1, nums2, n, m, dp)
        ans1 = max(nottake1, nottake2)
        ans = max(take, ans1)
        dp[i][j] = ans
        return ans

    def maxdotproduct(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        firstmax = float("-inf")
        secondmax = float("-inf")
        firstmin = float("inf")
        secondmin = float("inf")
        for num in nums1:
            firstmax = max(firstmax, num)
            firstmin = min(firstmin, num)

        for num in nums2:
            secondmax = max(secondmax, num)
            secondmin = min(secondmin, num)

        if firstmax < 0 and secondmin > 0:
            return firstmax * secondmin

        if firstmin > 0 and secondmax < 0:
            return firstmin * secondmax

        dp = [[-1] * m for _ in range(n)]
        return self.solve(0, 0, nums1, nums2, n, m, dp)


# Main function to take input and print output
if __name__ == "__main__":
    nums1 = list(map(int, input("Enter the first array: ").split()))
    nums2 = list(map(int, input("Enter the second array: ").split()))

    solution = MaxDotProductOf2Sequence()
    result = solution.maxdotproduct(nums1, nums2)

    print("Maximum Dot Product:", result)
