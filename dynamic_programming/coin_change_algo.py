# Dynamic Programming Python implementation of Coin 
# Change problem 
def count(S, m, n): 
	# We need n+1 rows as the table is constructed 
	# in bottom up manner using the base case 0 value 
	# case (n = 0) 
	table = [[0 for x in range(m)] for x in range(n+1)] 

	# Fill the entries for 0 value case (n = 0) 
	for i in range(m): 
		table[0][i] = 1

	# Fill rest of the table entries in bottom up manner 
	for i in range(1, n+1): 
		for j in range(m): 

			# Count of solutions including S[j] 
			x = table[i - S[j]][j] if i-S[j] >= 0 else 0

			# Count of solutions excluding S[j] 
			y = table[i][j-1] if j >= 1 else 0

			# total count 
			table[i][j] = x + y 

	return table[n][m-1] 

# Driver program to test above function 
arr = [1, 2, 3] 
m = len(arr) 
n = 4
print(count(arr, m, n)) 

# This code is contributed by Swagata Srimani 
