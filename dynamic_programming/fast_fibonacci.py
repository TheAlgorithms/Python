#!/usr/bin/env python3

"""
This program calculates the nth Fibonacci number in O(log(n)).
It's possible to calculate F(1_000_000) in less than a second.
"""

a=0
b=1
c=0
count=0
l=[a,b]
n=int(input("enter a number"))
if(n<0):
    print("Enter a positive integer")
elif(n==1):
    print("Enter a number greater than 1")
else:
    while(count<n-2):
        c=a+b
        l=l+[c]
        a=b
        b=c
        count+=1
    print("The fibonacci series for",n,"is",l)
