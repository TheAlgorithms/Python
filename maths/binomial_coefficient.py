# Python program to find binomial coefficient using pascals triangle.

def solve(n,r): 

	
	C = [0 for i in range(r+1)]
	
	# nc0 = 1 
	C[0] = 1  

	for i in range(1,n+1): 

		#to compute current row from previous row.
		j = min(i ,r) 

		while (j > 0): 
			C[j] = C[j] + C[j-1] 
			j -= 1

	return C[r]

#sample Data	
n = 10
r = 5

print (solve(n,r))	 
 

