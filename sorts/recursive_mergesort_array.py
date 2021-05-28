## Documentation: https://en.wikipedia.org/wiki/Merge_sort
def merge(arr):
	"""Return a sorted array.
	>>> merge([10,9,8,7,6,5,4,3,2,1])
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	>>> merge([1,2,3,4,5,6,7,8,9,10])
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	>>> merge([10,22,1,2,3,9,15,23])
	[1, 2, 3, 9, 10, 15, 22, 23]
	"""
	if(len(arr) > 1):
		middle = len(arr) // 2
		left = arr[:middle]
		right = arr[middle:]
		leftSize = len(left)
		rightSize = len(right)
		l = merge(left)
		r = merge(right)
		i = 0
		j = 0
		k = 0
		while(i < leftSize and j < rightSize):
			if(left[i] < right[j]):
				arr[k] = left[i]
				i = i + 1
			else:
				arr[k] = right[j]
				j = j + 1
			k = k + 1
		while(i < leftSize):
				arr[k] = left[i]
				i = i + 1
				k = k + 1
		while(j < rightSize):
				arr[k] = right[j]
				j = j + 1
				k = k + 1
	return arr

if __name__ == "__main__":
    import doctest
    doctest.testmod()
