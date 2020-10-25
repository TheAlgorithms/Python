"""
https://projecteuler.net/problem=50
Consecutive prime sum
Problem 50

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

def is_prime(val: int) -> bool:
    """
    Determines whether value is a prime or not.

    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(15)
    False
    """

    if val == 2:
        return True
    elif val % 2 == 0:
        return False
    else:
        for i in range(3, val // 2, 2):
            if val % i == 0:
                return False
        return True
