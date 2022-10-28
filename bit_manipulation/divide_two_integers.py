"""
Estimate the most significant bit of the divisor. This can be easily calculated by 
repeating the position of bit i from 31 to 1. Find the first bit where the divisor << i
is less than the dividend and keep updating the ith bit position where it is true. Add 
the result to the temp variable to check the next position such that (temp + (divisor << i)) is less than the dividend.
Return the final answer of the quotient after updating with a matching sign.

"""

import math


def divide(dividend, divisor):
	if dividend == 0:
		return 0
	if divisor == 0:
		# If divisor is 0, return the maximum integer value (4 byte)
		print("Division by 0 is impossible\n")
		return 2**31 - 1
	"""
	Calculate sign of divisor i.e.,
	sign will be negative only if
	either one of them is negative
	otherwise it will be positive
	"""
	sign = (divisor < 0) ^ (dividend < 0)
	# abs() : function used to get the absolute values for divisor and dividend
	dividend = abs(dividend)
	divisor = abs(divisor)

	# Ternary way to write a condition in python
	if divisor == 1:
		return dividend if(sign == 0) else -dividend

	"""
	log() : function used to get the logarithmic value of the entered value [Gives the natural log of the entered number]
	exp() : Return the e^(entered value)
	"""
	ans = math.exp(math.log(abs(dividend)) - math.log(abs(divisor)))
	"""
	adding 0.0000000001 to compensate for the precision errors
	like for a = 18 and b = -6,
	result after exponentiation will be 2.999999999...
	adding 0.0000000001, sets it right
	"""
	return ans if(sign == 0) else -ans


dividend, divisor = 10, 3
print(divide(dividend, divisor))
