def lengthOfLongestSubstring(s: str) -> int:
	"""
	Given a string s, returnss the length of the longest substring without repeating characters.

	>>> lengthOfLongestSubstring("abcabcbb")
	3
	>>> lengthOfLongestSubstring("bbbbb")
	1
	>>> lengthOfLongestSubstring("pwwkew")
	3
	>>> lengthOfLongestSubstring("")
	0
	>>> lengthOfLongestSubstring("a")
	1
	"""
	start = maxLength = 0
	usedChar = {}
	for i in range(len(s)):
		if s[i] in usedChar and start <= usedChar[s[i]]:
			start = usedChar[s[i]] + 1
		else:
			maxLength = max(maxLength, i - start + 1)
		usedChar[s[i]] = i
	return maxLength
  
if __name__ == "__main__":
	from doctest import testmod
	testmod()
