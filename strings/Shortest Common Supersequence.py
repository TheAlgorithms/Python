def shortestSuperSequence(X, Y): 
	m = len(X) 
	n = len(Y) 
	l = lcs(X, Y, m, n) 


	return (m + n - l) 

def lcs(X, Y, m, n): 
	L = [[0] * (n + 2) for i in
		range(m + 2)] 

	for i in range(m + 1): 

		for j in range(n + 1): 

			if (i == 0 or j == 0): 
				L[i][j] = 0

			elif (X[i - 1] == Y[j - 1]): 
				L[i][j] = L[i - 1][j - 1] + 1

			else: 
				L[i][j] = max(L[i - 1][j], 
							L[i][j - 1]) 


	return L[m][n] 



X = "AGGTAB"
Y = "GXTXAYB"

print("Length of the shortest supersequence is %d"
	% shortestSuperSequence(X, Y)) 


