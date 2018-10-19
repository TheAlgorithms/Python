from __future__ import print_function
from math import factorial

def lattice_paths(n):
	n = 2*n #middle entry of odd rows starting at row 3 is the solution for n = 1, 2, 3,...
	k = n/2

	return factorial(n)/(factorial(k)*factorial(n-k))

if __name__ == '__main__':
	import sys

	if len(sys.argv) == 1:
		print(lattice_paths(20))
	else:
		try:
			n = int(sys.argv[1])
			print(lattice_paths(n))
		except ValueError:
			print('Invalid entry - please enter a number.')
