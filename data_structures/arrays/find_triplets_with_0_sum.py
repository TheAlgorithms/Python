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
from itertools import combinations

def find_triplets_with_0_sum(nums):
    triplets = []
    nums.sort()  # Sort the input list in ascending order
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates to avoid duplicate triplets
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1  # Skip duplicates on the left
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1  # Skip duplicates on the right
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return triplets

# Example usage:
result = find_triplets_with_0_sum([-1, 0, 1, 2, -1, -4])
print(result)  # Output: [[-1, -1, 2], [-1, 0, 1]]

