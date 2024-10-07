# Python3 program to count the
# no. of ways to place 2*1 size
# tiles in 2*n size board.
def getNoOfWays(n):

	# Base case
	if n <= 2:
		return n

	return getNoOfWays(n - 1) + getNoOfWays(n - 2)

# Driver Code
print(getNoOfWays(4))
print(getNoOfWays(3))

# This code is contributed by Kevin Joshi
