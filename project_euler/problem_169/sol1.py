"""
Project Euler Problem 169: https://projecteuler.net/problem=169
Author: Vinayaka Gosula
Define f(0)=1 and f(n) to be the number of different ways n can be expressed as a sum of integer powers of 2 using each power no more than twice.
For example, f(10)=5 since there are five different ways to express 10:

1 + 1 + 8
1 + 1 + 4 + 4
1 + 1 + 2 + 2 + 4
2 + 4 + 4
2 + 8

What is f(10**25)?
"""
dp = {}
def solve(n):
	if n <= 1:
		return n
	if n in dp.keys():
		return dp[n]
	if n % 2:
		out = solve((n - 1) // 2) + solve((n + 1) // 2)
	else:
		out = solve(n // 2)
	dp[n] = out
	return out
def solution(n = 10**25):
	"""Finds the answer for a given n
    >>> solution()
    178653872807
    """
	return solve(n + 1)

