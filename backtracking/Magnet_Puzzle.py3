# Write Python3 code here
M = 5
N = 6
top = [ 1, -1, -1, 2, 1, -1 ]
bottom = [ 2, -1, -1, 2, -1, 3 ]
left = [ 2, 3, -1, -1, -1 ]
right = [ -1, -1, -1, 1, -1 ]

rules = [["L","R","L","R","T","T" ],
					[ "L","R","L","R","B","B" ],
					[ "T","T","T","T","L","R" ],
					[ "B","B","B","B","T","T" ],
					[ "L","R","L","R","B","B" ]];
		


def canPutPatternHorizontally(rules,i,j,pat):
	
	if j-1>=0 and rules[i][j-1] == pat[0]:
		return False
	elif i-1>=0 and rules[i-1][j] == pat[0]:
		return False
	elif i-1>=0 and rules[i-1][j+1] == pat[1]:
		return False
	elif j+2 < len(rules[0]) and rules[i][j+2] == pat[1]:
		return False
	
	return True
	

def canPutPatternVertically(rules,i,j,pat):
	
	if j-1>=0 and rules[i][j-1] == pat[0]:
		return False
	elif i-1>=0 and rules[i-1][j] == pat[0]:
		return False
	elif j+1 < len(rules[0]) and rules[i][j+1] == pat[0]:
		return False
	
	return True
	
def doTheStuff(rules,i,j):
	
	if rules[i][j] == "L" or rules[i][j] == "R":
			
		#	 option 1 +-
		if canPutPatternHorizontally(rules,i,j,"+-"):
			rules[i][j] = "+"
			rules[i][j+1] = "-"
			
			solveMagnets(rules,i,j)
		#	 option 2 -+

		#	 option 3 xx
			
def checkConstraints(rules):
	
	pCountH = [0 for i in range(len(rules))]
	nCountH = [0 for i in range(len(rules))]
	for row in range(len(rules)):
		for col in range(len(rules[0])):
			ch = rules[row][col]
			if ch == "+":
				pCountH[row] += 1
			elif ch == "-":
				nCountH[row] += 1
	
	
	pCountV = [0 for i in range(len(rules[0]))]
	nCountV = [0 for i in range(len(rules[0]))]
	for col in range(len(rules[0])):
		for row in range(len(rules)):
			ch = rules[row][col]
			if ch == "+":
				pCountV[col] += 1
			elif ch == "-":
				nCountV[col] += 1
				
	
	for row in range(len(rules)):
		if left[row] != -1:
			if pCountH[row] != left[row]:
				return False
		if right[row] != -1:
			if nCountH[row] != right[row]:
				return False
			
			
	
	for col in range(len(rules[0])):
		if top[col] != -1:
			if pCountV[col] != top[col]:
				return False
		if bottom[col] != -1:
			if nCountV[col] != bottom[col]:
				return False
		#			
		# if (top[col] != -1 and pCountH[col] != top[col]) or (bottom[col] != -1 and nCountH[col] != bottom[col]) :
		#	 return False
	
	return True
	
			
	
	
	
	
	
def solveMagnets(rules,i,j):
	
	if i == len(rules) and j == 0:

		# check the constraint before printing
		if checkConstraints(rules):
			print(rules)
	elif j >= len(rules[0]):
		
		solveMagnets(rules,i+1,0)

	# normal cases
	else:
		
		if rules[i][j] == "L":
			
			# option 1 +-
			if canPutPatternHorizontally(rules,i,j,"+-"):
				rules[i][j] = "+"
				rules[i][j+1] = "-"
				
				solveMagnets(rules,i,j+2)
				
				rules[i][j] = "L"
				rules[i][j+1] = "R"
			
			# option 2 -+
			if canPutPatternHorizontally(rules,i,j,"-+"):
				rules[i][j] = "-"
				rules[i][j+1] = "+"
				
				solveMagnets(rules,i,j+2)
				
				rules[i][j] = "L"
				rules[i][j+1] = "R"

			# option 3 xx
			if True or canPutPatternHorizontally(rules,i,j,"xx"):
				rules[i][j] = "x"
				rules[i][j+1] = "x"
				
				solveMagnets(rules,i,j+2)
				
				rules[i][j] = "L"
				rules[i][j+1] = "R"

		#	 vertical check
		elif rules[i][j] == "T":
			
			#	 option 1 +-
			if canPutPatternVertically(rules,i,j,"+-"):
				rules[i][j] = "+"
				rules[i+1][j] = "-"
				
				solveMagnets(rules,i,j+1)
				
				rules[i][j] = "T"
				rules[i+1][j] = "B"

			#	 option 2 -+
			if canPutPatternVertically(rules,i,j,"-+"):
				rules[i][j] = "-"
				rules[i+1][j] = "+"
				
				solveMagnets(rules,i,j+1)
				
				rules[i][j] = "T"
				rules[i+1][j] = "B"

			#	 option 3 xx
				
			if True or canPutPatternVertically(rules,i,j,"xx"):
				rules[i][j] = "x"
				rules[i+1][j] = "x"
				
				solveMagnets(rules,i,j+1)
				
				rules[i][j] = "T"
				rules[i+1][j] = "B"
				
		else:
			solveMagnets(rules,i,j+1)


# Driver code		
solveMagnets(rules,0,0)
