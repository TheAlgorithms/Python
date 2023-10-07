"""
https://medium.com/@eric.christopher.ness/leetcode-15-three-sum-de7e11e25106
"""


def find_triplets_with_0_sum(nums: list[int]) -> list[list[int]]:
    """
    Given a list of integers, return elements a, b, c such that a + b + c = 0.

    Args:
        nums (list[int]): list of integers

    Returns:
        list[list[int]]: list of lists of integers

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
    # Sort the list in ascending order to use two pointer method.
    nums.sort()

    result = []

    # Iterate through the list and use two-pointer method to initialize the target.
    for index in range(len(nums)):
        # Skip duplicate elements so that result does not contain duplicate triplets.
        if index > 0 and nums[index] == nums[index - 1]:
            continue

        # Initialize the target and the left and right pointers.
        target = -nums[index]
        left = index + 1
        right = len(nums) - 1

        # Two-pointer method
        while left < right:
            # If the sum equals target, add the triplet to result.
            if nums[left] + nums[right] == target:
                result.append([nums[index], nums[left], nums[right]])
                left += 1

                # Skip duplicate elements.
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

            # If the sum of is lesser than target, increment left pointer.
            elif nums[left] + nums[right] < target:
                left += 1

            # If the sum of is greater than target, decrement right pointer.
            else:
                right -= 1

    return result
