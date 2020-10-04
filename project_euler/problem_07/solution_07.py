"""Problem Statement
   By listing the first six prime numbers:
    2, 3, 5, 7, 11, and 13,
   we can see that the 1st prime is 2.
                       6th prime is 13.
   What is the nth prime number?
"""

from math import sqrt

def isprime(n):
    for i in range(2, int(sqrt(n))+2):
        if n%i==0:
            return False
    return True

def solution(n):
    a=1
    num=2
    while True:
        if isprime(num):
            a+=1
        if a==n:
            return num
        num+=1
        
if __name__ == "__main__":
    print(solution(int(input().strip())))
