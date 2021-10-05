def CharUnique(S):
	#for i scan ahead for same char
	for i in range(len(S)):
		#c is the one that i is compared against
		for c in range(i + 1, len(S)):
			if S[i] == S[c]:
				return(False)
	return(True)

#Given a string "S", Check if all characters in the string is unique or not
S = input("Input String: ")
print(CharUnique(S))