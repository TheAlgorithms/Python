# Function to check if a string can become empty 
# by recursively deleting a given sub-string 

def checkEmpty(input, pattern): 
	
	 
	if len(input)== 0 and len(pattern)== 0: 
		return 'true'

	if len(pattern)== 0: 
		return 'true'

	while (len(input) != 0): 

		index = input.find(pattern) 
			
		if (index ==(-1)): 
			return 'false'
			
		# slice input string in two parts and concatenate 
		input = input[0:index] + input[index + len(pattern):]			 

	return 'true'

# Driver program 
if __name__ == "__main__": 
	input ='PYTPYTHON'
	pattern ='PYT'
	print checkEmpty(input, pattern) 
