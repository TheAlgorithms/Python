"""
Project Euler problem 145: https://projecteuler.net/problem=145
Author: Vineet Rao
Problem statement:

Some positive integers n have the property that the sum [ n + reverse(n) ]
consists entirely of odd (decimal) digits.
For instance, 36 + 63 = 99 and 409 + 904 = 1313.
We will call such numbers reversible; so 36, 63, 409, and 904 are reversible.
Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^9)?
"""


def odd_digits(num: int) -> bool:
    """
    Check if the number passed as argument has only odd digits.
    >>> odd_digits(123)
    False
    >>> odd_digits(135797531)
    True
    """
    num_str = str(num)
    for i in ["0", "2", "4", "6", "8"]:
        if i in num_str:
            return False
    return True


def solution(max_num: int = 1_000_000_000) -> int:
    """
    To evaluate the solution, use solution()
    >>> solution(1000)
    120
    >>> solution(1_000_000)
    18720
    >>> solution(10_000_000)
    68720
    """
    result = 0
    # All single digit numbers reverse to themselves, so their sums are even
    # Therefore at least one digit in their sum is even
    # Last digit cannot be 0, else it causes leading zeros in reverse
    for num in range(11, max_num):
        if num % 10 == 0:
            continue
        num_sum = num + int(str(num)[::-1])
        num_is_reversible = odd_digits(num_sum)
        result += 1 if num_is_reversible else 0
    return result


if __name__ == "__main__":
    print(f"{solution() = }")
