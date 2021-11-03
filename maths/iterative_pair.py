import math
import os
import random
import re
import sys
from collections import Counter
import doctest

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, ar):
    """
    >>> sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
    3
    >>> sockMerchant(4, [1, 1, 3, 3])
    2

    """

    i = 0
    occur = Counter(ar)

    for x in occur.values():
        i += x // 2
    return i


if __name__ == "__main__":

    n = int(input("Enter length of array:- \n").strip())

    ar = list(map(int, input("Enter the elements: \n").rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)
    doctest.testmod()
