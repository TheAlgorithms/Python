# -*- coding: utf-8 -*-
"""
The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000
digits?
"""


def solution(n):
    """Returns the index of the first term in the Fibonacci sequence to contain
    n digits.

    >>> solution(1000)
    4782
    >>> solution(100)
    476
    >>> solution(50)
    237
    >>> solution(3)
    12
    """
    f1, f2 = 1, 1
    index = 2
    while True:
        i = 0
        f = f1 + f2
        f1, f2 = f2, f
        index += 1
        for j in str(f):
            i += 1
        if i == n:
            break
    return index


if __name__ == "__main__":
    print(solution(int(str(input()).strip())))
