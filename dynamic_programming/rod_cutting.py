from typing import List

def rod_cutting(prices: List[int],length: int) -> int:
	"""
	Given a rod of length n and array of prices that indicate price at each length.
	Determine the maximum value obtainable by cutting up the rod and selling the pieces
	
	>>> rod_cutting([1,5,8,9],4) 
	10
	>>> rod_cutting([1,1,1],3) 
	3
	>>> rod_cutting([1,2,3], -1)
	Traceback (most recent call last):
   	ValueError: Given integer must be greater than 1, not -1
   	>>> rod_cutting([1,2,3], 3.2)
	Traceback (most recent call last):
   	TypeError: Must be int, not float
   	>>> rod_cutting([], 3)
	Traceback (most recent call last):
   	AssertionError: prices list is shorted than length: 3
	
	

	Args:
		prices: list indicating price at each length, where prices[0] = 0 indicating rod of zero length has no value
	    length: length of rod

	Returns:
	    Maximum revenue attainable by cutting up the rod in any way. 
	"""

	prices.insert(0, 0)
	if not isinstance(length, int):
	    raise TypeError('Must be int, not {0}'.format(type(length).__name__))
	if length < 0: 
	    raise ValueError('Given integer must be greater than 1, not {0}'.format(length))
	assert len(prices) - 1 >= length, "prices list is shorted than length: {0}".format(length) 

	return rod_cutting_recursive(prices, length)

def rod_cutting_recursive(prices: List[int],length: int) -> int:
	#base case 
	if length == 0:
		return 0
	value = float('-inf')
	for firstCutLocation in range(1,length+1):
		value = max(value, prices[firstCutLocation]+rod_cutting_recursive(prices,length - firstCutLocation))
	return value


def main():
	assert rod_cutting([1,5,8,9,10,17,17,20,24,30],10) == 30
	# print(rod_cutting([],0))

if __name__ == '__main__':
	main()

