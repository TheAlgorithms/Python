def quick_sort(arr):
	n=len(arr)
	if n<=1:
		return arr
	else:
		pivot = arr.pop(0)

		# creating 2 empty lists to segregate greater than pivot elements and less than pivot elements
		lesser_than_pivot = []
		greater_than_pivot = []

		for item in arr:
			if item<pivot:
				lesser_than_pivot.append(item)
			else:
				greater_than_pivot.append(item)
		return quick_sort(lesser_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

arr = [5, 1, 7, 2, 9, 4, 3]
print(quick_sort(arr))