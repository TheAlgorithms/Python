"""
Algorithm: Moore's Voting Algorithm
Problem: Find the majority element (appears more than n/2 times) in an array.

Time Complexity: O(n)
Space Complexity: O(1)

Example:
majority_element([2, 2, 1, 1, 1, 2, 2])
2
majority_element([3, 3, 4])
3
"""

def majority_element(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return None

if __name__ == "__main__":
    print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # Output: 2
