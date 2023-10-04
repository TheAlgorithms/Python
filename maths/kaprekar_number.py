# Python program to check if a number is Kaprekar number or not

import math

# Returns true if n is a Kaprekar number, else false
def iskaprekar(n):
	if n == 1 :
		return True
	
	#Counting number of digits in square
	sq_n = n * n
	count_digits = 1
	while not sq_n == 0 :
		count_digits = count_digits + 1
		sq_n = sq_n // 10
	
	sq_n = n*n # Recompute square as it was changed
	
	# Split the square at different points and see if sum
	# of any pair of splitted numbers is equal to n.
	r_digits = 0
	while r_digits< count_digits :
		r_digits = r_digits + 1
		eq_parts = (int) (math.pow(10, r_digits))
		
		# To avoid numbers like 10, 100, 1000 (These are not
		# Kaprekar numbers
		if eq_parts == n :
			continue
		
		# Find sum of current parts and compare with n
		
		sum = sq_n//eq_parts + sq_n % eq_parts
		if sum == n :
			return True
	
	# compare with original number
	return False

i = input("Enter the number to check:")
if (iskaprekar(i)) :
	print ("The number is a Kaprekar number",end=" ")
else:
	print("The number is not a Kaprekar number",end=" ")

