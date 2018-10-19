'''
Problem:
The prime factors of 13195 are 5,7,13 and 29. What is the largest prime factor of a given number N?
e.g. for 10, largest prime factor = 5. For 17, largest prime factor = 17.
'''
from __future__ import print_function, division

import math

def isprime(no):
    if(no==2):
        return True
    elif (no%2==0):
        return False
    sq = int(math.sqrt(no))+1
    for i in range(3,sq,2):
        if(no%i==0):
            return False
    return True

maxNumber = 0
n=int(input())
if(isprime(n)):
    print(n)
else:
    while (n%2==0):
        n=n/2
    if(isprime(n)):
        print(n)
    else:
        n1 = int(math.sqrt(n))+1
        for i in range(3,n1,2):
            if(n%i==0):
                if(isprime(n/i)):
                    maxNumber = n/i
                    break
                elif(isprime(i)):
                    maxNumber = i
        print(maxNumber)
