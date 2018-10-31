from __future__ import print_function
'''
Counting Summations
Problem 76

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
'''
try:
	xrange		#Python 2
except NameError:
	xrange = range	#Python 3

def partition(m):
	memo = [[0 for _ in xrange(m)] for _ in xrange(m+1)]
	for i in xrange(m+1):
		memo[i][0] = 1

	for n in xrange(m+1):
		for k in xrange(1, m):
			memo[n][k] += memo[n][k-1]
			if n > k:
				memo[n][k] += memo[n-k-1][k]

	return (memo[m][m-1] - 1)

print(partition(100))