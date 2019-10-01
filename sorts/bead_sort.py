
from itertools import zip_longest

def beadsort(l):
	""" Implementation of bead sort algorithm in Python
	It can only be used with positive integers.
	
	:param l: some mutable collection with positive integers inside
	:return: the same collection ordered by ascending.
	
	Examples:
	>>> beadsort([9,6,4,3])
	[3, 4, 6, 9]
	
	>>> beadsort([])
	[]
	"""
	if all([type(x) == int and x >= 0 for x in l]):
		ref = [range(x) for x in l]  #for reference
	else:
		raise ValueError("All elements must be positive integers")
	inter = []
	ind = 0 
	prev = sum([1 for x in ref if len(x) > ind])
	while prev:
		inter.append(range(prev))
		ind += 1
		prev = sum([1 for x in ref if len(x) > ind])
	ind = 0
	prev = sum([1 for x in inter if len(x) > ind])
	out = []
	while prev:
		out.append(prev)
		ind += 1
		prev = sum([1 for x in inter if len(x) > ind])
	out = out[::-1]
	return out

if __name__ == "__main__":
	print(beadsort([5,3,1,7,4,1,1]))
	print(beadsort([9,6,4,3]))
	print(beadsort([]))
