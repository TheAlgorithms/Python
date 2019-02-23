from __future__ import print_function

try:
	xrange			#Python 2
except NameError:
	xrange = range	#Python 3

def fibonacci(n):
	if n == 1 or type(n) is not int:
		return 0
	elif n == 2:
		return 1
	else:
		sequence = [0, 1]
		for i in xrange(2, n+1):
			sequence.append(sequence[i-1] + sequence[i-2])

		return sequence[n]

def fibonacci_digits_index(n):
	digits = 0
	index = 2

	while digits < n:
		index += 1
		digits = len(str(fibonacci(index)))

	return index

if __name__ == '__main__':
	print(fibonacci_digits_index(1000))