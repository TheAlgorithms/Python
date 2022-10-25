# Python Program implementation
# of binary insertion sort


def binary_search(arr, val, start, end):
	
	# we need to distinugish whether we
	# should insert before or after the
	# left boundary. imagine [0] is the last
	# step of the binary search and we need
	# to decide where to insert -1
	if start == end:
		if arr[start] > val:
			return start
		else:
			return start+1

	# this occurs if we are moving
	# beyond left's boundary meaning
	# the left boundary is the least
	# position to find a number greater than val
	if start > end:
		return start

	mid = (start+end)//2
	if arr[mid] < val:
		return binary_search(arr, val, mid+1, end)
	elif arr[mid] > val:
		return binary_search(arr, val, start, mid-1)
	else:
		return mid


def insertion_sort(arr):
	for i in range(1, len(arr)):
		val = arr[i]
		j = binary_search(arr, val, 0, i-1)
		arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
	return arr


print("Sorted array:")
print(insertion_sort([37, 23, 0, 31, 22, 17, 12, 72, 31, 46, 100, 88, 54]))

# Code contributed by Mohit Gupta_OMG
