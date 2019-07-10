"""Implementation of Basic Math in Python."""
from __future__ import division
import math

def prime_factors(n):
    """Find Prime Factors."""
    if n < 2: 
        raise ValueError('Prime factors not defined in negative numbers or 1.')

    pf = []
    for i in [2] + list(range(3, int(math.sqrt(n)) + 1, 2)):
        while n % i == 0:
            pf.append(i)
            n = n//i
    if n > 2:
        pf.append(n)
    return pf


def divisors(n):
    """returns list of divisor"""
    divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0 and i*i != n:
            divisors.append(i)
            divisors.append(n // i)
    return sorted(divisors)


def number_of_divisors(n):
    """Calculate Number of Divisors of an Integer."""
    return len(divisors(n))


def sum_of_divisors(n):
    """Calculate Sum of Divisors."""
    return sum(divisors(n))


def euler_phi(n):
    """Calculte Euler's Phi Function."""
    l = prime_factors(n)
    l = set(l)
    s = n
    for x in l:
        s *= (x - 1) / x
    return s


def main():
    """Print the Results of Basic Math Operations."""
    print(prime_factors(100))
    print(divisors(100))
    print(number_of_divisors(100))
    print(sum_of_divisors(100))
    print(euler_phi(100))


if __name__ == '__main__':
    main()
