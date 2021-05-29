def merge(arr: list[int]) -> list[int]:
	"""Return a sorted array.
	>>> merge([10,9,8,7,6,5,4,3,2,1])
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	>>> merge([1,2,3,4,5,6,7,8,9,10])
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	>>> merge([10,22,1,2,3,9,15,23])
	[1, 2, 3, 9, 10, 15, 22, 23]
	"""
	if len(arr) > 1:
		middle_length = len(arr) // 2
		left_array = arr[:middle_length]
		right_array = arr[middle_length:]
		left_size = len(left_array)
		right_size = len(right_array)
		l = merge(left_array)
		r = merge(right_array)
		i = 0
		j = 0
		k = 0
		while(i < left_size and j < right_size):
			if left_array[i] < right_array[j]:
				arr[k] = left_array[i]
				i = i + 1
			else:
				arr[k] = right_array[j]
				j = j + 1
			k = k + 1
		while i < left_size:
				arr[k] = left_array[i]
				i = i + 1
				k = k + 1
		while(j < right_size):
				arr[k] = right_array[j]
				j = j + 1
				k = k + 1
	return arr

if __name__ == "__main__":
    import doctest
    doctest.testmod()
