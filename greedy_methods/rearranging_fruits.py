from collections import defaultdict
from typing import DefaultDict, List


def min_cost(basket1: List[int], basket2: List[int]) -> int:
    n = len(basket1)
    freq: DefaultDict[int, int] = defaultdict(int)
    mn: float = float("inf")

    for i in range(n):
        freq[basket1[i]] += 1
        freq[basket2[i]] -= 1
        mn = min(mn, basket1[i], basket2[i])

    to_swap: List[int] = []
    for j, k in freq.items():
        if k % 2 != 0:
            return -1
        to_swap += [j] * (abs(k) // 2)

    to_swap.sort()
    res: int = 0
    for i in range(len(to_swap) // 2):
        # Ensure mn is treated as int during arithmetic
        res += min(to_swap[i], 2 * int(mn))

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
