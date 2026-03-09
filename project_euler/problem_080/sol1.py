"""
Project Euler Problem 80: https://projecteuler.net/problem=80
Author: Sandeep Gupta
Problem statement: For the first one hundred natural numbers, find the total of
the digital sums of the first one hundred decimal digits for all the irrational
square roots.
Time: 5 October 2020, 18:30
"""

import decimal


def solution() -> int:
    """
    To evaluate the sum, Used decimal python module to calculate the decimal
    places up to 100, the most important thing would be take calculate
    a few extra places for decimal otherwise there will be rounding
    error.

    >>> solution()
    40886
    """
    answer = 0
    decimal_context = decimal.Context(prec=105)
    for i in range(2, 100):
        number = decimal.Decimal(i)
        sqrt_number = number.sqrt(decimal_context)
        if len(str(sqrt_number)) > 1:
            answer += int(str(sqrt_number)[0])
            sqrt_number_str = str(sqrt_number)[2:101]
            answer += sum(int(x) for x in sqrt_number_str)
    return answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{solution() = }")
