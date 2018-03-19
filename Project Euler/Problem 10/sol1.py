from __future__ import print_function
from math import sqrt

try:
	xrange          # Python 2
except NameError:
	xrange = range  # Python 3


def is_prime(n):
	for i in xrange(2, int(sqrt(n))+1):
		if n%i == 0:
			return False

	return True

def sum_of_primes(n):
	if n > 2:
		sumOfPrimes = 2
	else:
		return 0

	for i in xrange(3, n, 2):
		if is_prime(i):
			sumOfPrimes += i

	return sumOfPrimes

if __name__ == '__main__':
	import sys

	if len(sys.argv) == 1:
		print(sum_of_primes(2000000))
	else:
		try:
			n = int(sys.argv[1])
			print(sum_of_primes(n))
		except ValueError:
			print('Invalid entry - please enter a number.')
