from __future__ import print_function
from math import ceil

def diagonal_sum(n):
	total = 1

	for i in xrange(1, int(ceil(n/2.0))):
		odd = 2*i+1
		even = 2*i
		total = total + 4*odd**2 - 6*even

	return total

if __name__ == '__main__':
	import sys

	if len(sys.argv) == 1:
		print(diagonal_sum(1001))
	else:
		try:
			n = int(sys.argv[1])
			diagonal_sum(n)
		except ValueError:
			print('Invalid entry - please enter a number')