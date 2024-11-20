"""
Problem 20: https://projecteuler.net/problem=20

n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

from math import factorial


def solution(num: int = 100) -> int:
    """Returns the sum of the digits in the factorial of num
    >>> solution(1000)
    10539
    >>> solution(200)
    1404
    >>> solution(100)
    648
    >>> solution(50)
    216
    >>> solution(10)
    27
    >>> solution(5)
    3
    >>> solution(3)
    6
    >>> solution(2)
    2
    >>> solution(1)
    1
    >>> solution(0)
    1
    """
    return sum(map(int, str(factorial(num))))


if __name__ == "__main__":
    print(solution(int(input("Enter the Number: ").strip())))
