"""
Problem 34: https://projecteuler.net/problem=34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

from math import factorial
import time
start_time = time.time()

def sum_of_digit_factorial(n: int, lookup: list, memo: dict) -> int:
    """
    Returns the sum of the factorial of digits in n
    """
    if n in memo:
        return memo[n]
    s = 0
    for d in str(n):
        s += lookup[int(d)]
    memo[n] = s
    return s

def solution() -> int:
    """
    Returns the sum of all numbers whose
    sum of the factorials of all digits
    add up to the number itself.
    """
    lookup = [factorial(d) for d in range(10)]
    memo = {}
    result = 0
    for n in range(10, 100000):
        if n > sum_of_digit_factorial(n, lookup, memo):
            continue
        if n == sum_of_digit_factorial(n, lookup, memo):
            result += n
    return result

print(f"{solution() = }")
print("Process finished --- %s seconds ---" % (time.time() - start_time))
