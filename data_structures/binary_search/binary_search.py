# It returns index of x in given array arr if present,
# else returns -1 such as in this case if you're searching for 6 which is not in the array, it would return False represented by -1.

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1
 
 
# Test array
nums = [ 1, 2, 3, 4, 5 ]
element = 3
 
# Function call
result = binary_search(nums, element)

# Output condition
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
