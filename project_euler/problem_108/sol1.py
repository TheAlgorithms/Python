"""
Problem 108: https://projecteuler.net/problem=108

Problem Statement:

In the following equation x, y, and n are positive integers.
    1/x + 1/y = 1/n

For n = 4 there are exactly three distinct solutions:
    1/5 + 1/20 = 1/4
    1/6 + 1/12 = 1/4
    1/8 + 1/8 = 1/4

What is the least value of n for which the number of distinct solutions
exceeds one-thousand?


Solution:

For a given n, the number of distinct solutions is (d(n * n) // 2) + 1,
where d is the divisor counting function. Find an arbitrary n with more
than 1000 solutions, so n is an upper bound for the answer. Find
prime factorizations for all i < n, allowing easy computation of d(i * i)
for i <= n. Then try all i to find the smallest.
"""


def find_primes(n: int) -> list[int]:
    """
    Returns a list of all primes less than or equal to n
    >>> find_primes(19)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    sieve = [True] * (n + 1)

    for i in range(2, n + 1):
        for j in range(2 * i, n + 1, i):
            sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def find_prime_factorizations(n: int) -> list[dict[int, int]]:
    """
    Returns a list of prime factorizations of 2...n, with prime
    factorization represented as a dictionary of (prime, exponent) pairs
    >>> find_prime_factorizations(7)
    [{}, {}, {2: 1}, {3: 1}, {2: 2}, {5: 1}, {2: 1, 3: 1}, {7: 1}]
    """
    primes = find_primes(n)
    prime_factorizations = [dict() for _ in range(n + 1)]

    for p in primes:
        for j in range(p, n + 1, p):
            j_factorization = prime_factorizations[j]
            x = j
            while x % p == 0:
                x /= p
                j_factorization[p] = j_factorization.get(p, 0) + 1
    return prime_factorizations


def num_divisors_of_square(prime_factorization: dict[int, int]) -> int:
    """
    Returns the number of divisors of n * n, where n is the
    number represented by the input prime factorization
    >>> num_divisors_of_square({2: 2, 3: 2}) # n = 36
    25
    """
    num_divisors = 1
    for _, e in prime_factorization.items():
        num_divisors *= 2 * e + 1
    return num_divisors


def solution(target: int = 1000) -> int:
    """
    Returns the smallest n with more than 'target' solutions
    >>> solution()
    180180
    """

    upper_bound = 210 ** ((int((2 * target - 1) ** 0.25) + 1) // 2)
    prime_factorizations = find_prime_factorizations(upper_bound)

    def num_solutions(n):
        return (num_divisors_of_square(prime_factorizations[n]) // 2) + 1

    for i in range(2, upper_bound + 1):
        if num_solutions(i) > target:
            return i


if __name__ == "__main__":
    print(f"{solution() = }")
