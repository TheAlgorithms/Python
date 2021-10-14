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

def prime_list(upper_border: int) -> list:
    """
    Returns a boolean list where true means the index represents a prime number
    >>> prime_list(10)
    [False, False, True, True, False, True, False, True, False, False, False]
    >>> prime_list(23)
    [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True, False, False, False, True]
    """
    primes = [True] * (upper_border+1)
    primes[0] = False # 0 is no prime
    primes[1] = False # 1 is no prime
    for i in range(2,math.floor(math.sqrt(upper_border))+1): # using sieve of eratosthenes to strike all none primes in the list
        if primes[i]:
            for j in range(i*i,upper_border+1,i):
                primes[j] = False
    return primes

def sum_prime(upper_border: int) -> int:
    """
    Return the sum of all primes < n
    >>> sum_prime(10)
    17
    >>> sum_prime(1000)
    76127
    >>> sum_prime(5000)
    1548136
    """
    sum = 0 # Set initial sum to zero, in case a number less than 2 is passed
    primes = prime_list(upper_border) # get boolean-list of all numbers from 0 - n where true means the number is prime
    for i in range(2,upper_border+1):
        if primes[i]:
            sum = sum + (i)
    return sum

print(sum_prime(2000000))
