def three_sum(nums):
    # Sort the array to simplify the problem
    nums.sort()
    result = []
    
    # Iterate over the array
    for i in range(len(nums)):
        # Skip duplicates for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Two pointers approach
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                # Found a valid triplet
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                
                # Skip duplicates for the second and third elements
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            
            elif total < 0:
                # Move the left pointer to increase the sum
                left += 1
            else:
                # Move the right pointer to decrease the sum
                right -= 1
    
    return result
