"""A Pythagorean triplet is a set of three natural numbers, for which,
a^2+b^2=c^2
Given N, Check if there exists any Pythagorean triplet for which a+b+c=N
Find maximum possible value of product of a,b,c among all such Pythagorean triplets, If there is no such Pythagorean triplet print -1."""
#!/bin/python3
import sys

product=-1
d=0
N = int(input())
for a in range(1,N//3):
    """Solving the two equations a**2+b**2=c**2 and a+b+c=N eliminating c """
    b=(N*N-2*a*N)//(2*N-2*a)
    c=N-a-b
    if c*c==(a*a+b*b):
        d=(a*b*c)
        if d>=product:
            product=d
print(product)
