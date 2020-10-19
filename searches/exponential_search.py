"""
Exponential search (also called doubling search or galloping search or Struzik search) is a 
searching technique for sorted, unbounded/infinite lists.

Time Complexity  : O(Log n)
Space Complexity : O(1)
"""

# Binary search algorithm to return the position of
# key x in the sublist A[left..right]
def binarySearch(A, left, right, x):

	# Base condition (search space is exhausted)
	if left > right:
		return -1

	# we find the mid value in the search space and
	# compares it with key value

	mid = (left + right) // 2

	# overflow can happen. Use below
	# mid = left + (right - left) // 2

	# Base condition (key value is found)
	if x == A[mid]:
		return mid

	# discard all elements in the right search space
	# including the mid element
	elif x < A[mid]:
		return binarySearch(A, left, mid - 1, x)

	# discard all elements in the left search space
	# including the mid element
	else:
		return binarySearch(A, mid + 1, right, x)


# Returns the position of key x in the list A of length n
def exponentialSearch(A, x):

	bound = 1

	# find the range in which the key x would reside
	while bound < len(A) and A[bound] < x:
		bound *= 2  # calculate the next power of 2

	# call binary search on A[bound/2 .. min(bound, n)]
	return binarySearch(A, bound // 2, min(bound, len(A)), x)


if __name__ == '__main__':

	A = [2, 5, 6, 8, 9, 10]
	key = 9

	index = exponentialSearch(A, key)

	if index != -1:
		print("Element found at index", index)
	else:
		print("Element found not in the list")
