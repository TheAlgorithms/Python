def isColSafe(row, col, matrix):
	for i in range(row):
		if(matrix[i][col]==1):
			return False
	return True


def isLeftDiagonalSafe(row, col, matrix):
	rowCounter = row - 1
	colCounter = col - 1
	while(rowCounter >= 0 and colCounter>=0):
		if(matrix[rowCounter][colCounter]==1):
			return False
		rowCounter -= 1
		colCounter -= 1
	return True
	
def isRightDiagonalSafe(row, col, matrix):
	rowCounter = row - 1
	colCounter = col + 1
	while(rowCounter >= 0 and colCounter<len(matrix[0])):
		if(matrix[rowCounter][colCounter]==1):
			return False
		rowCounter -= 1
		colCounter += 1
	return True
	
def isSafe(row, col, matrix):
	return (isColSafe(row, col, matrix) and isLeftDiagonalSafe(row, col, matrix) and isRightDiagonalSafe(row, col, matrix))
	

def generateN_Nmatrix(n):
	matrix = []
	for i in range (n):
		item = []
		for j in range(n):
			item.append(0)
		matrix.append(item)
	return matrix
	

def placeQueen(n):
	matrix = generateN_Nmatrix(n)
	ans = {}	
	row = 0
	col = 0
	while(row<n):
		isPlacedInRow = False
		while(col<n):
			if(isSafe(row, col, matrix)):
				matrix[row][col] = 1
				ans[row] = col
				isPlacedInRow = True
				break
			col = col + 1
		if(not isPlacedInRow):
			row = row - 1
			col = ans[row]
			ans.pop(row)
			matrix[row][col] = 0
			col = col + 1
		else:
			row = row + 1
			col = 0
	return matrix
	
a = placeQueen(4)
for i in a:
	print(i)
