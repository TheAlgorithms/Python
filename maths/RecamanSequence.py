# number in Recaman's sequence

# Prints first n terms of Recaman
# sequence
def recaman(n):
	# Create an array to store terms
	arr = [0] * n
	# First term of the sequence
	# is always 0
	arr[0] = 0
	print(arr[0], end=", ")
	# Fill remaining terms using
	# recursive formula.
	for i in range(1, n):
		curr = arr[i-1] - i
		for j in range(0, i):
			# If arr[i-1] - i is
			# negative or already
			# exists.
			if ((arr[j] == curr) or curr < 0):
				curr = arr[i-1] + i
				break
		arr[i] = curr
		print(arr[i], end=", ")
# Driver code
n = 17
recaman(n)
