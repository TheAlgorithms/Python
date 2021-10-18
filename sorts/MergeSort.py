# Python3 program to sort an array using
# takes O(1) extra space.
def merge(arr, beg, mid, end, maxele):
	
	i = beg
	j = mid + 1
	k = beg
	
	while (i <= mid and j <= end):
		if (arr[i] % maxele <= arr[j] % maxele):
			arr[k] = arr[k] + (arr[i] %
					maxele) * maxele
			k += 1
			i += 1
		else:
			arr[k] = arr[k] + (arr[j] %
					maxele) * maxele
			k += 1
			j += 1
			
	while (i <= mid):
		arr[k] = arr[k] + (arr[i] %
				maxele) * maxele
		k += 1
		i += 1
	while (j <= end):
		arr[k] = arr[k] + (arr[j] %
				maxele) * maxele
		k += 1
		j += 1

	
	for i in range(beg, end + 1):
		arr[i] = arr[i] // maxele

def mergeSortRec(arr, beg, end, maxele):
	
	if (beg < end):
		mid = (beg + end) // 2
		mergeSortRec(arr, beg, mid, maxele)
		mergeSortRec(arr, mid + 1, end, maxele)
		merge(arr, beg, mid, end, maxele)

def mergeSort(arr, n):
	
maxele = max(arr) + 1
mergeSortRec(arr, 0, n - 1, maxele)


if __name__ == '__main__':

	arr = [ 999, 612, 589, 856, 56, 945, 243 ]
	n = len(arr)
	mergeSort(arr, n)

	print("Sorted array")
	
	for i in range(n):
		print(arr[i], end = " ")


