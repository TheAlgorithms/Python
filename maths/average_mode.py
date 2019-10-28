def mode(input_list):                    					#Defining function "mode."
	"""
	This function returns the mode(Mode as in the measures of central tendency) of the input data.

	>>> input_list = [2,3,4,5,3,4,2,5,2,2,4,2,2,2]
	>>> mode(input_list)
	2
	>>> import statistics
	>>> mode(input_list) == statistics.mode(input_list)
	True
	
	the input list may contain any Datastructure or any Datatype.
	"""
	check_list = input_list.copy()    					#Copying inputlist to check with the index number later.
	result = list()								#Empty list to store the counts of elements in inputlist
	for x in input_list:
		result.append(input_list.count(x))		
		input_list.remove(x)
		y=max(result)							#Gets the maximum value in the result list.
		return check_list[result.index(y)]				#Returns the value with the maximum number of repetitions.
data=[1,2,4,3,1,6,4,2,5,1,1,2,3]
print(mode(data))
