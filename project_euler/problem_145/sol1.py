"""
Project Euler problem 145: https://projecteuler.net/problem=145
Author: Vineet Rao, Maxim Smolskiy
Problem statement:

Some positive integers n have the property that the sum [ n + reverse(n) ]
consists entirely of odd (decimal) digits.
For instance, 36 + 63 = 99 and 409 + 904 = 1313.
We will call such numbers reversible; so 36, 63, 409, and 904 are reversible.
Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^9)?
"""
EVEN_DIGITS = [digit for digit in range(10) if digit % 2 == 0]
ODD_DIGITS = [digit for digit in range(10) if digit % 2 == 1]


def reversible_numbers(
    remaining_length: int, remainder: int, digits: list, length: int
) -> int:
    """
    Count the number of reversible numbers of given length.
    >>> reversible_numbers(1, 0, [None], 1)
    0
    >>> reversible_numbers(2, 0, [None] * 2, 2)
    20
    >>> reversible_numbers(3, 0, [None] * 3, 3)
    100
    """
    if remaining_length == 0:
        if digits[0] == 0 or digits[-1] == 0:
            return 0

        for i in range(length // 2 - 1, -1, -1):
            remainder += digits[i] + digits[length - i - 1]

            if remainder % 2 == 0:
                return 0

            remainder //= 10

        return 1

    if remaining_length == 1:
        if remainder % 2 == 0:
            return 0

        result = 0
        for digit in range(10):
            digits[length // 2] = digit
            result += reversible_numbers(
                0, (remainder + 2 * digit) // 10, digits, length
            )
        return result

    result = 0
    for digit1 in range(10):
        digits[(length + remaining_length) // 2 - 1] = digit1

        if (remainder + digit1) % 2 == 0:
            OTHER_DIGITS = ODD_DIGITS
        else:
            OTHER_DIGITS = EVEN_DIGITS

        for digit2 in OTHER_DIGITS:
            digits[(length - remaining_length) // 2] = digit2
            result += reversible_numbers(
                remaining_length - 2,
                (remainder + digit1 + digit2) // 10,
                digits,
                length,
            )
    return result


def solution(max_power: int = 9) -> int:
    """
    To evaluate the solution, use solution()
    >>> solution(3)
    120
    >>> solution(6)
    18720
    >>> solution(7)
    68720
    """
    result = 0
    for length in range(1, max_power + 1):
        result += reversible_numbers(length, 0, [None] * length, length)
    return result


if __name__ == "__main__":
    print(f"{solution() = }")
