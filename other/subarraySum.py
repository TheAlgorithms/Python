"""defaultdict documentation -> https://docs.python.org/3.3/library/collections.html"""

def subarraySum(nums, k):
        count = curr_sum = 0
        h = defaultdict(int)
        for num in nums:
            # current prefix sum
            curr_sum += num
            
            # situation 1:
            # continuous subarray starts 
            # from the beginning of the array
            if curr_sum == k:
                count += 1
            
            # situation 2:
            # number of times the curr_sum − k has occurred already, 
            # determines the number of times a subarray with sum k 
            # has occurred up to the current index
            count += h[curr_sum - k]
            
            # add the current sum
            h[curr_sum] += 1
                
        return count
 
