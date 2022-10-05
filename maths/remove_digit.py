def remove_digit(num: int)->int:
	"""

	returns the biggest possible result
	that can be achieved by removing
	one digit from the given number

	>>> remove_digit(152)
	52
	>>> remove_digit(6385)
	685
	>>> remove_digit(-11)
	1
	>>> remove_digit(2222222)
	222222
	>>> remove_digit("2222222")
	0
	>>> remove_digit("string input")
	0
	"""

	try:
		num_str = str(abs(num))
		num_list = [[c for c in num_str] for c in range(len(num_str))]
		for c in range(len(num_str)):
			num_list[c].pop(c)
		return sorted([int("".join([a for a in c])) for c in num_list])[-1]
	except TypeError:
		return 0

if __name__ == "__main__":
	__import__("doctest").testmod()