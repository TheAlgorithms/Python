def bubbleSort(arr): 
	n = len(a) 

	for i in range(n): 

		for j in range(0, n-i-1): 

			if a[j] > a[j+1] : 
				a[j], a[j+1] = a[j+1], a[j] 

a = [5, 4, 2, 1, 8, 0, 100] 

bubbleSort(arr) 

print ("Sorted array is:") 
for i in range(len(arr)): 
	print ("%d" %arr[i]), 
