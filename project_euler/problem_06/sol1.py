# -*- coding: utf-8 -*-
'''
Problem:
The sum of the squares of the first ten natural numbers is,
            1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
            (1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first N natural numbers and the square of the sum.
'''
from __future__ import print_function

suma = 0
sumb = 0
n = int(input())
for i in range(1,n+1):
    suma += i**2
    sumb += i
sum = sumb**2 - suma
print(sum)
