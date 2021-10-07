from math import sqrt
from fractions import Fraction
# Factoring complex integer polynomials
# As long as the first coefficient and constant are integers, the program will work
# Finds factors in O(sqrt(a)*sqrt(c)*n)
# Where a is the first coefficient, c is the constant, and n is the degree of the function
# Note: This program will only find linear factors in the form ax + b
# https://en.wikipedia.org/wiki/Factor_theorem


# Simple iterative factoring
def factor(num):
    factors = []
    for x in range(1, int(sqrt(num))+1):
        if num % x == 0:
            factors.append(int(x))
            if num/x != x:
                factors.append(int(num/x))
    return factors


class Number:
    def __init__(self, degree, number):
        self.degree = degree
        self.number = number


def main():
    f = []
    poly = []
    ans = []

    print("Input the degree of the function")
    n = int(input().strip())

    print("Coefficient from least to greatest degree; constant first\nIf a value of x^y does not exist, input zero")

    for i in range(n+1):
        poly.append(Number(i, float(input().strip())))

    # First coefficient and constant
    q = factor(abs(poly[-1].number))
    p = factor(abs(poly[0].number))

    # Append all combinations
    for j in p:
        for k in q:
            f.append(Fraction(j, k))
            f.append(Fraction(-j, k))

    f = set(f)

    # Solve for each possible factor
    for item in f:
        total = Fraction(0, 1)
        for var in poly:
            temp = Fraction(var.number)  # Important to convert floating point into fraction
            total += (item**var.degree)*temp
        if total == 0:
            ans.append(item)

    print("Factors ->")
    for o in ans:
        print(o, end=' ')


# main()

