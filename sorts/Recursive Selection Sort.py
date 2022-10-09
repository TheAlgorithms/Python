# Recursive Python3 code to sort
# an array using selection sort

# Return minimum index
def minIndex( a , i , j ):
	if i == j:
		return i
		
	# Find minimum of remaining elements
	k = minIndex(a, i + 1, j)
	
	# Return minimum of current
	# and remaining.
	return (i if a[i] < a[k] else k)
	
# Recursive selection sort. n is
# size of a[] and index is index of
# starting element.
def recurSelectionSort(a, n, index = 0):

	# Return when starting and
	# size are same
	if index == n:
		return -1
		
	# calling minimum index function
	# for minimum index
	k = minIndex(a, index, n-1)
	
	# Swapping when index and minimum
	# index are not same
	if k != index:
		a[k], a[index] = a[index], a[k]
		
	# Recursively calling selection
	# sort function
	recurSelectionSort(a, n, index + 1)
	
# Driver code
arr = [3, 1, 5, 2, 7, 0]
n = len(arr)

# Calling function
recurSelectionSort(arr, n)

# printing sorted array
for i in arr:
	print(i, end = ' ')
	
# This code is contributed by "Sharad_Bhardwaj".
