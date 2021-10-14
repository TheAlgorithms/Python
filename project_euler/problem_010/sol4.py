"""
Project Euler Problem 10: https://projecteuler.net/problem=10
Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
References:
    - https://en.wikipedia.org/wiki/Prime_number
    - https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

import math

def primeList(n: int) -> list:
    """
    Returns a boolean list where true means the index represents a prime number
    >>> primeList(10)
    [False, False, True, True, False, True, False, True, False, False, False]
    >>> primeList(23)
    [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True, False, False, False, True]
    """
    primes = [True] * (n+1)
    primes[0] = False # 0 is no prime
    primes[1] = False # 1 is no prime
    for i in range(2,math.floor(math.sqrt(n))+1): # using sieve of eratosthenes to strike all none primes in the list
        if primes[i]:
            for j in range(i*i,n+1,i):
                primes[j] = False
    return primes

def sumPrime(n: int) -> int:
    """
    Return the sum of all primes < n
    >>> sumPrime(10)
    17
    >>> sumPrime(1000)
    76127
    >>> sumPrime(5000)
    1548136
    """
    sum = 0 # Set initial sum to zero, in case a number less than 2 is passed
    primes = primeList(n) # get boolean-list of all numbers from 0 - n where true means the number is prime
    for i in range(2,n+1):
        if primes[i]:
            sum = sum + (i)
    return sum

print(sumPrime(2000000))
