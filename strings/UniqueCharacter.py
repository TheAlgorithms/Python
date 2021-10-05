def CharUnique(S):
	#for i scan ahead for same char
	for i in range(len(S)):
		#c is the one that i is compared against
		for c in range(i + 1, len(S)):
			"""
			Ex: Hello!
			i = 0 and C starts at i + 1 so the same char isn't compared against itself
			S[0] = H and S[1] = e
			
			H is compared to every other char ahead of it
			c loop finishes then e is compared to everything ahead of it
			
			S[2] = l S[3] = l; 2 characters are repeated and not unique return false
			if nothing is found by end of string return true
			"""
			if S[i] == S[c]:
				return(False)
	return(True)

#Given a string "S", Check if all characters in the string is unique or not
S = input("Input String: ")
print(CharUnique(S))
