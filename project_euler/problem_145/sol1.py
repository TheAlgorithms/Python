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

EVEN_DIGITS = [0, 2, 4, 6, 8]
ODD_DIGITS = [1, 3, 5, 7, 9]


def slow_reversible_numbers(
    remaining_length: int, remainder: int, digits: list[int], length: int
) -> int:
    """
    Count the number of reversible numbers of given length.
    Iterate over possible digits considering parity of current sum remainder.
    >>> slow_reversible_numbers(1, 0, [0], 1)
    0
    >>> slow_reversible_numbers(2, 0, [0] * 2, 2)
    20
    >>> slow_reversible_numbers(3, 0, [0] * 3, 3)
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
            result += slow_reversible_numbers(
                0, (remainder + 2 * digit) // 10, digits, length
            )
        return result

    result = 0
    for digit1 in range(10):
        digits[(length + remaining_length) // 2 - 1] = digit1

        if (remainder + digit1) % 2 == 0:
            other_parity_digits = ODD_DIGITS
        else:
            other_parity_digits = EVEN_DIGITS

        for digit2 in other_parity_digits:
            digits[(length - remaining_length) // 2] = digit2
            result += slow_reversible_numbers(
                remaining_length - 2,
                (remainder + digit1 + digit2) // 10,
                digits,
                length,
            )
    return result


def slow_solution(max_power: int = 9) -> int:
    """
    To evaluate the solution, use solution()
    >>> slow_solution(3)
    120
    >>> slow_solution(6)
    18720
    >>> slow_solution(7)
    68720
    """
    result = 0
    for length in range(1, max_power + 1):
        result += slow_reversible_numbers(length, 0, [0] * length, length)
    return result


def reversible_numbers(
    remaining_length: int, remainder: int, digits: list[int], length: int
) -> int:
    """
    Count the number of reversible numbers of given length.
    Iterate over possible digits considering parity of current sum remainder.
    >>> reversible_numbers(1, 0, [0], 1)
    0
    >>> reversible_numbers(2, 0, [0] * 2, 2)
    20
    >>> reversible_numbers(3, 0, [0] * 3, 3)
    100
    """
    # There exist no reversible 1, 5, 9, 13 (ie. 4k+1) digit numbers
    if (length - 1) % 4 == 0:
        return 0

    return slow_reversible_numbers(length, 0, [0] * length, length)


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
        result += reversible_numbers(length, 0, [0] * length, length)
    return result


def benchmark() -> None:
    """
    Benchmarks
    """
    # Running performance benchmarks...
    # slow_solution : 292.9300301000003
    # solution      : 54.90970860000016

    from timeit import timeit

    print("Running performance benchmarks...")

    print(f"slow_solution : {timeit('slow_solution()', globals=globals(), number=10)}")
    print(f"solution      : {timeit('solution()', globals=globals(), number=10)}")


if __name__ == "__main__":
    print(f"Solution : {solution()}")
    benchmark()

    # for i in range(1, 15):
    #     print(f"{i}. {reversible_numbers(i, 0, [0]*i, i)}")
