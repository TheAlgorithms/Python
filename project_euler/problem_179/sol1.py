"""
Project Euler Problem 179: https://projecteuler.net/problem=179

Find the number of integers 1 < n < 107, for which n and n + 1 have the same number of positive divisors. For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.

Solution: Finding divisors and than comparing with the following
number for every number between 1 and 10,000,000

"""

import math

def countDivisors(n) -> int :

    """
    Counting divisors from:
    https://www.geeksforgeeks.org/count-divisors-n-on13/?ref=lbp

    >>> countDivisors(10)
    4
    >>> countDivisors(11)
    2
    """

    cnt = 0
    for i in range(1, (int)(math.sqrt(n)) + 1) :
        if (n % i == 0) :

            # If divisors are equal,
            # count only one
            if (n / i == i) :
                cnt = cnt + 1
            else : # Otherwise count both
                cnt = cnt + 2

    return cnt


def solution() -> int:
    """
    >>> solution()
    986262

    """
    consecutive_positive_divisors = 0
    temp_divisors = 0

    for number in range(2,10_000_000):
        divisors = countDivisors(number)
        if divisors == temp_divisors:
            consecutive_positive_divisors += 1

        temp_divisors = divisors
    return consecutive_positive_divisors

if __name__ == "__main__":
    print(f"{solution() = }")