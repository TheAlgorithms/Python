from string import ascii_lowercase as letters, digits
from re import match

def toDecimal(base_str: str, base: int):
	""" convert any string in base n to decimal,
		>>> toDecimal("-FF", 16)
		-255
		>>> toDecimal("RidoineEl", 30)
		18118435414041
		>>> toDecimal("11111100110", 2)
		2022
		
	"""

	# check base_str type
	if not isinstance(base_str, str):
		raise ValueError("invalid string type: string woud be str")

	base_str = base_str.strip().lower()
	chars = digits + letters
	valid_chars = chars[:base]
	prefix = 1
	decimal = int()

	# check if base is valid
	if isinstance(base, int):
		if base <= 0 or base > 36:
			raise ValueError("invalid base range(1-36)")
	elif isinstance(base, float):
		if not base.is_integer():
			raise ValueError("invalid base: base would be integer")
		else:
			base = int(base)
	else:
		raise ValueError("invalid base: base would be integer")

	# check if base_str is valid
	if match(rf"^(-|\+)?[{valid_chars}]+", base_str) is None:
		# base_str is invalid
		raise ValueError("invalid string in base %d" % base)


	if base_str[0] in "-+":
		if base_str[0] == "-":
			prefix = -1

		# delete operator
		base_str = base_str[1:]

	# finally, reverse base_str 
	# and calculate decimal
	for index, char in enumerate(reversed(base_str)):
		char_value = valid_chars.index(char)
		decimal += prefix * char_value*base**index

	return decimal

def main():
	dec = toDecimal("-11111100110", 2)

	print(dec)

if __name__ == '__main__':
	import doctest
	doctest.testmod()
