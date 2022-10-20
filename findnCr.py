# Python3 implementation to find nCr
 
from math import *
 
# Function to find the nCr
 
 
def printNcR(n, r):
 
    # p holds the value of n*(n-1)*(n-2)...,
    # k holds the value of r*(r-1)...
    p = 1
    k = 1
 
    # C(n, r) == C(n, n-r),
    # choosing the smaller value
    if (n - r < r):
        r = n - r
 
    if (r != 0):
        while (r):
            p *= n
            k *= r
 
            # gcd of p, k
            m = gcd(p, k)
 
            # dividing by gcd, to simplify product
            # division by their gcd saves from
            # the overflow
            p //= m
            k //= m
 
            n -= 1
            r -= 1
 
        # k should be simplified to 1
        # as C(n, r) is a natural number
        # (denominator should be 1 )
 
    else:
        p = 1
 
    # if our approach is correct p = ans and k =1
    print(p)
 
 
# Driver code
if __name__ == "__main__":
    n = 50
    r = 25
 
    printNcR(n, r)
 
