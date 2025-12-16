"""Return indices of the two numbers that add up to the target.

Uses a single pass hash map for O(n) time complexity.
"""

from typing import Dict, Iterable, Tuple


def two_sum(nums: Iterable[int], target: int) -> Tuple[int, int]:
    seen: Dict[int, int] = {}
    for idx, value in enumerate(nums):
        other = target - value
        if other in seen:
            return seen[other], idx
        seen[value] = idx
    raise ValueError("No two numbers sum to target")
