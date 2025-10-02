def maxSubarraySum(arr):
    ans = arr[0]
  
    for i in range(len(arr)):
        currentSum = 0
      
        for j in range(i, len(arr)):
            currentSum = currentSum + arr[j]
            ans = max(ans, currentSum)
          
    return ans

if __name__ == "__main__":
    arr = list(map(int, input().split(' ')))
    print(maxSubarraySum(arr))
