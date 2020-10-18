def min_char(s):
	"""
	>>>min_char(aaba)
	1
	>>>min_char(aabaa)
	0
	>>>min_char(abcddcba)
	0
	>>>min_char(abfddcbb)
	2

	"""
	ans = 0
	for x in range(len(s)):
		if s[x] != s[-1-x]:
			ans = ans + 1
	return ans
 if __name__ == "__main__":
 	from doctest import testmod
 	testmod()