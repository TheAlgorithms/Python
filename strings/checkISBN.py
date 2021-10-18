# Python code to check if a given ISBN is valid or not.

def is_valid_isbn(isbn: str) -> bool:

	# check for length
	if len(isbn) != 10:
		return False
	
	# Computing weighted sum
	# of first 9 digits
	_sum = 0
	for i in range(9):
		if 0 <= int(isbn[i]) <= 9:
			_sum += int(isbn[i]) * (10 - i)
		else:
			return False
		
	# Checking last digit
	if(isbn[9] != 'X' and
	0 <= int(isbn[9]) <= 9):
		return False
	
	# If last digit is 'X', add
	# 10 to sum, else add its value.
	_sum += 10 if isbn[9] == 'X' else int(isbn[9])
	
	# Return true if weighted sum of
	# digits is divisible by 11
	return (_sum % 11 == 0)

# Test
if isValidISBN(isbn="007462542X"):
	print('Valid')
else:
	print("Invalid")
