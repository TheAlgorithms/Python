"""
Problem 33: https://projecteuler.net/problem=33

The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe
that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator
and denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""

from __future__ import annotations

from fractions import Fraction


def is_digit_cancelling(num: int, den: int) -> bool:
    return (
        num != den and num % 10 == den // 10 and (num // 10) / (den % 10) == num / den
    )


def fraction_list(digit_len: int) -> list[str]:
    """
    >>> fraction_list(2)
    ['16/64', '19/95', '26/65', '49/98']
    >>> fraction_list(3)
    ['16/64', '19/95', '26/65', '49/98']
    >>> fraction_list(4)
    ['16/64', '19/95', '26/65', '49/98']
    >>> fraction_list(0)
    []
    >>> fraction_list(5)
    ['16/64', '19/95', '26/65', '49/98']
    """
    solutions = []
    den = 11
    last_digit = int("1" + "0" * digit_len)
    for num in range(den, last_digit):
        while den <= 99:
            if (num != den) and (num % 10 == den // 10) and (den % 10 != 0):
                if is_digit_cancelling(num, den):
                    solutions.append(f"{num}/{den}")
            den += 1
        num += 1
        den = 10
    return solutions


def solution(n: int = 2) -> int:
    """
    Return the solution to the problem
    """
    result = 1.0
    for fraction in fraction_list(n):
        frac = Fraction(fraction)
        result *= frac.denominator / frac.numerator
    return int(result)


if __name__ == "__main__":
    print(solution())
