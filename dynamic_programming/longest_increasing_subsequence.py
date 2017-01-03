"""
The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order. For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 
"""
def LIS(arr):
    n= len(arr)
    lis = [1]*n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] <= lis[j]:
                lis[i] = lis[j] + 1
    return max(lis)
