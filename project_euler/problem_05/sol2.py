#!/bin/python3
'''
Problem:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible(divisible with no remainder) by all of the numbers from 1 to N?
'''

""" Euclidean GCD Algorithm """
def gcd(x,y):
    return x if y==0 else gcd(y,x%y)

""" Using the property lcm*gcd of two numbers = product of them """
def lcm(x,y):
    return (x*y)//gcd(x,y)

n = int(raw_input())
g=1
for i in range(1,n+1):
    g=lcm(g,i)
print(g)
