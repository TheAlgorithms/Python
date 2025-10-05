"""
Find the majority element in an array.
"""

def majority_element(nums: list[int]) -> int:
    """
    Find the element that appears more than n/2 times using
    Boyer-Moore Voting Algorithm.

    Args:
        nums: List of integers.

    Returns:
        The majority element.

    Examples:
        >>> majority_element([3, 2, 3])
        3
        >>> majority_element([2, 2, 1, 1, 1, 2, 2])
        2
    """
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate


if __name__ == "__main__":
    import doctest
    doctest.testmod()
