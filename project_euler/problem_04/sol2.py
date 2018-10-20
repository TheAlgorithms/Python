'''
Problem:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers which is less than N.
'''
from __future__ import print_function
arr = []
for i in range(999,100,-1):
    for j in range(999,100,-1):
        t = str(i*j)
        if t == t[::-1]:
            arr.append(i*j)
arr.sort()

n=int(input())
for i in arr[::-1]:
    if(i<n):
        print(i)
        exit(0)
