"""
Problem 43: https://projecteuler.net/problem=43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from itertools import permutations


def is_substring_divisible(num: tuple) -> bool:
    """
    Returns True if the pandigital number passes
    all the divisibility tests.
    >>> is_substring_divisible((0, 1, 2, 4, 6, 5, 7, 3, 8, 9))
    False
    >>> is_substring_divisible((5, 1, 2, 4, 6, 0, 7, 8, 3, 9))
    False
    >>> is_substring_divisible((1, 4, 0, 6, 3, 5, 7, 2, 8, 9))
    True
    """
    if num[3] % 2 != 0:
        return False

    if (num[2] + num[3] + num[4]) % 3 != 0:
        return False

    if num[5] % 5 != 0:
        return False

    tests = [7, 11, 13, 17]
    for i, test in enumerate(tests):
        if (num[i + 4] * 100 + num[i + 5] * 10 + num[i + 6]) % test != 0:
            return False
    return True


def solution(n: int = 10) -> int:
    """
    Returns the sum of all pandigital numbers which pass the
    divisibility tests.
    >>> solution(10)
    16695334890
    """
    return sum(
        int("".join(map(str, num)))
        for num in permutations(range(n))
        if is_substring_divisible(num)
    )


if __name__ == "__main__":
    print(f"{solution() = }")
