"""
Finding the continuous fraction for a rational number using python

https://en.wikipedia.org/wiki/Continued_fraction
"""


from fractions import Fraction
from math import floor


def continued_fraction(num: Fraction) -> list[int]:
    """
    :param num:
    Fraction of the number whose continued fractions to be found.
    Use Fraction(str(number)) for more accurate results due to
    float inaccuracies.

    :return:
    The continued fraction of rational number.
    It is the all commas in the (n + 1)-tuple notation.

    >>> continued_fraction(Fraction(2))
    [2]
    >>> continued_fraction(Fraction("3.245"))
    [3, 4, 12, 4]
    >>> continued_fraction(Fraction("2.25"))
    [2, 4]
    >>> continued_fraction(1/Fraction("2.25"))
    [0, 2, 4]
    >>> continued_fraction(Fraction("415/93"))
    [4, 2, 6, 7]
    >>> continued_fraction(Fraction(0))
    [0]
    >>> continued_fraction(Fraction(0.75))
    [0, 1, 3]
    >>> continued_fraction(Fraction("-2.25"))    # -2.25 = -3 + 0.75
    [-3, 1, 3]
    """
    numerator, denominator = num.as_integer_ratio()
    continued_fraction_list: list[int] = []
    while True:
        integer_part = floor(numerator / denominator)
        continued_fraction_list.append(integer_part)
        numerator -= integer_part * denominator
        if numerator == 0:
            break
        numerator, denominator = denominator, numerator

    return continued_fraction_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("Continued Fraction of 0.84375 is: ", continued_fraction(Fraction("0.84375")))
