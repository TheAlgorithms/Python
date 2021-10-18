"""
Program to find sum of all the elements from starting index to the given index in a list
"""

def cumulative_sum(lst: list, idx: int) -> int:
	"""
	>>> cumulative_sum([1, 2, 3, 4], 3)
	10
	>>> cumulative_sum([1, 2, 3, 4], 1)
	3
	>>> cumulative_sum([1, 2, 3, 4], -1)
	Traceback (most recent call last):
		...
	Exception: Index cannot be smaller than 0
	>>> cumulative_sum([1, 2, 3, 4], 5)
	Traceback (most recent call last):
		...
	Exception: Index cannot be bigger than 3
	"""
	if idx < 0:
		raise Exception("Index cannot be smaller than 0")
	if idx >= len(lst):
		raise Exception("Index cannot be bigger than " + str(len(lst)-1))

	for index in range(1, len(lst)):
		lst[index] += lst[index - 1]

	return lst[idx]

if __name__ == "__main__":
	from doctest import testmod
	
	testmod()