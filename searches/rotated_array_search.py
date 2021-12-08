'''
Description: 

To be used on a 1 dimensional list of numbers. Say you have been given a list of numbers, in this example the list 
is named nums, that was sorted, the list is then roated by an unknown pivot index, X. The array now becomes 
[nums[x], nums[x+1], ..., nums[n-1], nums[0], nums[1], ..., nums[x-1]]. If you wanted to find
a number in this list.

This algoirhtm allows you to find the index of the number in a rotated list in O(log(n)) time. 

Class Description: 

The main Function in the class rotated_array_search is search(nums, target). nums is a list of numbers of 
finite size, target is the number being searched for. This function will return the index of target
or -1 if target does not exist.  

The two helper functions are findPivot and helper. Find pivot performs a modified binary search to find the 
index of the pivot. helper performs binary search on the sub list. The sublist will be either from 0 to
pivot-1 or from pivot to length of list. 

Examples:


Input: nums = [7,8,9,10,11,1,2,3], target = 1
Output: 5

Explanation: 1 exists in the rotated list at index 5


Input: nums = [7,8,9,10,11,1,2,3], target = 12
Output: -1

Explanation: 12 does not exist in the rotated list so -1 is returned
'''


class rotated_array_search:
    def search(self, nums, target):
        if not nums or len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        pivot = self.findPivot(nums)
        if pivot == 0:
            return self.helper(nums, 0, len(nums)-1, target)
        if target <= nums[pivot-1] and target >= nums[0]:
            return self.helper(nums, 0, pivot-1, target)
        else:
            return self.helper(nums, pivot, len(nums)-1, target)

    def findPivot(self, arr):
        l = 0
        r = len(arr)-1
        while l <= r:
            m = l + (r-l)//2
            if (m == 0 and arr[m] < arr[m+1]) or (m == len(arr)-1 and arr[m] < arr[m-1]) or arr[m] < arr[m-1]:
                return m
            elif arr[m] < arr[r]:
                r = m-1
            else:
                l = m+1

    def helper(self, arr, l, r, x):
        while l <= r:
            m = l + (r-l)//2
            if arr[m] == x:
                return m
            elif arr[m] > x:
                r = m-1
            else:
                l = m+1
        return -1


# Example runs
# creates example object to run the following below examples
example = rotated_array_search()
# prints 5, see description at top of page
print(example.search([7, 8, 9, 10, 11, 1, 2, 3], 1))
# prints -1, see description at top of page
print(example.search([7, 8, 9, 10, 11, 1, 2, 3], 12))
