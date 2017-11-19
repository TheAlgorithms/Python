"""
Problem Statement:
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below N.

For doctests run the following command:
python -m doctest -v sol1.py
or
python3 -m doctest -v sol1.py
For manual testing run:
python sol1.py
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
    total = 0
    for number in range(3, limit):
        if number % 3 == 0 or number % 5 == 0:
            total += number
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
