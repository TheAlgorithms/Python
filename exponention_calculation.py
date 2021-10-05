#!/usr/bin/env python3
#https://cp-algorithms.com/algebra/binary-exp.html
def exponention_calculation(a:int,n:int)-> int:
    """
    calculate a raised to power n (a^n):
    >>>exponention_calculation(2,3)
    8
    >>>exponention_calculation(-5,2)
    25
    >>>exponention_calculation(5,2)
    25
    >>>exponention_calculation(2,-1)
    0.5
    >>>exponention_calculation(3,2)
    9
    
    
    """
    ans1=0
    if n<0:
        ans1=n
        n=-1*n
    ans = 1
    while (n > 0):
        last_bit = (n & 1)
        if (last_bit):
            ans = ans * a
        a = a * a
        n = n >> 1
    if ans1!=0:
        return 1/ans
    return ans
