def mode(inputlist):                    					#Defining function "mode."
	"""
	This function returns the mode(Mode as in the measures of central tendency) of the input data.
	
	>>> mode([2,3,4,5,3,4,2,5,2,2,4,2,2,2])
	2
	
	the input list may contain any Datastructure or any Datatype.
	"""
	checklist = inputlist.copy()    					#Copying inputlist to check with the index number later.
	result = list()								#Empty list to store the counts of elements in inputlist
	for x in inputlist:
		result.append(inputlist.count(x))		
		inputlist.remove(x)
		y=max(result)							#Gets the maximum value in the result list.
		return checklist[result.index(y)]				#Returns the value with the maximum number of repetitions.
data=[1,2,4,3,1,6,4,2,5,1,1,2,3]
print(mode(data))
