"""
Partition problem
Partition problem is to determine whether a given set can be partitioned into two 
subsets such that the sum of elements in both subsets is same.

arr[] = {1, 5, 11, 5}
Output: true 
The array can be partitioned as {1, 5, 5} and {11}

arr[] = {1, 5, 3}
Output: false 
The array cannot be partitioned into equal sum sets.
"""

def isSubsetSum (arr, n, sum): 
    # Base Cases 
    if sum == 0: 
        return True
    if n == 0 and sum != 0: 
        return False
  
    # If last element is greater than sum, then  
    # ignore it 
    if arr[n-1] > sum: 
        return isSubsetSum (arr, n-1, sum) 
  
    ''' else, check if sum can be obtained by any of  
    the following 
    (a) including the last element 
    (b) excluding the last element'''
      
    return isSubsetSum (arr, n-1, sum) or isSubsetSum (arr, n-1, sum-arr[n-1]) 
  
# Returns true if arr[] can be partitioned in two 
# subsets of equal sum, otherwise false 
def findPartion (arr, n): 
    # Calculate sum of the elements in array 
    sum = 0
    for i in range(0, n): 
        sum += arr[i] 
    # If sum is odd, there cannot be two subsets  
    # with equal sum 
    if sum % 2 != 0: 
        return False 
  
    # Find if there is subset with sum equal to 
    # half of total sum 
    return isSubsetSum (arr, n, sum // 2)