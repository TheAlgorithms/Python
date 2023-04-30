"""
Project Euler Problem 148 : https://projecteuler.net/problem=148
Author:	Sai Teja Manchi
Problem Statement:
We can easily verify that none of the entries in the
first seven rows of Pascal's triangle are divisible by 7:
                               1
                          1          1
                     1          2          1
                1          3          3          1
           1          4          6          4          1
      1          5         10         10          5          1
1          6         15         20         15          6          1
However, if we check the first one hundred rows, we will find that
only 2361 of the 5050 entries are not divisible by 7.
Find the number of entries which are not divisible by 7
in the first one billion (109) rows of Pascal's triangle.
"""

def get_num_binomials(row_num: int) -> int:
    """
    To compute the number of entries in the nth row of
    pascal triangle that are not divisble by 7.
    To compute the number of entries in the nth row of
    pascal triangle that are not divisble by 7.
    Based on Lucas Theroem it is the product of (each digit in the base 7 n + 1)
    Reference: https://brilliant.org/wiki/lucas-theorem/
    >>> get_num_binomials(3)
    4
    >>> get_num_binomials(6)
    7
    >>> get_num_binomials(10)
    8
    """
    cnt = 1
    while row_num > 0:
        cnt *= (row_num % 7) + 1
        row_num //= 7
    return cnt

def solution(pascal_row_count: int = 10**9) -> int:
    """
    To evaluate the solution, use solution()
    >>> solution(3)
    6
    >>> solution(10)
    40
    >>> solution(100)
    2361
    """

    result = 0
    for i in range(pascal_row_count):
        result += get_num_binomials(i)

    return result
