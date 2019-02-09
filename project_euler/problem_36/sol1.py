from __future__ import print_function
'''
Double-base palindromes
Problem 36
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''
try:
	xrange		#Python 2
except NameError:
	xrange = range	#Python 3

def is_palindrome(n):
	n = str(n)

	if n == n[::-1]:
		return True
	else:
		return False

total = 0

for i in xrange(1, 1000000):
	if is_palindrome(i) and is_palindrome(bin(i).split('b')[1]):
		total += i

print(total)