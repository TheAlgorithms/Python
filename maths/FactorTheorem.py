from math import sqrt  # Math.sqrt is used for iterative factoring
from fractions import Fraction  # Python Fraction module is very helpful in dealing with floating numbers

"""
Factoring complex integer polynomials
As long as the first coefficient and constant are integers, the program will work 
Finds factors in O(sqrt(a)*sqrt(c)*n)
Where a is the first coefficient, c is the constant, and n is the degree of the function
Note: This program will only find linear factors in the form ax + b
https://en.wikipedia.org/wiki/Factor_theorem 
"""


def factor(num):
    """
    Returns an array of all factors of a number
    >>> factor(2)
    [1, 2]
    >>> factor(3)
    [1, 3]
    >>> factor(6)
    [1, 2, 3, 6]
    """

    factors = []
    for x in range(1, int(sqrt(num))+1):  # Iterate to the square root of (num)
        # If x is a factor, append x and (if x != num/x) append num/x
        if num % x == 0:
            factors.append(int(x))
            if num/x != x:
                factors.append(int(num/x))
    return factors


class Number:
    """ This class is used to hold information about elements in the polynomial """
    def __init__(self, degree, number):
        self.degree = degree
        self.number = number


def main():
    """ Factors polynomial based on user input """
    possibleFactors = []
    polynomial = []
    answers = []

    print("Input the degree of the function")
    degree = int(input().strip())

    print("Coefficient from least to greatest degree; constant first")
    print("If a value of x^y does not exist, input zero")

    for i in range(degree+1):
        polynomial.append(Number(i, float(input().strip())))  # Construct polynomial - i refers to degree

    # First coefficient and constant
    q = factor(abs(polynomial[-1].number))
    p = factor(abs(polynomial[0].number))

    # Append all combinations of p/q
    for j in p:
        for k in q:
            possibleFactors.append(Fraction(j, k))
            possibleFactors.append(Fraction(-j, k))

    possibleFactors = set(possibleFactors)  # Remove duplicates

    # Solve for each possible factor
    for x in possibleFactors:
        total = Fraction(0, 1)
        for var in polynomial:
            # For each element in polynomial, plug x
            temp = Fraction(var.number)  # Important to convert floating point into fraction
            total += (x**var.degree)*temp
        if total == 0:
            answers.append(x)

    print("Factors ->")
    for x in answers:
        print(x, end=' ')


if __name__ == "__main__":
    main()

