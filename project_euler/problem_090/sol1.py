"""
Project Euler Problem 90: https://projecteuler.net/problem=90

Each of the six faces on a cube has a different digit (0 to 9) written on it; the same
is done to a second cube. By placing the two cubes side-by-side in different positions
we can form a variety of 2-digit numbers.

For example, the square number 64 could be formed:
￼
In fact, by carefully choosing the digits on both cubes it is possible to display all
of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube
and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an
arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square
numbers to be displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not
the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last
example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of
forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers to
be displayed?
"""


from itertools import combinations, combinations_with_replacement, permutations
from math import ceil
from typing import List, Set


def split_digits(number: int, num_digits: int) -> List[int]:
    """
    Return a list of length num_digits containing the digits of a number.
    If num_digits is longer than the length of number, the list is filled
    with zero-padding to the left.
    >>> split_digits(100,3)
    [1, 0, 0]
    >>> split_digits(169,3)
    [1, 6, 9]
    >>> split_digits(169,4)
    [0, 1, 6, 9]
    >>> split_digits(169,2)
    Traceback (most recent call last):
    ValueError: num_digits must be no smaller than the length of number
    """

    if 10 ** num_digits <= number:
        raise ValueError("num_digits must be no smaller than the length of number")

    digits: List[int] = [0] * num_digits
    for index in range(num_digits):
        digits[num_digits - 1 - index] = number % 10
        number //= 10

    return digits


def test_arrangement(dice: List[set], max_digits: int) -> bool:
    """
    Check if an arrangement of two dice can represent all squares numbers
    with at most max_digits digts. Obviously, the number of dice must be at least
    as large as max_digits.
    >>> test_arrangement([{0, 5, 6, 7, 8, 9},{1, 2, 3, 4, 6, 7}], 2)
    True
    >>> test_arrangement([{0, 5, 6, 7, 8, 9},{1, 2, 3, 4, 5, 7}], 2)
    False
    >>> test_arrangement([{1,3,4,5,7,9}], 1)
    True
    >>> test_arrangement([{0, 5, 6, 7, 8, 9},{1, 2, 3, 4, 6, 7},{0,1,2,3,4,5}], 2)
    True
    >>> test_arrangement([{0, 5, 6, 7, 8, 9},{1, 2, 3, 4, 6, 7},{6,1,2,3,4,5}], 3)
    False
    >>> test_arrangement([{1,3,4,5,7,9}], 2)
    False
    """

    if len(dice) < max_digits:
        return False

    for die in dice:
        if 6 in die:
            die.add(9)
        elif 9 in die:
            die.add(6)

    for i in range(1, ceil(10 ** (max_digits / 2))):
        square: int = i * i
        digits: List[int] = split_digits(square, max_digits)
        for dice_order in permutations(dice, max_digits):
            if all(digits[i] in dice_order[i] for i in range(max_digits)):
                break
        else:
            return False

    return True


def solution(num_dice: int = 2, max_digits: int = 2) -> int:
    """
    Return the number of distinct arrangement of num_dice dice which allow for all
    square numbers with at most max_digits digits to be displayed. Obviously, num_dice
    must be >= max_digits.
    >>> solution(1, 1)
    55
    >>> solution(2, 1)
    15070
    >>> solution(1, 2)
    0
    """
    if num_dice < max_digits:
        return 0

    good_arrangements: set = set()
    dice: tuple
    dice_sets: List[Set[int]]
    sorted_dice_tuples: List[tuple]
    die_options: List[tuple] = list(combinations(range(10), 6))

    for dice in combinations_with_replacement(die_options, num_dice):
        dice_sets = list(map(set, dice))
        if test_arrangement(dice_sets, max_digits):
            sorted_dice_tuples = [tuple(sorted(die)) for die in dice]
            good_arrangements.add(tuple(sorted(sorted_dice_tuples)))

    return len(good_arrangements)


if __name__ == "__main__":
    print(f"{solution() = }")
