# Project Euler - Problem 95
# Amicable Chains

# https://www.github.com/JehanPatel

# Refer to https://github.com/TheAlgorithms/Python/issues/9166 for further discussion on Project Euler - Problem 95

# What is Amicable Chains?
# Amicable chains are a sequence of numbers in which each number is the sum of the proper divisors of the number that follows it. For example, consider the sequence 220, 284, 220, 284, ... Here, 220 is the sum of the proper divisors of 284, and 284 is the sum of the proper divisors of 220.

# Problem Statement - https://user-images.githubusercontent.com/118645569/271806807-863546a0-c723-437a-9475-3017e3218d55.png

import itertools

def compute():
	LIMIT = 1000000
	
	divisorsum = [0] * (LIMIT + 1)
	for i in range(1, LIMIT + 1):
		for j in range(i * 2, LIMIT + 1, i):
			divisorsum[j] += i
	
	maxchainlen = 0
	ans = -1
	for i in range(LIMIT + 1):
		visited = set()
		cur = i
		for count in itertools.count(1):
			visited.add(cur)
			next = divisorsum[cur]
			if next == i:
				if count > maxchainlen:
					ans = i
					maxchainlen = count
				break
			elif next > LIMIT or next in visited:
				break
			else:
				cur = next
	
	return str(ans)


if __name__ == "__main__":
	print(compute())
