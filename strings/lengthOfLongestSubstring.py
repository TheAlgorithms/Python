def length_of_longest_substring(s: str) -> int:
	"""
	Given a string s, returnss the length of the longest substring without repeating characters.

	>>> length_of_longest_substring("abcabcbb")
	3
	>>> length_of_longest_substring("bbbbb")
	1
	>>> length_of_longest_substring("pwwkew")
	3
	>>> length_of_longest_substring("")
	0
	>>> length_of_longest_substring("a")
	1
	"""
	start = max_len = 0
	used_char = {}
	for i in range(len(s)):
		if s[i] in used_char and start <= used_char[s[i]]:
			start = used_char[s[i]] + 1
		else:
			max_len = max(max_len, i - start + 1)
		used_char[s[i]] = i
	return max_len
  
if __name__ == "__main__":
	from doctest import testmod
	testmod()
