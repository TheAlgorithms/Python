"""
Project Euler Problem 78: https://projecteuler.net/problem=78

Let p(n) represent the number of different ways in which n coins can be
separated into piles. For example, five coins can be separated into
piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO O
OOO OO
OOO O O
OO OO O
OO O O O
O O O O O

Find the least value of n for which p(n) is divisible by one million.

References:
- https://en.wikipedia.org/wiki/Partition_(number_theory)
- https://oeis.org/A000041
"""

MODULUS = 1000000

memoize = {}
def euler(n: int) -> int:
    """
    Return the number of partitions of n elements
    as recursive sum of pentagonal numbers.

    Implemented as memoized function for performance.

    >>> euler(3)
    3
    >>> euler(4)
    5
    >>> euler(15)
    176
    >>> euler(33)
    10143
    """
    if n == 0: return 1
    if n in memoize: return memoize[n]
    S = 0
    J = n - 1
    k = 2
    while J >= 0:
        T = euler(J)
        S = S + T if (k // 2) % 2 == 1 else S - T
        J -= k if k % 2 == 1 else k // 2
        k += 1
    S = S % MODULUS
    memoize[n] = S
    return S

def solution() -> int:
    """
    Returns the first number n for which the number of
    partitions is evenly divisible by the predefined modulus.

    >>> solution()
    55374
    """
    n = 1
    while True:
        x = euler(n)
        if x == 0:
            return n
        n += 1

if __name__ == "__main__":
    print(f"{solution() = }")
