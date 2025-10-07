# it's a leetcode question no. 2561 where You have two fruit baskets containing n fruits each. You are given two 0-indexed integer arrays basket1 and basket2 representing the cost of fruit in each basket.
# You want to make both baskets equal. To do so, you can use the following operation as many times as you want:

# Chose two indices i and j, and swap the ith fruit of basket1 with the jth fruit of basket2.
# The cost of the swap is min(basket1[i],basket2[j]).
# Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.

# Return the minimum cost to make both the baskets equal or -1 if impossible.

from typing import List
from collections import defaultdict


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        n = len(basket1)
        freq = defaultdict(int)
        mn = float("inf")
        for i in range(n):
            freq[basket1[i]] += 1
            freq[basket2[i]] -= 1
            mn = min(mn, basket1[i], basket2[i])

        to_swap = []
        for j, k in freq.items():
            if k % 2 != 0:
                return -1
            to_swap += [j] * (abs(k) // 2)

        to_swap.sort()
        res = 0
        for i in range(len(to_swap) // 2):
            res += min(to_swap[i], 2 * mn)

        return res


s = Solution()
print(s.minCost([4, 2, 2, 2], [1, 4, 1, 2]))  # Output: 1
