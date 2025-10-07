from typing import List
from collections import defaultdict


def min_cost(basket1: List[int], basket2: List[int]) -> int:
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


if __name__ == "__main__":
    # ---- Test Cases ----
    test_cases = [
        ([4, 2, 2, 2], [1, 4, 1, 2]),  # Expected: 1
        ([1, 2, 3, 4], [2, 3, 4, 1]),  # Expected: 0
        ([1, 1, 1, 1], [1, 1, 1, 1]),  # Expected: 0
        ([1, 2, 2], [2, 1, 1]),  # Expected: -1
        ([5, 3, 3, 2], [2, 5, 5, 3]),  # Expected: -1
    ]

    print("Running test cases...\n")
    for b1, b2 in test_cases:
        print(f"basket1 = {b1}, basket2 = {b2} → minCost = {min_cost(b1, b2)}")
