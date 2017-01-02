"""
LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily continious.
Example:"abc", "abg" are subsequences of "abcdefgh". 
"""
def LCS(s1, s2):
    m = len(s1)
    n = len(s2)

    arr = [[0 for i in range(n+1)]for j in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                arr[i][j] = arr[i-1][j-1]+1
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])
    return arr[m][n]
