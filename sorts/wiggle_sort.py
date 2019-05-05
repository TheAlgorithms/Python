"""
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....  
For example:
if input numbers = [3, 5, 2, 1, 6, 4] 
one possible Wiggle Sorted answer is [3, 5, 1, 6, 2, 4].
"""
def wiggle_sort(nums):
    for i in range(len(nums)):
        if (i % 2 == 1) == (nums[i-1] > nums[i]):
            nums[i-1], nums[i] = nums[i], nums[i-1]

if __name__ == '__main__':
    print("Enter the array elements:\n")
    array=list(map(int,input().split()))
    print("The unsorted array is:\n")
    print(array)
    wiggle_sort(array)
    print("Array after Wiggle sort:\n")
    print(array)
