'''
Problem:
The sum of the squares of the first ten natural numbers is,
            1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
            (1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first N natural numbers and the square of the sum.
'''
from __future__ import print_function
import math
def problem6(number=100):
    sum_of_squares = sum([i*i for i in range(1,number+1)])
    square_of_sum = int(math.pow(sum(range(1,number+1)),2))
    return square_of_sum - sum_of_squares
def main():
    print(problem6())

if __name__ == '__main__':
    main()