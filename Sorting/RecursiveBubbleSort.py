def bubble_sort(array):
	'''Function that takes a list and performs
	bubble sort recusrively'''

	for i, num in enumerate(array):
		try:
			if array[i+1] < num:
				array[i] = array[i+1] 
				array[i+1] = num
				bubble_sort(array)
		except IndexError:
			pass
	return array


arr = []
print("Enter Elements:")
arr = [int(num) for num in input().split()]
n = n = len(arr)
bubble_sort(arr)
print("Sorted array:")
for i in range(n):
	print(f"{arr[i]}", end = ' ')
