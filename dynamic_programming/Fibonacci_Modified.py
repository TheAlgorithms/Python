"""
https://www.hackerrank.com/challenges/fibonacci-modified/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

def fibonacciModified(t1, t2, n):
    if (n<3):
        if(n==1):
            return t1
        else:
            return t2

    else:
        c = t1 + t2*t2
        n = n - 2
        while (n>0):
            t1 = t2
            t2 = c
            c = t1 + t2*t2
            n = n - 1
        return t2
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1T2n = input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
