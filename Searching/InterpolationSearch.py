
def interpolationSearch(arr, n, x): 
	# Find indexs of two corners 
	lo = 0
	hi = (n - 1) 

	
	while lo <= hi and x >= arr[lo] and x <= arr[hi]: 
		if lo == hi: 
			if arr[lo] == x: 
				return lo; 
			return -1; 
		
		 
		pos = lo + int(((float(hi - lo) /
			( arr[hi] - arr[lo])) * ( x - arr[lo]))) 

		# Condition of target found 
		if arr[pos] == x: 
			return pos 

		# If x is larger, x is in upper part 
		if arr[pos] < x: 
			lo = pos + 1; 

		# If x is smaller, x is in lower part 
		else: 
			hi = pos - 1; 
	
	return -1

# Driver Code 
# Array of items oin which search will be conducted 
arr = [10, 12, 13, 16, 18, 19, 20, 21, \ 
				22, 23, 24, 33, 35, 42, 47] 
n = len(arr) 

x = 18 # Element to be searched 
index = interpolationSearch(arr, n, x) 

if index != -1: 
	print "Element found at index",index 
else: 
	print "Element not found"

