"""
Project Euler Problem 38: https://projecteuler.net/problem=38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call
192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

from itertools import permutations


def test_pandigital_factors(pan: str, count: int, factor: int) -> bool:
    """Returns True if the input panditigal, count, and factor meet the problem criteria

    >>> test_pandigital_factors('12', 3, 1)
    False
    >>> test_pandigital_factors('12', 2, 1)
    True
    >>> test_pandigital_factors('78156234', 3, 78)
    True
    """
    for c in range(1, count + 1):
        test = str(factor * c)
        if test == pan[: len(test)]:
            pan = pan[len(test) :]
        else:
            return False

    if pan == "":
        return True

    return False


def find_factors(pan: str) -> tuple:
    """Returns the count and factor that meets the problem criteria for the input

    >>> find_factors('12')
    (2, 1)
    >>> find_factors('78156234')
    (3, 78)
    """
    is_factor = False

    for i in range(1, 9):
        factor = int(pan[:i])
        for count in range(2, 10):
            if test_pandigital_factors(pan, count, factor):
                is_factor = True
                break

        if is_factor:
            break

    if is_factor:
        return (count, factor)
    else:
        return (None, None)


def test_permutations(digits: list, print_factors: bool = False) -> int:
    """Returns first permutation of the input digits that meets problem criteria.

    >>> test_permutations([2, 1])
    12
    >>> test_permutations([8, 7, 6, 5, 4, 3, 2, 1])
    78156234
    """
    for pan in permutations(digits):
        pan = "".join([str(i) for i in pan])
        (count, factor) = find_factors(pan)
        if count:
            break

    if print_factors is True:
        print(pan)
        for c in range(1, count + 1):
            product = c * factor
            print(f"{c} * {factor} = {product}")

    return int(pan)


def solution(digit_range: list = list(range(1, 10))) -> int:
    """Returns the Euler 38 solution

    Finds the largest pandigital from the provided list of ints where the
    solution is also the concatenated products of of counting numbers in seq

    >>> solution()
    932718654
    >>> solution([1, 2, 3, 4])
    1234
    """
    digit_range = sorted(digit_range, reverse=True)
    return test_permutations(digit_range)


if __name__ == "__main__":
    print(f"{solution() = }")
