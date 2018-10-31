from __future__ import print_function
'''
Self Powers
Problem 48

The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
'''

try:
	xrange
except NameError:
	xrange = range

total = 0
for i in xrange(1, 1001):
	total += i**i


print(str(total)[-10:])