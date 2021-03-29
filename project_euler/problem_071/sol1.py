"""
Ordered fractions
Problem 71
https://projecteuler.net/problem=71

Consider the fraction n/d, where n and d are positive
integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8
in ascending order of size, we get:
    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7,
    1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000
in ascending order of size, find the numerator of the fraction
immediately to the left of 3/7.
"""


def solution(numerator: int = 3, denominator: int = 7, limit: int = 1000000) -> int:
    """
    Returns the closest numerator of the fraction immediately to the
    left of given fraction (numerator/denominator) from a list of reduced
    proper fractions.
    >>> solution()
    428570
    >>> solution(3, 7, 8)
    2
    >>> solution(6, 7, 60)
    47
    """
    max_numerator = 0
    max_denominator = 1

    for current_denominator in range(1, limit + 1):
        current_numerator = current_denominator * numerator // denominator
        if current_denominator % denominator == 0:
            current_numerator -= 1
        if current_numerator * max_denominator > current_denominator * max_numerator:
            max_numerator = current_numerator
            max_denominator = current_denominator
    return max_numerator


if __name__ == "__main__":
    print(solution(numerator=3, denominator=7, limit=1000000))
