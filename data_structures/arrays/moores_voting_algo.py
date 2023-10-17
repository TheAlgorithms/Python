from typing import List, Optional


def majorityElement(nums: List[int]) -> Optional[int]:
    """
    Finds the majority element in a given list using Moore's Voting Algorithm.
    Majority Element : that have more than N/ 2 occurrences among the given elements.
    Time Complexity : O(N)
    Space Complexity : O(1)

    Args:
        nums (List[int]): A list of integers.

    Returns:
        int: The majority element if it exists otherwise (-1)

    Examples:
        >>> majorityElement([2, 2, 1, 1, 1, 2, 2])
        2
        >>> majorityElement([3, 3, 4, 2, 4, 4, 2])
        -1
        >>> majorityElement([1, 2, 3])
        -1
    """
    count = 0  # Not necessarily representing votes of the majority element
    majority_element = None

    for num in nums:
        # The majority element's votes cannot be canceled even if all other elements conspire against it!
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

    return -1


# Example
list = [2, 2, 1, 1, 1, 2, 2]
print("Majority element in list is:", majorityElement(list))
