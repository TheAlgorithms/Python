#!/usr/bin/env python3

# Title: sol1.py
# Author: William Gherman
# Date: 2020-10-06
#
# Description: Solution to Project Euler problem 38, answering the question of
#              "What is the largest 1 to 9 pandigital 9-digit number that can be
#              formed as the concatenated product of an integer with (1, 2, ...,
#              n) where n > 1?"
#
#              https://projecteuler.net/problem=38


def solution() -> int:
    """
    This program searches through all positive integers under 10000, multiplies
    each candidate number i by (1, 2, ...) until the products' concatenation has
    at least nine digits. The concatenation is then checked to make sure it has
    no repeating digits or the digit zero. If the concatenation is larger than
    the largest previous result, it is replaced.
    >>> solution()
    932718654
    """
    result = 0
    for i in range(1, 9999):
        digits = ""
        current_digit = 1
        while len(digits) < 9:
            digits += str(i * current_digit)
            current_digit += 1
        if (len(digits) == 9) and (len(set(digits)) == 9) and ("0" not in digits):
            if int(digits) > result:
                result = int(digits)
    return result

if __name__ == "__main__":
    print(solution())
