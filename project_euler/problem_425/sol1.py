"""
Project Euler Problem 425: https://projecteuler.net/problem=425

Problem Statement:
Two positive numbers A and B are said to be connected (denoted by "A <-> B") if one of these conditions holds:
  (1) A and B have the same length and differ in exactly one digit; for example, 123 <-> 173.
  (2) Adding one digit to the left of A (or B) makes B (or A); for example, 23 <-> 223 and 123 <-> 23.
We call a prime P a 2's relative if there exists a chain of connected primes between 2 and P and no prime in the chain exceeds P.
For example, 127 is a 2's relative. One of the possible chains is shown below:
2 <-> 3 <-> 13 <-> 113 <-> 103 <-> 107 <-> 127
However, 11 and 103 are not 2's relatives.
Let F(N) be the sum of the primes <= N which are not 2s relatives.
We can verify that F(10^3) = 431 and F(10^4) = 78728.
Find F(10^7).

    This function finds all the relatives of 2, which can be viewed as solving a single-source
    shortest path problem using Dijkstra's algorithm. The main insight is that for each node
    (represented by a prime number), we evaluate the connection path from 2 to that prime.
    We then store the maximum path number at that node. This problem is well-suited for dynamic
    programming since the objective is to minimize the maximum path number.

    For instance, the prime 2 is connected to 103 via the following path:
    2 <-> 3 <-> 13 <-> 113 <-> 103.
    In this path, the largest number is 113. Among all possible paths, this path has the
    smallest maximum number. Therefore, 103 is not considered a relative of 2.
"""
3dfb77148c9b8ef0e5650a544af8
import heapq


def sqrt(x: int) -> int:
    assert x >= 0
    i: int = 1
    while i * i <= x:
        i *= 2
    y: int = 0
    while i > 0:
        if (y + i) ** 2 <= x:
            y += i
        i //= 2
    return y


def list_primality(n: int) -> list[bool]:
	# Sieve of Eratosthenes
	result: list[bool] = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(sqrt(n) + 1):
		if result[i]:
			for j in range(i * i, len(result), i):
				result[j] = False
	return result


def solution():
    LIMIT = 10**7

    isprime = list_primality(LIMIT)

    # pathmax[i] = None if i is not prime or i is not connected to 2.
    # Otherwise, considering all connection paths from 2 to i and for each path computing
    # the maximum number, pathmax[i] is the minimum number among all these maxima.
    pathmax = [None] * len(isprime)

    # Process paths in increasing order of maximum number
    queue = [(2, 2)]
    while len(queue) > 0:
        pmax, n = heapq.heappop(queue)
        if pathmax[n] is not None and pmax >= pathmax[n]:
            # This happens if at the time this update was queued, a better
            # or equally good update was queued ahead but not processed yet
            continue

        # Update the target node and explore neighbors
        pathmax[n] = pmax

        # Try all replacements of a single digit, including the leading zero.
        # This generates exactly all (no more, no less) the ways that a number m is connected to n.
        digits = to_digits(n)
        tempdigits = list(digits)
        for i in range(len(tempdigits)):  # For each digit position
            for j in range(10):  # For each digit value
                tempdigits[i] = j
                m = to_number(tempdigits)
                nextpmax = max(m, pmax)
                if (
                    m < len(isprime)
                    and isprime[m]
                    and (pathmax[m] is None or nextpmax < pathmax[m])
                ):
                    heapq.heappush(queue, (nextpmax, m))
            tempdigits[i] = digits[i]  # Restore the digit

    ans = sum(
        i
        for i in range(len(isprime))
        if isprime[i] and (pathmax[i] is None or pathmax[i] > i)
    )
    return str(ans)


# Returns the given non-negative integer as an array of digits, in big endian, with an extra leading zero.
# e.g. 0 -> [0,0]; 1 -> [0,1]; 8 -> [0,8]; 42 -> [0,4,2]; 596 -> [0,5,9,6].
def to_digits(n):
    if n < 0:
        raise ValueError()

    # Extract base-10 digits in little endian
    temp = []
    while True:
        temp.append(n % 10)
        n //= 10
        if n == 0:
            break

    temp.append(0)
    temp.reverse()
    return temp


def to_number(digits):
    result = 0
    for x in digits:
        result = result * 10 + x
    return result


if __name__ == "__main__":
    print(solution())
