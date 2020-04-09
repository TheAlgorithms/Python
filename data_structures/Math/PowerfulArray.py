'''

Problem Description
Given two array of integers A, B of equal size N. Power of an array is defined as the product of all the elements of the array. If the power of array A >= power of array B return 1 else return 0.    


Problem Constraints
1 <= N <= 100000
1 <= A[i], B[i] <= 109


Input Format
First argument is an array of integers A.
Second argument is an array of integers B.


Output Format
Return 1 if power of A >= power of B else return 0.


Example Input
Input 1:
A = [1, 2, 3, 4]
B = [2, 4, 3, 2]
   


Example Output
Output 1:
0
   


Example Explanation
Explanation 1:
Power of A = 24 and Power of B = 48.
So, the answer is 0.
'''



class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n=len(A)
        ans1=0
        ans2=0
    
        for i in range (0,n):
            ans1=ans1+math.log10(A[i])
            ans2=ans2+math.log10(B[i])
        if(ans1>=ans2):
            return 1
        return 0
