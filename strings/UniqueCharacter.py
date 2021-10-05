def CharUnique(S: str):
	"""
	>>> CharUnique('deacidified')
	False
	>>> CharUnique('keraunoscopia')
	False
	>>> CharUnique('layout')
	True
	>>> CharUnique('brand')
	True
	>>> CharUnique('texture')
	False
	>>> CharUnique('ovalness')
	False
	>>> CharUnique('unglove')
	True
	"""

	#for i scan ahead for same char
	for i in range(len(S)):
		#c is the one that i is compared against
		for c in range(i + 1, len(S)):
			if S[i] == S[c]:
				return(False)
	return(True)

#Given a string "S", Check if all characters in the string are unique or not if not return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
