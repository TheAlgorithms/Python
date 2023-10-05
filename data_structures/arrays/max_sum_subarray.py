"""
Following is the program to find the maximum sum of subarray of size K using 
Sliding window approach
"""
""""
The fact that the sum of a subarray (or window) of size k can be calculated in O(1) time using the sum of the subarray (or window) of size k before it serves as the foundation for an efficient solution. With the exception of the first subarray of size k, we compute the total for all other subarrays by subtracting the first element from the previous window and adding the final element from the current window.
""""
# O(n) solution in Python3 for finding 
# maximum sum of a subarray of size k
 
# Returns maximum sum in
# a subarray of size k.
def maxSum(arr, n, k):
 
    # k must be smaller than n
    if (n < k):
     
        print("Invalid")
        return -1
     
    # Compute sum of first
    # window of size k
    res = 0
    for i in range(k):
        res += arr[i]
 
    # Compute sums of remaining windows by
    # removing first element of previous
    # window and adding last element of 
    # current window.
    curr_sum = res
    for i in range(k, n):
     
        curr_sum += arr[i] - arr[i-k]
        res = max(res, curr_sum)
 
    return res
 
# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k)

# result
24
