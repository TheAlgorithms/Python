def largestGCDSubsequence(arr, n):
    ans = 0
 
    maxele = max(arr)
 
    for i in range(2, maxele + 1):
        count = 0
        for j in range(n):
            if (arr[j] % i == 0):
                count += 1
        ans = max(ans, count)
 
    return ans
if __name__ == '__main__':
    arr = [3, 6, 2, 5, 4]
    size = len(arr)
    print(largestGCDSubsequence(arr, size))
