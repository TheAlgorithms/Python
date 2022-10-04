def maxTrappedWater(arr, n):
	size = n - 1
	prev = arr[0]
	prev_index = 0
	water = 0
	temp = 0
	for i in range(1, size + 1):
		if (arr[i] >= prev):
			prev = arr[i]
			prev_index = i
			temp = 0
		else:
			water += prev - arr[i]
			temp += prev - arr[i]
      
	if (prev_index < size):
		water -= temp
		prev = arr[size]
		for i in range(size, prev_index - 1, -1):
			if (arr[i] >= prev):
				prev = arr[i]
			else:
				water += prev - arr[i]
	return water



if __name__ == '__main__':
	arr = [0, 6, 0, 4, 1, 3, 2, 6, 1, 2, 1,3]
	N = len(arr)
	print(maxTrappedWater(arr, N))
