"""A positive integer is called square root smooth if all of its prime factors are strictly less than its square root.
Including the number 1, there are 29 square root smooth numbers not exceeding 100.

How many square root smooth numbers are there not exceeding 10000000000?
"""

import math
import sympy
def divisible(number):
    LIMIT = (int)(math.sqrt(number))
    return [i for i in range(2, LIMIT + 1) if (number % i == 0)]

def factors(number):
    return [i for i in range(number) if max(divisible(number)) < int(math.sqrt(number))]

def squareRootSmooth(number):
    return [i for i in range(number) if sympy.isprime(i)]

def noOfSquareRootSmooth(number):
    count = 0
    for i in range(1, number):
        if(squareRootSmooth(i)):
            count = count + 1
    return count
print(factors(100))
print(noOfSquareRootSmooth(100))

