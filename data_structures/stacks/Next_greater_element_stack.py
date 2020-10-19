
# Function for implementation of NGE 
def NGE(arr): 

	# Iterate through array to check for greatest element 
	for i in range(0, len(arr)): 

		# Find the maximum from i to end 
		lead = max(arr[i:]) 

		# If max is same as the i'th number then 
		# print -1 else print the maximum 
		if (arr[i] == lead): 
			print("% d --> % d" % (arr[i], -1)) 
		else: 
			print("% d --> % d" % (arr[i], lead)) 


# Driver program 
def main(): 
	arr = [11, 13, 21, 3, 9, 12] 
	NGE(arr) 
	arr = [10, 9, 8, 7, 6, 5, 4, 3, 2] 
	NGE(arr) 

if __name__ == '__main__': 
	main() 


