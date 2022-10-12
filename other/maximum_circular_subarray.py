# The function returns maximum circular contiguous sum in a[]
def maxCircularSum(a, n):
  """
  Input: arr[] = {8, -7, 9, -9, 10, -11, 12}
  Output: 22 
  Explanation: Subarray 12, 8, -7, 9, -9, 10 gives the maximum sum, that is 23.
  """
     
    # Edge Case
    if (n == 1):
        return a[0]
 
    # Sum variable which stores the total sum of the array.
    sum = 0
    for i in range(n):
        sum += a[i]
 
    # Every variable stores the first value of array.
    current_max = a[0]
    max_so_far = a[0]
    current_min = a[0]
    min_so_far = a[0]
 
    # Concept of Kadane's Algorithm
    for i in range(1, n):
       
        # Kadane's Algorithm to find Maximum subarray sum.
        current_max = max(current_max + a[i], a[i])
        max_so_far = max(max_so_far, current_max)
 
        # Kadane's Algorithm to find Minimum subarray sum.
        current_min = min(current_min + a[i], a[i])
        min_so_far = min(min_so_far, current_min)
    if (min_so_far == sum):
        return max_so_far
 
    # returning the maximum value
    return max(max_so_far, sum - min_so_far)
 
if __name__ == "__main__":
    n = int(input("Enter number of elements : ").strip())
    a = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
    print("Maximum circular sum is", maxCircularSum(a, n))
