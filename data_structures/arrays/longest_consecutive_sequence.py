"""
author: Sarthak Sharma https://github.com/Sarthak950
Website: https://sarthak950.netlify.app
date:   4 OCT 2023
Longest Consecutive Sequence Problem from LeetCode
"""


def longest_consecutive_sequence(nums: list[int]) -> int:
    """
    Finds the length of the longest consecutive sequence in a list of numbers.

    Examples:
    >>> longest_consecutive_sequence([100, 4, 200, 1, 3, 2])
    4
    >>> longest_consecutive_sequence([1, 2, 3, 4, 5])
    5
    >>> longest_consecutive_sequence([5, 4, 3, 2, 1])
    5
    >>> longest_consecutive_sequence([])
    0
    """
    if not nums:
        return 0

    # Create a set of all the numbers in the list
    num_set = set(nums)
    longest_sequence = 0

    # Iterate over the set of numbers
    for num in num_set:
        # If the number that is one less than the current number is not in the set,
        # then this is the beginning of a sequence
        if num - 1 not in num_set:  # Start of a potential sequence
            # Store the current number in a variable
            # and initiate a sequence length counter
            current_num = num
            current_sequence = 1

            # While the next number is in the set,
            # increment the current number and the sequence counter
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1

            # Update the longest sequence if the current sequence is longer
            longest_sequence = max(longest_sequence, current_sequence)

    return longest_sequence


"""
This code takes in a list of numbers and returns the length of
the longest sequence of consecutive numbers in the list.
For example, if the list is [1, 3, 2, 4, 5, 6, 7], the function will return 5,
since the longest sequence of consecutive numbers is [3, 4, 5, 6, 7].
"""
