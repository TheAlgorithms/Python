"""
Problem 50
Consecutive Prime Sum
https://projecteuler.net/problem=50

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below 100.
The longest sum of consecutive primes below one-thousand that adds
to a prime, contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the
sum of the most consecutive primes?
"""

import math
from bisect import bisect_left
from typing import List


def prime_sieve(n: int) -> List[int]:
    """
    Sieve Of Eratosthenes
    Function to return all the prime numbers up to a certain number.
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    >>> prime_sieve(9)
    [2, 3, 5, 7]
    >>> prime_sieve(53)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    """

    if n < 2:
        return []

    end = n + 1
    is_prime = [True] * end
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        for j in range(i * 2, end, i):
            is_prime[j] = False

    primes = [2]
    for i in range(3, end, 2):
        if is_prime[i]:
            primes.append(i)
    return primes


def binary_search(num_list, item) -> int:
    """
    Returns the index of item in sorted list l using binary search
    bisect_left(list, item) returns the index to insert item in list.

    >>> binary_search([1, 3, 5, 8, 9], 5)
    2
    >>> binary_search([1, 3, 5, 8, 9], 2)
    -1
    """
    i = bisect_left(num_list, item)
    if i != len(num_list) and num_list[i] == item:
        return i
    else:
        return -1


def solution(MAX_LIMIT: int = 1_000_000) -> int:
    """
    Returns the prime below 1 Million/MAX_LIMIT that can be
    written as the sum of the most consecutive primes.

    >>> solution(1000000)
    997651
    >>> solution(100000)
    92951
    >>> solution(10000)
    9521
    """

    primes = prime_sieve(MAX_LIMIT)
    consecutive_seq = []
    for start in range(10):
        Sum = 0
        i = 0
        sequence = primes[start:]
        for prime in sequence:
            Sum = Sum + prime
            if Sum > MAX_LIMIT:
                break
            i = i + 1
            if binary_search(primes, Sum) != -1:
                temp = sequence[:i]
                if len(temp) > len(consecutive_seq):
                    consecutive_seq = temp

    final_ans = sum(consecutive_seq)
    return final_ans


if __name__ == "__main__":
    print(f"{solution() = }")
