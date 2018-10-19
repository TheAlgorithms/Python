'''
Problem Statement:
Work out the first ten digits of the sum of the N 50-digit numbers.
'''
from __future__ import print_function

n = int(raw_input().strip())

array = []
for i in range(n):
    array.append(int(raw_input().strip()))

print(str(sum(array))[:10])

