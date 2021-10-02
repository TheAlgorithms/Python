def wave_sort(arr, n): 
"""
Python function to sort the array arr[0..n-1] in wave form,
i.e., arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= arr[5]
"""
	
	for i in range(0, n, 2): 
		
    # If current even element is smaller than previous
		if (i> 0 and arr[i] < arr[i-1]): 
			arr[i],arr[i-1] = arr[i-1],arr[i] 
		
    # If current even element is smaller than next
		if (i < n-1 and arr[i] < arr[i+1]): 
			arr[i],arr[i+1] = arr[i+1],arr[i] 

arr = [22,10,3,12,21,1,200] 

wave_sort(arr, len(arr)) 
print(arr)
