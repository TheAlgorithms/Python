from itertools import combinations


def find_triplets_with_0_sum(nums: list[int]) -> list[list[int]]:
    """
    Given a list of integers, return elements a, b, c such that a + b + c = 0.
    Args:
        nums: list of integers
    Returns:
        list of lists of integers where sum(each_list) == 0
    Examples:
        >>> find_triplets_with_0_sum([-1, 0, 1, 2, -1, -4])
        [[-1, -1, 2], [-1, 0, 1]]
        >>> find_triplets_with_0_sum([])
        []
        >>> find_triplets_with_0_sum([0, 0, 0])
        [[0, 0, 0]]
        >>> find_triplets_with_0_sum([1, 2, 3, 0, -1, -2, -3])
        [[-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
    """
    return [
        list(x)
        for x in sorted({abc for abc in combinations(sorted(nums), 3) if not sum(abc)})
    ]
