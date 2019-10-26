"""
Problem:
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""

#!/usr/bin/env python
from itertools import *

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def digits(n):
    return list(map(int, str(n)))

def is_increasing(n):
    return all(prev <= curr for prev, curr in pairwise(digits(n)))

def is_decreasing(n):
    return all(prev >= curr for prev, curr in pairwise(digits(n)))

def is_bouncy(n):
    return not is_increasing(n) and not is_decreasing(n)

def running_total(iterable):
    total = 0
    for element in iterable:
        total += element
        yield total

def main():
    nums = count(1)
    bouncy = running_total(map(lambda n: float(is_bouncy(n)), count(1)))
    print(next((n for n, b in zip(nums, bouncy) if b / n == 0.99)))

if __name__ == "__main__": main()
