"""
Project Euler Problem 104 : https://projecteuler.net/problem=104

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number
for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9,
but not necessarily in order). And F2749, which contains 575 digits, is the first
Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND
the last nine digits are 1-9 pandigital, find k.
"""

import sys

sys.set_int_max_str_digits(0)  # type: ignore


def is_pandigital_both(number: int) -> bool:
    """
    Takes a number and checks if it is pandigital both from start and end


    >>> is_pandigital_both(123456789987654321)
    True

    >>> is_pandigital_both(120000987654321)
    False

    >>> is_pandigital_both(1234567895765677987654321)
    True

    """

    check_last = [0] * 11
    check_front = [0] * 11

    # mark last 9 numbers
    for _ in range(9):
        check_last[int(number % 10)] = 1
        number = number // 10
    # flag
    f = True

    # check last 9 numbers for pandigitality

    for x in range(9):
        if not check_last[x + 1]:
            f = False
    if not f:
        return f

    # mark first 9 numbers
    number = int(str(number)[:9])

    for _ in range(9):
        check_front[int(number % 10)] = 1
        number = number // 10

    # check first 9 numbers for pandigitality

    for x in range(9):
        if not check_front[x + 1]:
            f = False
    return f


def is_pandigital_end(number: int) -> bool:
    """
    Takes a number and checks if it is pandigital from END

    >>> is_pandigital_end(123456789987654321)
    True

    >>> is_pandigital_end(120000987654321)
    True

    >>> is_pandigital_end(12345678957656779870004321)
    False

    """

    check_last = [0] * 11

    # mark last 9 numbers
    for _ in range(9):
        check_last[int(number % 10)] = 1
        number = number // 10
    # flag
    f = True

    # check last 9 numbers for pandigitality

    for x in range(9):
        if not check_last[x + 1]:
            f = False
    return f


def solution() -> int:
    """
    Outputs the answer is the least Fibonacci number pandigital from both sides.
    >>> solution()
    329468
    """

    a = 1
    b = 1
    c = 2
    # temporary Fibonacci numbers

    a1 = 1
    b1 = 1
    c1 = 2
    # temporary Fibonacci numbers mod 1e9

    # mod m=1e9, done for fast optimisation
    tocheck = [0] * 1000000
    m = 1000000000

    for x in range(1000000):
        c1 = (a1 + b1) % m
        a1 = b1 % m
        b1 = c1 % m
        if is_pandigital_end(b1):
            tocheck[x + 3] = 1

    for x in range(1000000):
        c = a + b
        a = b
        b = c
        # perform check only if in tocheck
        if tocheck[x + 3] and is_pandigital_both(b):
            return x + 3  # first 2 already done
    return -1


if __name__ == "__main__":
    print(f"{solution() = }")
