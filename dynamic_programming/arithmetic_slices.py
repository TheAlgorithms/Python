"""
    An integer array is called arithmetic if it 
    consists of at least three elements and if 
    the difference between any two consecutive 
    elements is the same.

    Given an integer array nums, 
    return the number of 
    arithmetic subarrays of nums.

    A subarray is a contiguous 
    subsequence of the array.

"""

class ArithmeticSlices:
    def numberofarithmeticslices(self, nums):
        
        """
        This defines a class and a function.  
        `nums` is input list of integers.
        """
        n = len(nums)
        
        """
        We store the length of the 
        array nums in variable n
        """
        if n < 3:
            return 0
        
        total = 0
        curr = 0
        
        """
        An *arithmetic slice* must have **at least 3 numbers**.

        So, if the array has fewer than 3 elements,  
        no arithmetic slices are possible — immediately return `0`.
        """
        
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                curr += 1
                total += curr
            else:
                curr = 0
                
        """
        We start iterating from index `2` 
        because we need **three elements** 
        (`nums[i-2], nums[i-1], nums[i]`) 
        to check if they form an arithmetic pattern.

        So at each step, 
        we’re looking at a triplet ending at index `i`.
        """
        
        return total

"""
test_cases = [
        #  Basic cases
        ([1, 2, 3, 4], 3),      # [1,2,3], [2,3,4], [1,2,3,4]
        ([1, 3, 5, 7, 9], 6),   # all diffs = 2; 
                                total slices = 6
        
        #  Edge cases
        ([1, 2], 0),            # less than 3 elements → 0
        ([1, 1, 1], 1),         # [1,1,1] itself is arithmetic
        ([1], 0),               # single element
        ([], 0),                # empty array
        ]
"""