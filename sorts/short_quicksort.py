def QuickSort(A):
	n=len(A)
	if n<=1:
		return A
	else:
		pivot = A.pop(0)
		lesser = []
		greater = []

		for item in A:
			if item<pivot:
				lesser.append(item)
			else:
				greater.append(item)
		return QuickSort(lesser) + [pivot] + QuickSort(greater)

# A = [5, 1, 7, 2, 9, 4, 3]
print("Enter the elements: ")
x= [int(p) for p in input().split()]

print(QuickSort(x))