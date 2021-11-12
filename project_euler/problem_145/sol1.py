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


def solution(number: int = 1000000000) -> int:
    """
    Loops over the range of numbers.
    Checks if they have ending zeros which disqualifies them from being reversible.
    If that condition is passed it generates the reversed number.
    Then sum up n and reverse(n).
    Then check if no number in the sum is even. If true add 1 to the answer.
    >>> solution(1000000000)
    608720
    >>> solution(1000000)
    18720
    >>> solution(1000)
    120
    """
    answer = 0
    for x in range(1, number):
        if x % 10 == 0:
            continue
        x_reverse = int(str(x)[::-1])
        summ = x + x_reverse
        if all([i not in str(summ) for i in ['2', '4', '6', '8', '0']]):
            answer += 1        
    return answer


if __name__ == "__main__":
    print(f"{solution() = }")
