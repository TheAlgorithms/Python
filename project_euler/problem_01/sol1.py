'''
Problem Statement:
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3,5,6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below N.
'''
from __future__ import print_function
try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3
n = int(raw_input().strip())
print(sum([e for e in range(3, n) if e % 3 == 0 or e % 5 == 0]))
