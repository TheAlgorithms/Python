#Function to left rotate arr[] of size n by d*/ 
def leftRotate(arr, d, n): 
	for i in range(d): 
		leftRotatebyOne(arr, n) 

#Function to left Rotate arr[] of size n by 1*/ 
def leftRotatebyOne(arr, n): 
	temp = arr[0] 
	for i in range(n-1): 
		arr[i] = arr[i+1] 
	arr[n-1] = temp 
		

# utility function to print an array */ 
def printArray(arr,size): 
	for i in range(size): 
		print ("%d"% arr[i],end=" ") 


# Driver program to test above functions */ 
arr = [1, 2, 3, 4, 5, 6, 7] 
leftRotate(arr, 2, 7) 
printArray(arr, 7) 

# This code is contributed by Shreyanshi Arun 
