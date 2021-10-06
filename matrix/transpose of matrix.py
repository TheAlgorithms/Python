# Python3 Program to find 
# transpose of a matrix 

N = 4

# Finds transpose of A[][] in-place 
def transpose(A): 

	for i in range(N): 
		for j in range(i+1, N): 
			A[i][j], A[j][i] = A[j][i], A[i][j] 

# matrix
A = [ [1, 1, 1, 1], 
	[2, 2, 2, 2], 
	[3, 3, 3, 3], 
	[4, 4, 4, 4]] 

transpose(A) 

print("Modified matrix is") 
for i in range(N): 
	for j in range(N): 
		print(A[i][j], " ", end='') 
	print() 
	
# This code is contributed 
# by aditya
