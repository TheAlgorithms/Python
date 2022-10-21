# Python program to search an element in row-wise
# and column-wise sorted matrix
# Searches the element ele in mat[][]. If the



def searchMatix(mat, n, x):
	if(n == 0):
		return -1
      
	for i in range(n):
		for j in range(n):

			if(mat[i][j] == x):
				print("Element found at (", i, ",", j, ")")
				return 1

	print(" Element not found")
	return -1


if __name__ == "__main__":
	mat = [[10, 20, 30, 40], [15, 25, 35, 45],
		[27, 29, 37, 48], [32, 33, 39, 50]]

	searchMatix(mat, 4, 29)

