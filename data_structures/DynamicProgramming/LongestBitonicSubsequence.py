'''
Given an array arr[0 … n-1] containing n positive integers, a subsequence of arr[] is called Bitonic if it is first increasing, then decreasing. Write a function that takes an array as argument and returns the length of the longest bitonic subsequence.
A sequence, sorted in increasing order is considered Bitonic with the decreasing part as empty. Similarly, decreasing order sequence is considered Bitonic with the increasing part as empty.

Examples:

Input arr[] = {1, 11, 2, 10, 4, 5, 2, 1};
Output: 6 (A Longest Bitonic Subsequence of length 6 is 1, 2, 10, 4, 2, 1)

Input arr[] = {12, 11, 40, 5, 3, 1}
Output: 5 (A Longest Bitonic Subsequence of length 5 is 12, 11, 5, 3, 1)

Input arr[] = {80, 60, 30, 40, 20, 10}
Output: 5 (A Longest Bitonic Subsequence of length 5 is 80, 60, 30, 20, 10)
'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lbs(self, A):
        n=len(A)
        lis=[0]*(n)

        for i in range (0,n):
            lis[i]=1

        for i in range (0,n):
            for j in range (0,i):
                if A[i]>A[j] and lis[i]<lis[j]+1:
                    lis[i]=lis[j]+1
        
        lds=[0]*(n)

        for i in range (0,n):
            lds[i]=1

        for i in range (n-1,-1,-1):
            for j in range (n-1,i,-1):
                if A[i]>A[j] and lds[i]<lds[j]+1:
                    lds[i]=lds[j]+1
                    
        max=-1
        
        for i in range (0,n):
            if lis[i]+lds[i]>max:
                max=lis[i]+lds[i]-1
                
        return max
                


