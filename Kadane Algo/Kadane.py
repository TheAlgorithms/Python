#Author-Prajul Gupta
# Python program to find maximum contiguous subarray 
   
# Function to find the maximum contiguous subarray 
from sys import maxint 
def maxSubArraySum(a,size): 
       
    max_so_far = -maxint - 1
    max_ending_here = 0
       
    for i in range(0, size): 
        max_ending_here = max_ending_here + a[i] 
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
  
        if max_ending_here < 0: 
            max_ending_here = 0   
    return max_so_far 
   
# Driver function to check the above function  
if __name__ == "__main__":
    arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22] 
    print("Maximum contiguous sum for array is", maxSubArraySum(arr,len(a)))