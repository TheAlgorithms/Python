'''
Problem Description
Given an array of integers, every element appears twice except for one. Find that single one.

NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


Problem Constraints
2 <= N <= 2000000
0 <= A[i] <= INTMAX
 


Input Format
First and only argument of input contains an integer array A.


Output Format
Return a single integer denoting the single element.


Example Input
Input 1:
 A = [1, 2, 2, 3, 1]
Input 2:
 A = [1, 2, 2]
  


Example Output
Output 1:
 3
Output 2:
 1
 


Example Explanation
 3 occurs only once.
 So the answer is 3.
'''



class Solution:
	# @param A : tuple of integers
	# @return an integer
	def singleNumber(self, A):
        n=len(A)
        ans=A[0]
        for i in range (1,n):
            ans=A[i]^ans
        
        return ans

