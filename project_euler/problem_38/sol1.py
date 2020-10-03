"""
Project Euler Problem 38
https://projecteuler.net/problem=38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""


def solution() -> int:
    """
    Calculates and returns the largest 1-9 pandigital 9-digit number as product of
    integer set n>1.

    Answer:
    >>> solution()
    932718654

    Assumptions:
    1. Since n>1, we'll concatenate the fixed number at least twice. We only need
         9 digits, so 2x5=10 would exceed this safely. Thus target number is 4
         digits or less.
    2. We know at least one 9-digit pandigital starts with 9 as per the example,
         so can short circuit search based on that.
    3. We can start with 90, the next 9-start number following 9 (already calculated)
    """

    largest_pandigital = 918273645

    for fixed_num in range(90, 10000):  # assumption 1 and 3
        if not str(fixed_num).startswith("9"):  # assumption 2
            continue

        pan = fixed_num
        i = 2
        while len(str(pan)) < 9:
            pan = int(str(pan) + str(fixed_num * i))

        if is_pandigital(pan) and pan > largest_pandigital:
            largest_pandigital = pan

    return largest_pandigital


def is_pandigital(num: int) -> bool:
    """
    Validates that a number is 9-digit pandigital.
    i.e. contains all numbers 1-9 without zero.

    Examples:
    >>> is_pandigital(123456789)
    True
    >>> is_pandigital(987654321)
    True
    >>> is_pandigital(1234567890)
    False
    >>> is_pandigital(111111111)
    False
    """

    # check that only digits 1-9 are present with no duplicates
    numberset = set(str(num))
    return len(numberset) == 9 and "0" not in numberset


if __name__ == "__main__":

    print(solution())
