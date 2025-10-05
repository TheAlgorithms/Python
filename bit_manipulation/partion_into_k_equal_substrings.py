"""
Partition to K Equal Sum Subsets
Medium

Problem Statement:
Given an integer array nums and an integer k, return true if it is possible 
to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:
Input: nums = [1,2,3,4], k = 3
Output: false

Constraints:
- 1 <= k <= nums.length <= 16
- 1 <= nums[i] <= 10^4
- The frequency of each element is in the range [1, 4]

Algorithm Analysis:
- The key insight is that if we can partition into k equal subsets, 
  each subset must have sum = total_sum / k
- We use backtracking to try placing each number into different buckets
- Multiple optimizations are applied for efficiency

Time Complexity: O(k^n) in worst case, but pruning makes it much faster in practice
Space Complexity: O(k) for buckets + O(n) for recursion stack
"""

from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
        Approach 1: Backtracking with Bucket Filling
        
        Time Complexity: O(k^n) where n is the length of nums
        Space Complexity: O(k) for the buckets array + O(n) for recursion stack
        
        Strategy:
        1. Calculate target sum for each subset
        2. Use backtracking to try placing each number in each bucket
        3. Prune early if any bucket exceeds target
        """
        total = sum(nums)
        
        # Early termination checks
        if total % k != 0:
            return False
        
        target = total // k
        
        # If any number is larger than target, impossible
        if max(nums) > target:
            return False
        
        # Sort in descending order for better pruning
        nums.sort(reverse=True)
        
        # Create k buckets to store current sums
        buckets = [0] * k
        
        def backtrack(index: int) -> bool:
            # Base case: all numbers have been placed
            if index == len(nums):
                return True
            
            current_num = nums[index]
            
            # Try placing current number in each bucket
            for i in range(k):
                # Skip if placing current number exceeds target
                if buckets[i] + current_num > target:
                    continue
                
                # Place number in bucket i
                buckets[i] += current_num
                
                # Recursively try to place remaining numbers
                if backtrack(index + 1):
                    return True
                
                # Backtrack: remove number from bucket i
                buckets[i] -= current_num
                
                # Optimization: if current bucket is empty and we can't make a solution,
                # then other empty buckets won't work either
                if buckets[i] == 0:
                    break
            
            return False
        
        return backtrack(0)
    
    def canPartitionKSubsets_optimized(self, nums: List[int], k: int) -> bool:
        """
        Approach 2: Optimized Backtracking with Bitmask
        
        Time Complexity: O(k * 2^n)
        Space Complexity: O(2^n) for memoization
        
        This approach uses bitmask to represent which numbers have been used
        and memoization to avoid recomputing the same states.
        """
        total = sum(nums)
        
        if total % k != 0:
            return False
        
        target = total // k
        
        if max(nums) > target:
            return False
        
        nums.sort(reverse=True)
        n = len(nums)
        
        # Memoization: memo[mask] = whether we can partition remaining numbers
        memo = {}
        
        def dp(mask: int) -> bool:
            if mask in memo:
                return memo[mask]
            
            # Calculate current sum of used numbers
            current_sum = sum(nums[i] for i in range(n) if mask & (1 << i))
            
            # If current sum is multiple of target, we can start a new subset
            if current_sum % target == 0:
                memo[mask] = solve(mask)
                return memo[mask]
            
            # Try adding each unused number to current subset
            remainder = current_sum % target
            for i in range(n):
                # Skip if number is already used or would exceed target
                if mask & (1 << i) or nums[i] > target - remainder:
                    continue
                
                # Try using this number
                if dp(mask | (1 << i)):
                    memo[mask] = True
                    return True
            
            memo[mask] = False
            return False
        
        def solve(mask: int) -> bool:
            if mask == (1 << n) - 1:  # All numbers used
                return True
            
            # Find first unused number to start new subset
            for i in range(n):
                if not (mask & (1 << i)):
                    return dp(mask | (1 << i))
            
            return False
        
        return solve(0)


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    test_cases = [
        # (nums, k, expected)
        ([4, 3, 2, 3, 5, 2, 1], 4, True),
        ([1, 2, 3, 4], 3, False),
        ([1, 1, 1, 1], 2, True),
        ([2, 2, 2, 2, 3, 3, 3, 3], 4, True),
        ([5, 5, 5, 5, 16, 4, 4, 4, 4, 4, 4, 4, 4, 4], 8, False),
        ([1], 1, True),
        ([2, 2], 1, True),
        ([1, 1], 2, True),
    ]
    
    print("Testing Partition to K Equal Sum Subsets")
    print("=" * 50)
    
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        # Test both approaches
        result1 = solution.canPartitionKSubsets(nums.copy(), k)
        result2 = solution.canPartitionKSubsets_optimized(nums.copy(), k)
        
        status1 = "✓" if result1 == expected else "✗"
        status2 = "✓" if result2 == expected else "✗"
        
        print(f"Test {i}:")
        print(f"  Input: nums = {nums}, k = {k}")
        print(f"  Expected: {expected}")
        print(f"  Backtracking: {result1} {status1}")
        print(f"  Optimized: {result2} {status2}")
        print()


def demonstrate_algorithm():
    """Demonstrate how the algorithm works step by step"""
    print("Algorithm Demonstration")
    print("=" * 30)
    
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    
    print(f"Input: nums = {nums}, k = {k}")
    print(f"Total sum: {sum(nums)}")
    print(f"Target sum per subset: {sum(nums) // k}")
    print()
    
    print("Possible partition:")
    print("Subset 1: [5] = 5")
    print("Subset 2: [1, 4] = 5") 
    print("Subset 3: [2, 3] = 5")
    print("Subset 4: [2, 3] = 5")
    print()
    
    solution = Solution()
    result = solution.canPartitionKSubsets(nums, k)
    print(f"Can partition: {result}")


if __name__ == "__main__":
    # Run tests
    test_solution()
    
    # Demonstrate algorithm
    demonstrate_algorithm()
    
    # Interactive testing
    print("\n" + "=" * 50)
    print("Interactive Testing")
    print("Enter your own test case:")
    
    try:
        nums_input = input("Enter numbers separated by spaces: ")
        k_input = input("Enter k: ")
        
        nums = list(map(int, nums_input.split()))
        k = int(k_input)
        
        solution = Solution()
        result = solution.canPartitionKSubsets(nums, k)
        
        print(f"\nResult: {result}")
        if result:
            print("It is possible to partition the array into k equal sum subsets!")
        else:
            print("It is not possible to partition the array into k equal sum subsets.")
            
    except (ValueError, KeyboardInterrupt):
        print("Invalid input or interrupted.")
