'''
Problem Description
You are given an array A (containing only 0 and 1) as element of N length. Given L and R, you need to determine value of XOR of all elements from L to R (both inclusive) and number of unset bits (0's) in the given range of the array.


Problem Constraints
1<=N,Q<=100000
1<=L<=R<=N


Input Format
First argument contains the array of size N containing 0 and 1 only. 
Second argument contains a 2D array with Q rows and 2 columns, each row represent a query with 2 columns representing L and R.


Output Format
Return an 2D array of Q rows and 2 columns i.e the xor value and number of unset bits in that range respectively for each query.


Example Input
A=[1,0,0,0,1]
B=[ [2,4],
    [1,5],
    [3,5] ]


Example Output
[[0 3]
[0 3]
[1 2]]


Example Explanation
In the given case the bit sequence is of length 5 and the sequence is 1 0 0 0 1. 
For query 1 the range is (2,4), and the answer is (array[2] xor array[3] xor array[4]) = 0, and number of zeroes are 3, so output is 0 3. 
Similarly for other queries.
'''
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        n = len(A)
        m = len(B)
        count=[0]*n
        ans=[]
        count[0]=A[0]
        for i in range (1,n):
            count[i]=count[i-1]+A[i]
        xor_list=[0]*n
        xor_list[0]=A[0]
        for i in range (1,n):
            xor_list[i]=xor_list[i-1]^A[i]
        
        for i in range (0,m):
            if B[i][0]==1:
                ans.append([xor_list[B[i][1]-1],B[i][1]-B[i][0]+1-count[B[i][1]-1]])
            else:
                ans.append([xor_list[(B[i][1]-1)]^xor_list[(B[i][0]-2)],B[i][1]-B[i][0]+1-count[B[i][1]-1]+count[B[i][0]-2]])
        
        return ans

