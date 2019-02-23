from __future__ import print_function

try:
	xrange		#Python 2
except NameError:
	xrange = range	#Python 3

try:
	raw_input		#Python 2
except NameError:
	raw_input = input	#Python 3

'''
The number of partitions of a number n into at least k parts equals the number of partitions into exactly k parts
plus the number of partitions into at least k-1 parts. Subtracting 1 from each part of a partition of n into k parts
gives a partition of n-k into k parts. These two facts together are used for this algorithm.
'''
def partition(m):
	memo = [[0 for _ in xrange(m)] for _ in xrange(m+1)]
	for i in xrange(m+1):
		memo[i][0] = 1

	for n in xrange(m+1):
		for k in xrange(1, m):
			memo[n][k] += memo[n][k-1]
			if n-k > 0:
				memo[n][k] += memo[n-k-1][k]

	return memo[m][m-1]

if __name__ == '__main__':
	import sys

	if len(sys.argv) == 1:
		try:
			n = int(raw_input('Enter a number: '))
			print(partition(n))
		except ValueError:
			print('Please enter a number.')
	else:
		try:
			n = int(sys.argv[1])
			print(partition(n))
		except ValueError:
			print('Please pass a number.')