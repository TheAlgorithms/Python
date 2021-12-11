"""
Problem 145: https://projecteuler.net/problem=145

Name: How many reversible numbers are there below one-billion?

Some positive integers n have the property that the
sum [ n + reverse(n) ] consists entirely of odd (decimal) digits.
For instance, 36 + 63 = 99 and 409 + 904 = 1313.
We will call such numbers reversible; so 36, 63, 409, and 904 are reversible.
Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^9)?


Solution:

Here a brute force solution is used to find and count the reversible numbers.

"""
from __future__ import annotations


def check_if_odd(sum: int = 36) -> int:
    """
    Check if the last digit in the sum is even or odd. If even return 0.
    If odd then floor division by 10 is used to remove the last number.
    Process continues until sum becomes 0 because no more numbers.
    >>> check_if_odd(36)
    0
    >>> check_if_odd(33)
    1
    """
    while sum > 0:
        if (sum % 10) % 2 == 0:
            return 0
        sum = sum // 10
    return 1


def find_reverse_number(number: int = 36) -> int:
    """
    Reverses the given number. Does not work with number that end in zero.
    >>> find_reverse_number(36)
    63
    >>> find_reverse_number(409)
    904
    """
    reverse = 0

    while number > 0:
        temp = number % 10
        reverse = reverse * 10 + temp
        number = number // 10

    return reverse


def solution(number: int = 1000000000) -> int:
    """
    Loops over the range of numbers.
    Checks if they have ending zeros which disqualifies them from being reversible.
    If that condition is passed it generates the reversed number.
    Then sum up n and reverse(n).
    Then check if all the numbers in the sum are odd. If true add to the answer.
    >>> solution(1000000000)
    608720
    >>> solution(1000000)
    18720
    >>> solution(1000000)
    18720
    >>> solution(1000)
    120
    """
    answer = 0
    for x in range(1, number):
        if x % 10 != 0:
            reversed_number = find_reverse_number(x)
            sum = x + reversed_number
            answer += check_if_odd(sum)

    return answer


if __name__ == "__main__":
    print(f"{solution() = }")
