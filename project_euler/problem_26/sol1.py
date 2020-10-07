"""
Euler Problem 26
https://projecteuler.net/problem=26

Problem Statement:

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
"""


def find_digit(numerator: int, digit: int) -> int:
    """
    Considering any range can be provided,
    because as per the problem, the digit d < 1000
    >>> find_digit(1, 10)
    7
    >>> find_digit(10, 100)
    97
    >>> find_digit(10, 1000)
    983
    """
    the_digit = 1
    longest_list_length = 0

    for divide_by_number in range(numerator, digit + 1):
        has_been_divided = []
        now_divide = numerator
        for division_cycle in range(1, digit + 1):
            if now_divide in has_been_divided:
                if longest_list_length < len(has_been_divided):
                    longest_list_length = len(has_been_divided)
                    the_digit = divide_by_number
            else:
                has_been_divided.append(now_divide)
                now_divide = now_divide * 10 % divide_by_number

    return the_digit


def solution(n: int = 1000) -> int:
    """
    Find the value of n < 1000 for which 1/n contains the longest recurring cycle
    in its decimal fraction part.

    >>> solution(10)
    7
    >>> solution(100)
    97
    >>> solution(1000)
    983

    """

    return find_digit(1, n)


if __name__ == "__main__":
    print(solution(int(str(input()).strip())))
