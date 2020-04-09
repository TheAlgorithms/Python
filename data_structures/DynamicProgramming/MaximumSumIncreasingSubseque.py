'''
Given an array of n positive integers. Write a program to find the sum of maximum sum subsequence of the given array such that the integers in the subsequence are sorted in increasing order. For example, if input is {1, 101, 2, 3, 100, 4, 5}, then output should be 106 (1 + 2 + 3 + 100), if the input array is {3, 4, 5, 10}, then output should be 22 (3 + 4 + 5 + 10) and if the input array is {10, 5, 4, 3}, then output should be 10
'''


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def liss(self, A):
        n=len(A)
        ans=[0]*(n)
        
        for i in range (0,n):
            ans[i]=A[i]
            
        for i in range (0,n):
            for j in range (0,i):
                if A[i]>A[j] and ans[i]<ans[j]+A[i]:
                    ans[i]=ans[j]+A[i]
        return max(ans)

