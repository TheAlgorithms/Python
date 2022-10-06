"""
A recursive implementation of the selection sort algorithm.

Selection Sort : https://en.wikipedia.org/wiki/Selection_sort#:~:text=In%20computer%20science%2C%20selection%20sort%20is%20an%20in-place,of%20items%20which%20is%20built%20up%20from%20left
"""

# Return min index
def minind(a, i, j):
    if i == j:
        return i
	# Find min of remaining elements
    k = minind(a, i + 1, j)
	# Return min of current and remaining.
    return i if a[i] < a[k] else k

# n is size of a[] and index is index of starting element.
def recursive_selection_sort(a, n, index=0):
 if index == n:
        return -1

    k = minind(a, index, n - 1)

	# Swapping when index and min index are not same
    if k != index:
        a[k], a[index] = a[index], a[k]
		
	# Recursively calling selection sort function
    recursive_selection_sort(a, n, index + 1)


arr = [3, 1, 5, 2, 7, 0]
n = len(arr)

recursive_selection_sort(arr, n)

# printing sorted array
for i in arr:
    print(i, end=" ")
