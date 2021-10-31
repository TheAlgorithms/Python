"""
Problem 95 Amicable chains: https://projecteuler.net/problem=95

Description:


The proper divisors of a number
are all the divisors excluding the number itself.
For example, the proper divisors of 28 are 1, 2, 4, 7, and 14.
As the sum of these divisors is equal to 28, we call it a perfect number.
Interestingly,
the sum of the proper divisors of 220 is 284
and the sum of the proper divisors of 284 is 220,
forming a chain of two numbers.
For this reason, 220 and 284 are called an amicable pair.


Perhaps less well known are longer chains.
For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.
Find the smallest member of the longest amicable chain
with no element exceeding one million.


Solution:

Given an initial number x_0,
we can determine whether if forms an amicable chain
with no element exceeding one million by following a few basic rules.
- Compute x_i := sum of the proper divisors of x_(i-1)
    - If x_i > 1.000.000, discard the chain.
    - If x_i == x_j, for j in {1, ..., i-1}, discard the chain
        because we found a loop that doesn't start with x_0
    - If x_i == x_0, we found an amicable chain


Time: 111 sec
"""

from math import sqrt

DIVISORS_SUM = {}
MAX = 10 ** 6
CANDIDATES = [n for n in range(4, MAX)]


def divisors_sum(N: int) -> int:
    """
    Returns the sum of the proper divisors of N.

    >>> divisors_sum(7)
    1
    >>> divisors_sum(284)
    220
    >>> divisors_sum(12496)
    14288
    """

    if N in DIVISORS_SUM.keys():
        return DIVISORS_SUM[N]

    if N == 1:
        return 1

    sum = 1
    i = 2
    while i <= sqrt(N):
        if N % i == 0:
            if i == N / i:
                sum += i
            else:
                sum += i + int(N / i)
        i += 1
    DIVISORS_SUM[N] = sum
    return sum


def check_chain(N: int):
    """
    Given a starting point N, it check whether this forms an amicable chain
    with no element exceeding one million.
    If so, it returns the chain as a list.
    Otherwise, it returns False.

    >>> check_chain(7)
    False
    >>> check_chain(284)
    [284, 220]
    >>> check_chain(12496)
    [12496, 14288, 15472, 14536, 14264]

    """

    chain = [N]
    run = True

    while run:
        next = divisors_sum(chain[-1])

        if next > MAX:
            return False

        elif next == N:
            return chain

        elif next in chain:  # it can't be N because we already checked
            return False
        chain.append(next)


def solution():
    """
    It computes the longest amicable chain with no element
    exceeding one million and it returns the smallest member.
    """
    longest_chain = []

    for N in CANDIDATES:
        chain = check_chain(N)
        if chain:
            if len(chain) > len(longest_chain):
                longest_chain = chain
    return min(longest_chain)


if __name__ == "__main__":
    print(f"{solution() = }")
