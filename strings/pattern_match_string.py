# Function to determine if given pattern matches with a string or not
def match(str, i, pat, j, dict):

	n = len(str)
	m = len(pat)

	# base condition
	if n < m:
		return False

	# if both pattern and the string reaches end
	if i == n and j == m:
		return True

	# if either string or pattern reaches end
	if i == n or j == m:
		return False

	# consider next character from the pattern
	curr = pat[j]

	# if the character is seen before
	if curr in dict:

		s = dict[curr]
		k = len(s)

		# ss stores next k characters of the given string
		if i + k < len(str):
			ss = str[i:i + k]
		else:
			ss = str[i:]

		# return false if next k characters doesn't match with s
		if ss != s:
			return False

		# recur for remaining characters if next k characters matches
		return match(str, i + k, pat, j + 1, dict)

	# process all remaining characters in the string if current
	# character is never seen before
	for k in range(1, n - i + 1):

		# insert substring formed by next k characters of the string
		# into the dictionary
		dict[curr] = str[i:i + k]

		# check if it leads to the solution
		if match(str, i + k, pat, j + 1, dict):
			return True

		# else backtrack - remove current character from the dictionary
		dict.pop(curr)

	return False


if __name__ == '__main__':

	# input string and pattern
	str = "codesleepcode"
	pat = "XYX"

	# create a dictionary to store mappings between the pattern and string
	dict = {}

	# check for solution
	if match(str, 0, pat, 0, dict):
		print(dict)
	else:
		print("Solution doesn't exist")
