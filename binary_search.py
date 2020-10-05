def binary_search(l, x): 
    low = 0
    high = len(l) - 1
    mid = 0  
    while low <= high: 
        mid = (high + low) // 2
        if l[mid] < x: 
            low = mid + 1
        elif l[mid] > x: 
            high = mid - 1
        else: 
            return mid 
    return -1
l = [1,2,3,4,5,6] 
x = 5
result = binary_search(l, x) 
if result != -1: 
    print("Element is present at index %d" %result) 
else: 
    print("Element is not present in array")
