"""
Project Euler Problem 93: https://projecteuler.net/problem=93

By using each of the digits from the set {1, 2, 3, 4} exactly once, and making
use of the four arithmetic operations (+, -, *, /) and brackets/parentheses, it
is possible to form different positive integer targets.

For example,

    8 = (4 * (1 + 3)) / 2
    14 = 4 * (3 + 1 / 2)
    19 = 4 * (2 + 3) - 1
    36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 3 - 4, are not allowed.

Using the set {1, 2, 3, 4}, it is possible to obtain thirty-one different
target numbers, of which 28 is the highest, and the set of consecutive numbers
1 to 28 can be obtained.

Find the set of four distinct digits, a < b < c < d, for which the longest set
of consecutive positive integers, 1 to n, can be obtained, giving your answer
as a string: abcd.

References:
- https://en.wikipedia.org/wiki/Four_fours

Solution
--------
Any expression built from four numbers with brackets can be seen as repeatedly
merging two of the numbers into one with a single operation, three times in
total.  Recursing over every unordered pair therefore covers every possible
bracket structure without enumerating the brackets themselves, and because both
orders of a pair are merged there is no need to permute the digits either.

All arithmetic is done with ``fractions.Fraction`` so that divisions such as
1 / 3 stay exact.  Floating point silently destroys the answer: results that
should be whole numbers come out as 23.999999999999996 and get discarded.
"""

from collections.abc import Sequence
from fractions import Fraction
from itertools import combinations


def _merge_all(numbers: Sequence[Fraction]) -> set[Fraction]:
    """
    Return every value obtainable by merging ``numbers`` with +, -, * and /.

    >>> sorted(map(str, _merge_all([Fraction(1), Fraction(2)])))
    ['-1', '1', '1/2', '2', '3']
    """
    if len(numbers) == 1:
        return {numbers[0]}

    results: set[Fraction] = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            left, right = numbers[i], numbers[j]
            remaining = [
                numbers[index] for index in range(len(numbers)) if index not in (i, j)
            ]

            candidates = [left + right, left - right, right - left, left * right]
            if right:
                candidates.append(left / right)
            if left:
                candidates.append(right / left)

            for candidate in candidates:
                results.update(_merge_all([*remaining, candidate]))
    return results


def _consecutive_length(values: set[Fraction]) -> int:
    """
    Return how far the run 1, 2, 3, ... reaches inside ``values``.

    >>> _consecutive_length({Fraction(1), Fraction(2), Fraction(4)})
    2
    >>> _consecutive_length(set())
    0
    """
    whole_numbers = {
        int(value) for value in values if value.denominator == 1 and value > 0
    }
    length = 0
    while length + 1 in whole_numbers:
        length += 1
    return length


def solution(digits: str = "123456789") -> str:
    """
    Return the four digits that reach the longest run of consecutive integers.

    >>> solution("1234")
    '1234'
    """
    best_digits, best_length = "", 0
    candidates = sorted({int(digit) for digit in digits})
    for combination in combinations(candidates, 4):
        numbers = [Fraction(digit) for digit in combination]
        length = _consecutive_length(_merge_all(numbers))
        if length > best_length:
            best_digits = "".join(str(digit) for digit in combination)
            best_length = length
    return best_digits


if __name__ == "__main__":
    print(f"{solution() = }")
