"""
Problem 204: https://projecteuler.net/problem=204

Problem Statement:

A Hamming number is a positive number which has no prime factor larger than 5.
So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
There are 1105 Hamming numbers not exceeding 10^8.

We will call a positive number a generalised Hamming number of type n, if
it has no prime factor larger than n. Hence the Hamming numbers are the
generalised Hamming numbers of type 5.

How many generalised Hamming numbers of type 100 are there which don't exceed 10^9?


Solution:

Find all primes under 100, then find the number of integers that can
be constructed by multiplying some primes in the list repeatedly.
"""


def find_primes(limit: int) -> list[int]:
    """
    Returns a list of all primes less than or equal to 'limit'
    >>> find_primes(19)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    sieve = [True] * (limit + 1)

    for i in range(2, limit + 1):
        for j in range(2 * i, limit + 1, i):
            sieve[j] = False
    return [i for i in range(2, limit + 1) if sieve[i]]


def num_hamming_numbers(val: int, primes: list[int], limit: int) -> int:
    """
    Returns the number of n such that n <= limit and
    n = val * p_1 * p_2... * p_k, where p_i are in 'primes'
    >>> num_hamming_numbers(6, [3, 5], 90)
    5
    """
    if val > limit:
        return 0

    num = 1
    for i in range(len(primes)):
        num += num_hamming_numbers(val * primes[i], primes[i:], limit)
    return num


def solution(hamming_type: int = 100, limit: int = 10**9) -> int:
    """
    Returns the number of generalized Hamming numbers of type 'hamming_type'
    not exceeding 'limit'
    >>> solution(5, 10**8)
    1105
    """
    return num_hamming_numbers(1, find_primes(hamming_type), limit)


if __name__ == "__main__":
    print(f"{solution() = }")
