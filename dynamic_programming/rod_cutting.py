### SOLUTION ###
"""
Optimal Substructure: 
When we receive a rod, we have two options:
a) Don't cut it and sell it as is (receiving prices[length])
b) Cut it and sell it in two parts. The length we cut it and the rod we are
left with, which we have to try and sell separately in an efficient way.
Choose the maximum price we can get.
"""

def rod_cutting_recursive(prices,length):
	"""
	Given a rod of length n and array of prices that indicate price at each length.
	Determine the maximum value obtainable by cutting up the rod and selling the pieces

	Args:
		prices: list indicating price at each length, where prices[0] = 0 indicating rod of zero length has no value
	    length: length of rod

	Returns:
	    Maximum revenue attainable by cutting up the rod in any way. 

	Raises:
	    KeyError: Raises an exception.
	"""
	#base case 
	if length == 0:
		return 0
	value = float('-inf')
	for firstCutLocation in range(1,length+1):
		value = max(value, prices[firstCutLocation]+rod_cutting_recursive(prices,length - firstCutLocation))
	return value


def main():
	assert rod_cutting_recursive([0,1,5,8,9,10,17,17,20,24,30],10) == 30
    
if __name__ == '__main__':
	main()


