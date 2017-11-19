"""
Problem Statement:
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below N.

For doctests run the following command:
python -m doctest -v sol3.py
or
python3 -m doctest -v sol3.py
For manual testing run:
python sol3.py
"""

from __future__ import print_function

def calculate_sum(limit):
    """Pure implementation of the solution in Python.
    :param limit: the highest number that gets checked
    :return: the sum of all integers divisible by 3 or 5 until the limit.
    Examples:
    >>> calculate_sum(10)
    23
    >>> calculate_sum(100)
    2318
    >>> calculate_sum(1000)
    233168
    """
    # Strategy
    #
    # Utilize the patterns in the space between dividends.
    # e.g.
    # Numbers:  3   5   6   9   10   12   15...
    # Space:      2   1   3   1    2    3...

    total = 0
    num = 0
    while 1:
        num += 3
        if num >= limit:
            break
        total += num
        num += 2
        if num >= limit:
            break
        total += num
        num += 1
        if num >= limit:
            break
        total += num
        num += 3
        if num >= limit:
            break
        total += num
        num += 1
        if num >= limit:
            break
        total += num
        num += 2
        if num >= limit:
            break
        total += num
        num += 3
        if num >= limit:
            break
        total += num
    return total

def main():
    """Gets executed when the file is called."""
    import sys
    # For python 2.x and 3.x compatibility: 3.x has no raw_input builtin
    # otherwise 2.x's input builtin function is too "smart"
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function("Enter number: ")
    integer = int(user_input)
    print(calculate_sum(integer))

if __name__ == '__main__':
    main()
