# Python3 the implementation to sort an  
# array of size n 
  
# A function to do counting sort of arr[]  
# according to the digit represented by exp.  
def countSort(arr, n, exp):  
    output = [0] * n # output array  
    count = [0] * n 
    for i in range(n): 
        count[i] = 0
  
    # Store count of occurrences in count[]  
    for i in range(n): 
        count[ (arr[i] // exp) % n ] += 1
  
    # Change count[i] so that count[i] now contains  
    # actual position of this digit in output[]  
    for i in range(1, n):  
        count[i] += count[i - 1]  
  
    # Build the output array  
    for i in range(n - 1, -1, -1):  
  
        output[count[ (arr[i] // exp) % n] - 1] = arr[i]  
        count[(arr[i] // exp) % n] -= 1
  
    # Copy the output array to arr[], so that  
    # arr[] now contains sorted numbers according  
    # to current digit  
    for i in range(n):  
        arr[i] = output[i]  
  
# The main function to that sorts arr[] of  
# size n using Radix Sort  
def sort(arr, n) : 
      
    # Do counting sort for first digit in base n.  
    # Note that instead of passing digit number, 
    # exp (n^0 = 1) is passed.  
    countSort(arr, n, 1)  
  
    # Do counting sort for second digit in base n.  
    # Note that instead of passing digit number,  
    # exp (n^1 = n) is passed.  
    countSort(arr, n, n)  
  
# Driver Code 
if __name__ =="__main__":  
      
    # Since array size is 7, elements should 
    # be from 0 to 48  
    arr = [40, 12, 45, 32, 33, 1, 22] 
    n = len(arr)  
    print("Given array is") 
    print(*arr) 
      
    sort(arr, n) 
      
    print("Sorted array is") 
    print(*arr) 
  
# This code is contribute by  
# Shubham Singh(SHUBHAMSINGH10) 
