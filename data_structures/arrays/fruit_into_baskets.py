"""
Question:
Given an array fruits representing types of fruit, pick a contiguous subarray containing at most 2 different types of fruit.
Return the maximum number of fruits you can collect.

Example:
Input: fruits = [1,2,1,2,3]
Output: 4
Explanation:
Pick subarray [1,2,1,2] -> contains 2 types and length 4
"""

from typing import List
from collections import defaultdict


class FruitIntoBaskets:
    def total_fruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)  # Stores count of each fruit type
        left = 0  # Left pointer of sliding window
        max_fruit = 0  # Tracks max number of fruits collected

        for right, fruit in enumerate(fruits):
            count[fruit] += 1  # Include current fruit

            # Shrink window if more than 2 types
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

            max_fruit = max(max_fruit, right - left + 1)

        return max_fruit


# Example dry run
if __name__ == "__main__":
    fruits = [1, 2, 1, 2, 3]
    solver = FruitIntoBaskets()
    print("Maximum Fruits Collected:", solver.total_fruit(fruits))
