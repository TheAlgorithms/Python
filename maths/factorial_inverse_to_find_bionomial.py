# of nCr in O(1) time.
N = 1000001

# array to store inverse of 1 to N
factorial_num_inverse = [None] * (N + 1)

# array to precompute inverse of 1! to N!
natural_num_inverse = [None] * (N + 1)

# array to store factorial of
# first N numbers
fact = [None] * (N + 1)

# Function to precompute inverse of numbers
<<<<<<< HEAD
def inverse_of_num(p) -> None:
	natural_num_inverse[0] = natural_num_inverse[1] = 1
	for i in range(2, N + 1, 1):
		natural_num_inverse[i] = (natural_num_inverse[p % i] *
								(p - int(p / i)) % p)

# Function to precompute inverse
# of factorials
def InverseofFactorial(p) -> None:
	factorial_num_inverse[0] = factorial_num_inverse[1] = 1

	# precompute inverse of natural numbers
	for i in range(2, N + 1, 1):
		factorial_num_inverse[i] = (natural_num_inverse[i] *
								factorial_num_inverse[i - 1]) % p

# Function to calculate factorial of 1 to N
def factorial(p) -> None:
	fact[0] = 1
=======
def InverseofNumber(p):
    naturalNumInverse[0] = naturalNumInverse[1] = 1
    for i in range(2, N + 1, 1):
        naturalNumInverse[i] = naturalNumInverse[p % i] * (p - int(p / i)) % p


# Function to precompute inverse
# of factorials
def InverseofFactorial(p):
    factorialNumInverse[0] = factorialNumInverse[1] = 1

    # precompute inverse of natural numbers
    for i in range(2, N + 1, 1):
        factorialNumInverse[i] = (naturalNumInverse[i] * factorialNumInverse[i - 1]) % p


# Function to calculate factorial of 1 to N
def factorial(p):
    fact[0] = 1

    # precompute factorials
    for i in range(1, N + 1):
        fact[i] = (fact[i - 1] * i) % p
>>>>>>> ffb7e20ef957177e1b0db68a726566007e8777e9


# Function to return nCr % p in O(1) time
def Binomial(N, R, p):
<<<<<<< HEAD
	
	# n C r = n!*inverse(r!)*inverse((n-r)!)
	ans = ((fact[N] * factorial_num_inverse[R])% p *
					factorial_num_inverse[N - R])% p
	return ans

# Driver Code
if __name__ == '__main__':
	
	# Calling functions to precompute the
	# required arrays which will be required
	# to answer every query in O(1)
	p = 1000000007
	inverse_of_num(p)
	InverseofFactorial(p)
	factorial(p)
=======

    # n C r = n!*inverse(r!)*inverse((n-r)!)
    ans = ((fact[N] * factorialNumInverse[R]) % p * factorialNumInverse[N - R]) % p
    return ans


# Driver Code
if __name__ == "__main__":
>>>>>>> ffb7e20ef957177e1b0db68a726566007e8777e9

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
