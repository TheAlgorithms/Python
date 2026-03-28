def majority_element(nums: list[int]) -> int:
    """
    Find majority element using Boyer-Moore Voting Algorithm
    https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm

    >>> majority_element([3, 3, 4])
    3
    >>> majority_element([2, 2, 1, 1, 2, 2, 2])
    2
    """

    if not nums:
        raise ValueError("List cannot be empty")

    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate
