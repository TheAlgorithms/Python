"""
Project Euler Problem 204: https://projecteuler.net/problem=204

Problem Statement:
A Hamming number is a positive number which has no prime factor larger than 5.
So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
There are 1105 Hamming numbers not exceeding 10^8.

We will call a positive number a generalised Hamming number of type n,
if it has no prime factor larger than n.
Hence the Hamming numbers are the generalised Hamming numbers of type 5.

How many generalised Hamming numbers of type 100 are there which don't exceed
10^9?

Solution explanation:
We find all the prime numbers using the standar prime sieve. Then we find the
eligible combinations of the prime factors.
"""

primes = []


def find(x: int = 1, indexMinPrime: int = 0, limit: int = 1000000000) -> int:
    """
    The function returns the number of hamming numbers where at least one
    prime factor is prime and a factor of x.

    This is a recursive function that outputs based on the list primes.
    If the list is empty, then:

    >>> search()
    1
    """
    result = 1
    for i in range(indexMinPrime, len(primes)):
        product = primes[i]*x
        if product > limit:
            break
        result += search(product, i)
    return result


def solution(limit: int = 100000000, hamming: int = 100) -> int:
    """
    The solution the basic prime sieve to find the  prime numbers
    This followed by the search funciton for finding the eligible primes
    that are also a factor

    We iterate from 2:hamming and iterate consequently in primes list.
    If the number in primes is greater than the iteration number, we break.
    if its a factor, its not prime and then we break.
    If after this, it remains prime, we add it to list of primes.
    Then we apply the search function.

    >>>solution(100000000, 5)
    1530
    >>solution(100000000, 15)
    27365
    >>>solution(1000000000,50)
    735425
    """
    for i in range(2, hamming + 1):
        isPrime = True
        for p in primes:
            if p * p > i:
                break
            if i % p == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
    return find()


if __name__ == "__main__":
    print(f"{solution() = }")
