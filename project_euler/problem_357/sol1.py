"""
Problem 206 : https://projecteuler.net/problem=357

Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.

Solution: Since all numbers are divisible by 1 than 1 plus the number
must be a prime, so possible prime generating integers are prime - 1.
d+30/d is actually the pairs of factors so adding the factor pairs and checking
if it is prime determines if the number is a prime generating integer.

"""

import math


def sieve_of_eratosthenes(n) -> [int]:
    """
    https://www.geeksforgeeks.org/sieve-of-eratosthenes/?ref=lbp
    Creating list of primes

    >>> sieve_of_eratosthenes(10)
    [2, 3, 5, 7]

    >>> sieve_of_eratosthenes(20)
    [2, 3, 5, 7, 11, 13, 17, 19]

    """

    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true. A value
    # in prime[i] will finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it is
        # a prime
        if prime[p]:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    primes = []

    # adding primes into list
    for p in range(2, n):
        if prime[p]:
            primes.append(p)
    return primes


def is_prime(n) -> bool:
    """
    https://www.rookieslab.com/posts/fastest-way-to-check-if-a-number-is-prime-or-not
    Checks if number is prime

    >>> is_prime(11)
    True

    >>> is_prime(12)
    False

    """

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i * i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True


def get_divisors(n) -> bool:
    """
    Modified from:
    https://www.geeksforgeeks.org/find-all-divisors-of-a-natural-number-set-2/
    Gets and checks if divisors are prime generating

    >>> get_divisors(6)
    True

    >>> get_divisors(12)
    False

    """
    # method to get divisors

    for i in range(1, int(math.sqrt(n) + 1)):

        # skips 1 and the number it self since prime
        if i == 1:
            continue

        # checks all other divisors
        elif n % i == 0:

            # add pairs of divisors
            possible_prime = 0
            possible_prime += i
            if n / i == i:
                possible_prime += i
            else:
                possible_prime += int(n / i)

            # checks if pairs are primes
            if not is_prime(possible_prime):
                return False

    return True


def solution() -> int:

    """
    >>> solution()
    1739023853137
    """

    # making list of primes
    primes = sieve_of_eratosthenes(100_000_000)

    total = 0

    # checking for possible primes generators
    for prime in primes:

        # has to be a prime - 1 since all numbers are divisible by 1
        possible_prime_generating = prime - 1
        if get_divisors(possible_prime_generating):
            total += possible_prime_generating

    return total


if __name__ == "__main__":
    print(f"{solution() = }")
