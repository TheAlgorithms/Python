"""
Farey Sequence Generator

The Farey sequence of order n is the sequence of completely reduced
fractions between 0 and 1 which have denominators less than or equal to n,
arranged in increasing order.

Reference: https://en.wikipedia.org/wiki/Farey_sequence
"""

from fractions import Fraction


def farey_sequence(order: int) -> list[Fraction]:
    """
    Generate the Farey sequence of a given order in ascending order.

    :param order: The maximum denominator allowed in the fractions.
    :return: A list of Fraction objects in ascending order.

    >>> farey_sequence(1)
    [Fraction(0, 1), Fraction(1, 1)]
    >>> farey_sequence(2)
    [Fraction(0, 1), Fraction(1, 2), Fraction(1, 1)]
    >>> farey_sequence(3)
    [Fraction(0, 1), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(1, 1)]
    >>> [(f.numerator, f.denominator) for f in farey_sequence(4)]
    [(0, 1), (1, 4), (1, 3), (1, 2), (2, 3), (3, 4), (1, 1)]
    >>> farey_sequence(0)
    Traceback (most recent call last):
        ...
    ValueError: Order must be a positive integer
    >>> farey_sequence(-3)
    Traceback (most recent call last):
        ...
    ValueError: Order must be a positive integer
    >>> farey_sequence("5")
    Traceback (most recent call last):
        ...
    TypeError: Order must be an integer
    """
    if not isinstance(order, int) or isinstance(order, bool):
        raise TypeError("Order must be an integer")
    if order < 1:
        raise ValueError("Order must be a positive integer")

    sequence: list[Fraction] = [Fraction(0, 1)]
    numerator1, denominator1 = 0, 1
    numerator2, denominator2 = 1, order

    sequence.append(Fraction(numerator2, denominator2))

    while numerator2 != 1 or denominator2 != 1:
        scale_factor = (denominator1 + order) // denominator2
        next_numerator = scale_factor * numerator2 - numerator1
        next_denominator = scale_factor * denominator2 - denominator1

        sequence.append(Fraction(next_numerator, next_denominator))

        numerator1, denominator1 = numerator2, denominator2
        numerator2, denominator2 = next_numerator, next_denominator

    return sequence


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("Farey sequence of order 4:")
    print(farey_sequence(4))
