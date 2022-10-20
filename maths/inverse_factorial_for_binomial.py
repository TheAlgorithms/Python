# of nCr in O(1) time.
N = 1000001

# array to store inverse of 1 to N
factorialNumInverse = [None] * (N + 1)

# array to precompute inverse of 1! to N!
naturalNumInverse = [None] * (N + 1)

# array to store factorial of
# first N numbers
fact = [None] * (N + 1)

# Function to precompute inverse of numbers
def InverseofNumber(p):
	naturalNumInverse[0] = naturalNumInverse[1] = 1
	for i in range(2, N + 1, 1):
		naturalNumInverse[i] = (naturalNumInverse[p % i] *
								(p - int(p / i)) % p)

# Function to precompute inverse
# of factorials
def InverseofFactorial(p):
	factorialNumInverse[0] = factorialNumInverse[1] = 1

	# precompute inverse of natural numbers
	for i in range(2, N + 1, 1):
		factorialNumInverse[i] = (naturalNumInverse[i] *
								factorialNumInverse[i - 1]) % p

# Function to calculate factorial of 1 to N
def factorial(p):
	fact[0] = 1

	# precompute factorials
	for i in range(1, N + 1):
		fact[i] = (fact[i - 1] * i) % p

# Function to return nCr % p in O(1) time
def Binomial(N, R, p):
	
	# n C r = n!*inverse(r!)*inverse((n-r)!)
	ans = ((fact[N] * factorialNumInverse[R])% p *
					factorialNumInverse[N - R])% p
	return ans

# Driver Code
if __name__ == '__main__':
	
	# Calling functions to precompute the
	# required arrays which will be required
	# to answer every query in O(1)
	p = 1000000007
	InverseofNumber(p)
	InverseofFactorial(p)
	factorial(p)

	
	N = 15
	R = 4
	print(Binomial(N, R, p))

	
	N = 20
	R = 3
	print(Binomial(N, R, p))
