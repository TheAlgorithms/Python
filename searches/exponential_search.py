# Python program to find an element x
# in a sorted array using Exponential Search

# A recursive binary search function returns
# location of x in given array arr[l..r] is
# present, otherwise -1
def binarySearch( arr, l, r, x):
	if r >= l:
		mid = l + ( r-l ) // 2
		
		# If the element is present at
		# the middle itself
		if arr[mid] == x:
			return mid
		
		# If the element is smaller than mid,
		# then it can only be present in the
		# left subarray
		if arr[mid] > x:
			return binarySearch(arr, l,
								mid - 1, x)
		
		# Else he element can only be
		# present in the right
		return binarySearch(arr, mid + 1, r, x)
		
	# We reach here if the element is not present
	return -1

# Returns the position of first
# occurrence of x in array
def exponentialSearch(arr, n, x):
	# IF x is present at first
	# location itself
	if arr[0] == x:
		return 0
		
	# Find range for binary search
	# j by repeated doubling
	i = 1
	while i < n and arr[i] <= x:
		i = i * 2
	
	# Call binary search for the found range
	return binarySearch( arr, i // 2,
						min(i, n-1), x)
	

# Driver Code
arr = []
n = int(input())
for i in range(0, n):
    ele = int(input())
  
    arr.append(ele)
x = int(input())
result = exponentialSearch(arr, n, x)
if result == -1:
	print ("Not found")
else:
	print ("Element is present at index %d" %(result))

#contributed by Sohini Joarder
