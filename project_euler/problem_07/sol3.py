'''
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the Nth prime number?
'''
from __future__ import print_function
# from Python.Math import PrimeCheck
import math
import itertools
def primeCheck(number):
    if number % 2 == 0 and number > 2:
        return False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2))

def prime_generator():
    num = 2
    while True:
        if primeCheck(num):
            yield num
        num+=1

def main():
    n = int(input('Enter The N\'th Prime Number You Want To Get: '))  # Ask For The N'th Prime Number Wanted
    print(next(itertools.islice(prime_generator(),n-1,n)))


if __name__ == '__main__':
    main()