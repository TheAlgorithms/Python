#!/usr/bin/env python3

"""
Python3 Program for recursive binary search.
"""  
# Returns index of x in arr if present, else -1
def binarySearch (arr, l, r, x):
    
    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it 
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        # Else the element can only be present 
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


if __name__ == "__main__":
    arr = input("Enter numbers separated by comma:\n").strip()
    target = int(input("Enter a single number to be found in the list:\n"))
    
    # Function call
    result = binarySearch(arr, 0, len(arr)-1, target)

    if result != -1:
        print ("Element is present at index % d" % result)
    else:
        print ("Element is not present in array")