def maximumSubarraySum(arr):
       n = len(arr)
       maxSum = -1e8
       currSum = 0

       for i in range(0, n):
           currSum = currSum + arr[i]
           if(currSum > maxSum):
               maxSum = currSum
           if(currSum < 0):
               currSum = 0
      
       return maxSum

if __name__ == "__main__":
    # Your code goes here
    arr = [1, 2, -54, 34, 22, 55, -22]    #input your array here
    print(maximumSubarraySum(arr))