"""
Project Euler Problem 407: https://projecteuler.net/problem=407

Problem Statement:
If we calculate a2 mod 6 for 0 a 5 we get: 0, 1, 4, 3, 4, 1.
The largest value of a such that a^2 = a mod 6 is 4.
Let's call M(n) the largest value of a < n such that a^2 = a (mod n).
so M(6) = 4.
Find SIGMA M(n) for 1 <= n <= 101

Solutions to Modular Equations:

- If a^2 ≡ a mod n, it's valid for any divisor of n.
- For prime powers, p^k, only solutions are a = 0, 1 mod p^k.
- Factoring n as prime powers, we have congruences of the form a = 0,1 mod p^k.
- Using the Chinese remainder theorem, we get 2^N solutions, where N is the number of unique prime factors of n.
- The largest solution among these is used for the M() function.
"""
from typing import Any, Callable, Optional, TypeVar, cast

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

def list_smallest_prime_factors(n: int) -> list[int]:
	result: list[Optional[int]] = [None] * (n + 1)
	limit = sqrt(n)
	for i in range(2, len(result)):
		if result[i] is None:
			result[i] = i
			if i <= limit:
				for j in range(i * i, n + 1, i):
					if result[j] is None:
						result[j] = i
	return cast(list[int], result)

def solution():
	LIMIT = 10**7
	
	smallestprimefactor = list_smallest_prime_factors(LIMIT)
	
	ans = 0
	for i in range(1, LIMIT + 1):
		# Compute factorization as coprime prime powers. e.g. 360 = {2^3, 3^2, 5^1}
		factorization = []
		j = i
		while j != 1:
			p = smallestprimefactor[j]
			q = 1
			while True:
				j //= p
				q *= p
				if j % p != 0:
					break
			factorization.append(q)
		
		solns = [0]
		modulus = 1
		for q in factorization:
			# Use Chinese remainder theorem; cache parts of it
			recip = pow(q, -1, modulus)
			newmod = q * modulus
			solns = [((0 + (x    ) * recip * q) % newmod) for x in solns] + \
			        [((1 + (x - 1) * recip * q) % newmod) for x in solns]
			modulus = newmod
		
		ans += max(solns)
	return str(ans)


if __name__ == "__main__":
	print(solution())
