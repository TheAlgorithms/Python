"""
Total number of non-decreasing numbers with n digits
A number is non-decreasing if every digit (except the first one) is greater 
an or equal to previous digit. For example, 223, 4455567, 899, are 
non-decreasing numbers.
So, given the number of digits n, you are required to find the count of 
total non-decreasing numbers with n digits.

Examples:
Input:  n = 1
Output: count  = 10

Input:  n = 2
Output: count  = 55

Input:  n = 3
Output: count  = 220

"""


def Totaldigits(n):
	count=0
	for i in range(10**n):
		if Accending(i):
			count+=1
	return count

def Accending(num):
	temp2=10
	while num>0:
		temp1=num%10
		num=num//10
		if temp1<=temp2:
			temp2=temp1
		else:
			return False
	return True