'''
Find longest increasing Subsequence
Input  : arr[] = {3, 10, 2, 1, 20}
Output : Length of LIS = 3
The longest increasing subsequence is 3, 10, 20

Input  : arr[] = {3, 2}
Output : Length of LIS = 1
The longest increasing subsequences are {3} and {2}

Input : arr[] = {50, 3, 10, 7, 40, 80}
Output : Length of LIS = 4
The longest increasing subsequence is {3, 7, 40, 80}
'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        DP = [1]*len(A)
        for i in range(len(A)):
            for j in range(i):
                if A[j] < A[i]:
                    DP[i] = max(DP[i], DP[j]+1)
        return max(DP)
