n = 3

def findLongestPathFromACell(i, j, mat, dp):
	if (i<0 or i>= n or j<0 or j>= n):
		return 0
	if (dp[i][j] != -1):
		return dp[i][j]

	x, y, z, w = -1, -1, -1, -1

	if (j<n-1 and ((mat[i][j] +1) == mat[i][j + 1])):
		x = 1 + findLongestPathFromACell(i, j + 1, mat, dp)
	if (j>0 and (mat[i][j] +1 == mat[i][j-1])):
		y = 1 + findLongestPathFromACell(i, j-1, mat, dp)
	if (i>0 and (mat[i][j] +1 == mat[i-1][j])):
		z = 1 + findLongestPathFromACell(i-1, j, mat, dp)
	if (i<n-1 and (mat[i][j] +1 == mat[i + 1][j])):
		w = 1 + findLongestPathFromACell(i + 1, j, mat, dp)

	dp[i][j] = max(x, max(y, max(z, max(w, 1))))
	return dp[i][j]

def findLongestPathInAMatrix(mat):
	result = 1
	dp =[[-1 for i in range(n)]for i in range(n)]
	for i in range(n):
		for j in range(n):
			if (dp[i][j] == -1):
				findLongestPathFromACell(i, j, mat, dp)
			result = max(result, dp[i][j]);
	return result

if __name__ == "__main__":
  import doctest
  doctest.testmod()
