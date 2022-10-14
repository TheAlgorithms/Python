# iterative implementation
def binarySearch(a, item, low, high):
	while (low <= high):
		mid = low + (high - low) // 2
		if (item == a[mid]):
			return mid + 1
		elif (item > a[mid]):
			low = mid + 1
		else:
			high = mid - 1
	return low
	
# Function to sort an array a[] of size 'n'
def insertionSort(a, n):
	for i in range (n):
		j = i - 1
		selected = a[i]
		
		# find location where selected should be inseretd
		loc = binarySearch(a, selected, 0, j)
		
		# Move all elements after location to create space
		while (j >= loc):
			a[j + 1] = a[j]
			j-=1
		a[j + 1] = selected


a = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
n = len(a)
insertionSort(a, n)
print("Sorted array: ")
for i in range (n):
	print(a[i], end=" ")


