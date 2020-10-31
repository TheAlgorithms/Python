def isSafe(A,row,col,visited,N,M):
	return ((row >= 0) and (col >= 0) and (row < N) and (col < M) and A[row][col] and (visited[row][col] == False))

def dfs(A,i,j,visited,N,M):
	row = [-1,-1,-1,0,0,1,1,1]
	col = [-1,0,1,-1,1,-1,0,1]
	visited[i][j] = True
	for k in range(8):
		if(isSafe(A,i+row[k],j+col[k],visited,N,M)):
			dfs(A,i+row[k],j+col[k],visited,N,M)

def findIslands(A,N,M):
	visited = []
	for i in range(N):
		V = []
		for j in range(M):
			V.append(False)
		visited.append(V)

	count = 0
	for i in range(N):
	 	for j in range(M):
	 		if((visited[i][j] == False) and A[i][j] == 1):
	 			dfs(A,i,j,visited,N,M)
	 			count += 1

	return count

if __name__ == '__main__':
	t = int(input())

	A = []
	while(t>0):
		N,M = input().strip().split()
		N = int(N)
		M = int(M)

		lst = [int(x) for x in input().strip().split()]
		k = 0
		for i in range(N):
			B = []
			for j in range(M):
				B.append(lst[k])
				k += 1
			A.append(B)


		#print(A)
		print(findIslands(A,N,M))

		t -= 1
