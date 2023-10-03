from itertools import combinations
from typing import List


def combine_recursive(nums: List[int], k: int) -> List[List[int]]:
    """
    Return all combinations of length k.

    >>> combine_recursive([1, 2, 3], 2)
    [[1, 2], [1, 3], [2, 3]]
    """
    result: List[List[int]] = []

    def combine_helper(current_combination: List[int], start: int, k: int) -> None:
        if k == 0:
            result.append(current_combination)
            return
        for i in range(start, len(nums)):
            combine_helper(current_combination + [nums[i]], i + 1, k - 1)

    combine_helper([], 0, k)
    return result


if __name__ == "__main__":
    import doctest

    result = combine_recursive([1, 2, 3], 2)
    print(result)
    doctest.testmod()
