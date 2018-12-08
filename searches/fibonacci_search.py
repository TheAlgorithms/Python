"""
fibonacci search
The idea is to first find the smallest Fibonacci number that is greater
than or equal to the length of given array.
"""

from __future__ import print_function

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

#Fibonacci Search
def fibonacci_search(arr, x, n):
    fibMMm2 = 0  # (m-2)'th Fibonacci No. 
    fibMMm1 = 1   # (m-1)'th Fibonacci No. 
    fibM = fibMMm2 + fibMMm1  # m'th Fibonacci

    # fibM is going to store the smallest Fibonacci 
    # Number greater than or equal to n 
    while (fibM < n): 
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM  = fibMMm2 + fibMMm1
  
    offset = -1
  
    # while there are elements to be inspected. Note that 
    #  we compare arr[fibMm2] with x. When fibM becomes 1, 
    #  fibMm2 becomes 0
    while (fibM > 1):
        # Check if fibMm2 is a valid location
        i = min(offset+fibMMm2, n-1)

        # If x is greater than the value at index fibMm2, 
        #  cut the subarray array from offset to i
        if (arr[i] < x):
            fibM  = fibMMm1
            fibMMm1 = fibMMm2 
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif (arr[i] > x):
            fibM  = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            return i
  

    if(fibMMm1 and arr[offset+1]==x):
        return offset+1
  
    return None


def __assert_sorted(collection):
    if collection != sorted(collection):
        raise ValueError('Collection must be sorted')
        
    return True

if __name__ == '__main__':
    import sys
    user_input = raw_input('Enter numbers separated by comma:\n').strip()
    collection = [int(item) for item in user_input.split(',')]
    
    try:
        __assert_sorted(collection)
    except ValueError:
        sys.exit('Sequence must be sorted to apply binary search')
   
    target_input = raw_input('Enter a single number to be found in the list:\n')
    target = int(target_input)
    
    n = len(collection)
    print("Found at index:", 
            fibonacci_search(collection, target, n))
