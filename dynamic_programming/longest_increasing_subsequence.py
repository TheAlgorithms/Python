'''
Author  : Mehdi ALAOUI

This is a pure Python implementation of Dynamic Programming solution to the longest increasing subsequence of a given sequence.

The problem is  :
Given an ARRAY, to find the longest and increasing sub ARRAY in that given ARRAY and return it.
Example: [10, 22, 9, 33, 21, 50, 41, 60, 80] as input will return [10, 22, 33, 41, 60, 80] as output
'''

def longestSub(ARRAY): 			#This function is recursive
	
	ARRAY_LENGTH = len(ARRAY)
	if(ARRAY_LENGTH <= 1):  	#If the array contains only one element, we return it (it's the stop condition of recursion)
		return ARRAY
								#Else
	PIVOT=ARRAY[0]
	LONGEST_SUB=[]				#This array will contains the longest increasing sub array
	for i in range(1,ARRAY_LENGTH):			#For each element from the array (except the pivot),
		if (ARRAY[i] < PIVOT):				#if the element is smaller than the pivot, it won't figure on the sub array that contains the pivot
			TEMPORARY_ARRAY = [ element for element in ARRAY[i:] if element >= ARRAY[i] ]	#But it cas figure in an increasing sub array starting from this element
			TEMPORARY_ARRAY = longestSub(TEMPORARY_ARRAY)									#We calculate the longest sub array that starts from this element
			if ( len(TEMPORARY_ARRAY) > len(LONGEST_SUB) ):									#And we save the longest sub array that begins from an element smaller than the pivot (in LONGEST_SUB)
				LONGEST_SUB = TEMPORARY_ARRAY

	TEMPORARY_ARRAY = [ element for element in ARRAY[1:] if element >= PIVOT ]				#Then we delete these elements (smaller than the pivot) from the initial array
	TEMPORARY_ARRAY = [PIVOT] + longestSub(TEMPORARY_ARRAY)									#And we calculate the longest sub array containing the pivot (in TEMPORARY_ARRAY)
	if ( len(TEMPORARY_ARRAY) > len(LONGEST_SUB) ):											#Then we compare the longest array between TEMPORARY_ARRAY and LONGEST_SUB
		return TEMPORARY_ARRAY
	else:																					#And we return the longest one
		return LONGEST_SUB

#Some examples

print(longestSub([4,8,7,5,1,12,2,3,9]))
print(longestSub([9,8,7,6,5,7]))