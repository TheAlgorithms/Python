"""
This program counts pairs in an array that sum up to a given target sum.

Reference: https://www.geeksforgeeks.org/count-pairs-with-given-sum/

Author : Arunkumar (Arunsiva003)
Date: 9th October 2023
"""
from typing import List, Dict

def count_pairs_with_given_sum(arr: List[int], target_sum: int) -> int:
    """
    Count pairs in the array that sum up to the given target sum.

    Args:
        arr : The input array of integers.
        target_sum : The target sum to be matched.

    Returns:
        int: The count of pairs that sum up to the target sum.

    Examples:
        >>> count_pairs_with_given_sum([1, 2, 3, 4, 5], 6)
        2
        >>> count_pairs_with_given_sum([4, 5, 6, 7, 8, 9], 13)
        3
    """
    # Create a dictionary to store the frequency of each element in the array
    num_freq: Dict[int, int] = {}
    
    # Initialize the count of pairs to 0
    pair_count = 0
    
    # Iterate through the array
    for num in arr:
        # Calculate the difference needed to reach the target sum
        diff = target_sum - num
        
        # If the difference is in the dictionary, increment the pair count
        if diff in num_freq:
            pair_count += num_freq[diff]
        
        # Update the frequency of the current number in the dictionary
        if num in num_freq:
            num_freq[num] += 1
        else:
            num_freq[num] = 1
    
    # The pair count is twice the actual count, so divide by 2
    return pair_count

if __name__ == "__main__":
    input_arr = [1,2,3,4,5,6]
    target_sum = 6
    print(f"Pairs that sum up to {target_sum}: {count_pairs_with_given_sum(input_arr, target_sum)}")
