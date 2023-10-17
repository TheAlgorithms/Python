def major_ele(nums: list[int]) -> int | None:
    """
    Finds the majority element in a given list using Moore's Voting Algorithm.
    Majority Element: element with more than N/2 occurrences among given elements.
    Time Complexity: O(N)
    Space Complexity: O(1)
    For Further Reading: https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm

    Args:
        nums (list[int]): A list of integers.

    Returns:
        int: The majority element if it exists, otherwise, None

    Examples:
        >>> major_ele([2, 2, 1, 1, 1, 2, 2])
        2
        >>> major_ele([3, 3, 4, 2, 4, 4, 2])

        >>> major_ele([1, 2, 3])

    """
    count = 0  # Not necessarily representing votes of the majority element
    majority_element = None

    for num in nums:
        if count == 0:
            count = 1
            majority_element = num
        elif num == majority_element:
            count += 1
        else:
            count -= 1

    # Being cautious for if there might be NO majority element in the array
    count_of_majority_element = 0

    for num in nums:
        if num == majority_element:
            count_of_majority_element += 1

    if count_of_majority_element > len(nums) // 2:
        return majority_element

    return None


# Example
lst = [2, 2, 1, 1, 1, 2, 2]
print("Majority element in list is:", major_ele(lst))
