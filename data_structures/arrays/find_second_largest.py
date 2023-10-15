def print2largest(arr, arr_size): 
  
    # There should be 
    # atleast two elements 
    if (arr_size < 2): 
        print(" Invalid Input ") 
        return
  
    # Sort the array 
    arr.sort 
  
    # Start from second last 
    # element as the largest 
    # element is at last 
    for i in range(arr_size-2, -1, -1): 
  
        # If the element is not 
        # equal to largest element 
        if (arr[i] != arr[arr_size - 1]): 
  
            print("The second largest element is", arr[i]) 
            return
  
    print("There is no second largest element") 
  
  
# Driver code 
arr = [12, 35, 1, 10, 34, 1] 
n = len(arr) 
print2largest(arr, n) 
