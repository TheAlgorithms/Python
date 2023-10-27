"""
Project Euler Problem 401: https://projecteuler.net/problem=401

Problem Statement:
The divisors of 6 are 1, 2, 3 and 6.
The sum of the squares of these numbers is 1 + 4 + 9 + 36 = 50.
Let sigma2(n) represent the sum of the squares of the divisors of n. Thus sigma2(6) = 50.
Let SIGMA2 represent the summatory function of sigma.2, that is SIGMA2(n) E sigma2(i) for i = 1 to n
The first 6 values of SIGMA2 are: 1, 6, 16, 37, 63 and 113.
Find SIGMA2(10^15) modulo 10^9.


Sum of Squared Divisors Optimization:

This technique optimizes the computation of the sum of squared divisors for numbers from 1 to n.

Key Insights:
- Instead of calculating squared divisors individually for each number up to n, consider how many times 
  each divisor from 1 to n appears in the multiset union of all divisors.
- The count for a divisor k in this multiset is floor(n/k). Its contribution to the sum is floor(n/k) * k^2.
- For larger k values (specifically, k > sqrt(n)), the count doesn't change frequently. This allows us 
  to reduce the computational complexity from O(n) to O(sqrt(n)).
- For a specific count m = floor(n/k), k values yielding this count fall in the range: 
  floor(n/(m + 1)) < k <= floor(n/m).

Auxiliary Formula:
- To compute the sum of squares for integers up to n: sum(k^2 for k=1 to n) = n(n + 1)(2n + 1) / 6.
"""



def sqrt(x: int) -> int:
	assert x >= 0
	i: int = 1
	while i * i <= x:
		i *= 2
	y: int = 0
	while i > 0:
		if (y + i)**2 <= x:
			y += i
		i //= 2
	return y

def solution():
	LIMIT = 10**15
	MODULUS = 10**9
	
	# Can be any number from 1 to LIMIT, but somewhere near sqrt(LIMIT) is preferred
	splitcount = sqrt(LIMIT)
	# Consider divisors individually up and including this number
	splitat = LIMIT // (splitcount + 1)
	
	# The sum (s+1)^2 + (s+2)^2 + ... + (e-1)^2 + e^2.
	def sum_squares(s, e):
		return (e * (e + 1) * (e * 2 + 1) - s * (s + 1) * (s * 2 + 1)) // 6
	
	ans = sum((i * i * (LIMIT // i)) for i in range(1, splitat + 1))
	ans += sum((sum_squares(LIMIT // (i + 1), LIMIT // i) * i) for i in range(1, splitcount + 1))
	return str(ans % MODULUS)


if __name__ == "__main__":
	print(solution())
