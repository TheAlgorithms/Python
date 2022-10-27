"""
Program to find max length of valid paranthesis
author : aakash_2001
"""
def find_max_len(string : str) -> int:

	"""
	function to find max length of valid paranthesis in an input
	:param string : string
	>>> find_max_len('())()') 
	2
	"""
	n = len(string)

	# Create a stack and push -1
	# as initial index to it.
	stk = []
	stk.append(-1)

	# Initialize result
	result = 0

	# Traverse all characters of given string
	for i in range(n):

		# If opening bracket, push index of it
		if string[i] == '(':
			stk.append(i)
		
		# If closing bracket, i.e., str[i] = ')'
		else:

			# Pop the previous opening bracket's index
			if len(stk) != 0:
			    stk.pop()

			# Check if this length formed with base of
			# current valid substring is more than max
			# so far
			if len(stk) != 0:
				result = max(result,
							i - stk[len(stk)-1])

			# If stack is empty. push current index as
			# base for next valid substring (if any)
			else:
				stk.append(i)

	return result


# Driver code
string = input("Enter String")

# Function call
print (find_max_len(string))
