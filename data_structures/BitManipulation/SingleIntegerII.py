'''
Problem Description
Given an array of integers, every element appears thrice except for one which occurs once.

Find that element which does not appear thrice.

NOTE: Your algorithm should have a linear runtime complexity.

Could you implement it without using extra memory?

'''
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def singleNumber(self, A):
	    n=len(A)
	    m=0
	    temp=1
	    for j in range (0,32):
	        c0=0
	        c1=0
	        for i in range (0,n):
	            if A[i]& temp:
	                c1+=1
	            else:
	                c0+=1
	        if c0%3:
	            m+=pow(2,j)*0
	        else:
	            m+=pow(2,j)*1
	        temp=temp<<1
        return m

