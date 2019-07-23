"""
Problem Statement:
Work out the first ten digits of the sum of the following one-hundred 50-digit
numbers.
"""
from __future__ import print_function
import os

try:
    raw_input  # Python 2
except NameError:
    raw_input = input  # Python 3


def solution(array):
    """Returns the first ten digits of the sum of the array elements.
    
    >>> sum = 0
    >>> array = []
    >>> with open(os.path.dirname(__file__) + "/num.txt","r") as f:
    ...     for line in f:
    ...         array.append(int(line))
    ...
    >>> solution(array)
    '5537376230'
    """
    return str(sum(array))[:10]


if __name__ == "__main__":
    n = int(input().strip())

    array = []
    for i in range(n):
        array.append(int(input().strip()))
    print(solution(array))
