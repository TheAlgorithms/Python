"""
https://projecteuler.net/problem=51
Prime digit replacements
Problem 51
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

from typing import List


def prime_sieve(n: int) -> List[int]:
    """
    Sieve of Erotosthenes
    Function to return all the prime numbers up to a certain number
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    >>> prime_sieve(3)
    [2]
    >>> prime_sieve(50)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True

    for i in range(3, int(n ** 0.5 + 1), 2):
        index = i * 2
        while index < n:
            is_prime[index] = False
            index = index + i

    primes = [2]

    for i in range(3, n, 2):
        if is_prime[i]:
            primes.append(i)

    return primes


def solution(limit: int = 1_000_000) -> int:
    """
    Returns the solution of the problem
    >>> solution(100)
    53
    >>> solution(200)
    197
    >>> solution(1_000_000)
    997651
    """

    # Filter primes less than limit
    primes = prime_sieve(limit)
    
    # initalize is_prime
    is_prime = {}
    for i in range(limit):
        is_prime[i] = False

    partial_sum = [2]
    for index, prime in enumerate(primes[1:]):
        partial_sum.append(partial_sum[index] + prime)
        is_prime[prime] = True


    best_answer_consecutive_primes_size = -1
    best_answer = -1

    for i in range(len(primes)):
        if partial_sum[i] < limit and is_prime[partial_sum[i]]:
            if i > best_answer_consecutive_primes_size:
                best_answer_consecutive_primes_size = i
                best_answer = partial_sum[i]

        for j in range(i + 1, len(primes)):
            sum_of_consecutive_prime = partial_sum[j] - partial_sum[i]
            if sum_of_consecutive_prime >= limit:
                break

            if is_prime[sum_of_consecutive_prime]:
                if j - i > best_answer_consecutive_primes_size:
                    best_answer_consecutive_primes_size = j - i
                    best_answer = sum_of_consecutive_prime

    return best_answer



if __name__ == "__main__":
    print(solution())
