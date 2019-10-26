"""
Euler discovered the remarkable quadratic formula:
n2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 412 + 41 + 41 is clearly divisible by 41.
The incredible formula  n2 − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form:
n² + an + b, where |a| &lt; 1000 and |b| &lt; 1000
where |n| is the modulus/absolute value of ne.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""
def isPrime(input):
		if (input == 2): 
			return True
		if (input <= 1): 
			return False
		if (input % 2 == 0):
			return False
		for (int i = input - 2; i >= math.sqrt(input); i -= 2):
			if (input % i == 0):
				return False
		return True
	
def findMaxN(a,b):
		max = 0
		n = 2
		while (isPrime(n*n + a*n + b)==True):
			if (n > max):
				max = n+1
    return max

  
def findMaxN(a,b):
		max = 0
		n = 2
		while (isPrime(n*n + a*n + b)==True):
			if (n > max):
				max = n+1
		return max

if __name__ == "__main__":
    print(solution(int(input().strip())))
	
