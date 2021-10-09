"""
Project Euler Problem 73: https://projecteuler.net/problem=73

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1,
it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size,
we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7,
3/4, 4/5, 5/6, 6/7, 7/8
It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced
proper fractions for d ≤ 12,000?

References
  - https://en.wikipedia.org/wiki/Euclidean_division

"""

from math import gcd


def solution(input: int = 12000) -> int:
    """
    Returns the number of fractions lying between 1/3 and 1/2 in the sorted set of
    reduced proper fractions for d ≤ 12,000.

    >>> solution(500)
    12687
    >>> solution(6000)
    1823861
    >>> solution(12000)
    7295372
    >>> solution()
    7295372
    """

    result = 0

    # loop through all the possible fractions for a given value of d
    for numerator in range(1, input):
        for denominator in range(numerator + 1, input + 1):
            # count only if the fractions are reduced and lie in the range (1/3, 1/2)
            if (
                1 / 3 < numerator / denominator < 0.5
                and gcd(numerator, denominator) == 1
            ):
                result += 1

    return result


if __name__ == "__main__":
    print(f"{solution() = }")
