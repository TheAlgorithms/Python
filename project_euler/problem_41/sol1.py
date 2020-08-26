from itertools import permutations
from math import sqrt
from typing import List

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits
1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
"""

"""
All pandigital numbers except for 1, 4 ,7 pandigital numbers are divisible by 3.
So we will check only 7 digit panddigital numbers to obtain the largest possible
pandigital prime.
"""


def is_prime(n: int) -> bool:
    """
    Returns True if n is prime,
    False otherwise.
    >>> is_prime(67483)
    False
    >>> is_prime(563)
    True
    >>> is_prime(87)
    False
    """
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n) + 1), 2):
        if n % i == 0:
            return False
    return True


def compute_pandigital_primes(n: int) -> List[int]:
    """
    Returns a list of all n-digit pandigital primes.
    >>> compute_pandigital_primes(2)
    []
    >>> max(compute_pandigital_primes(4))
    4231
    >>> max(compute_pandigital_primes(7))
    7652413
    """
    pandigital_str = "".join(str(i) for i in range(1, n + 1))
    perm_list = [int("".join(i)) for i in permutations(pandigital_str, n)]
    return [num for num in perm_list if is_prime(num)]


if __name__ == "__main__":
    print(f"{max(compute_pandigital_primes(7)) = }")
