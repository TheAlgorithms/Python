# Implementing Newton Raphson method in Python
# Author: Syed Haseeb Shah (github.com/QuantumNovice)
# The Newton-Raphson method (also known as Newton's method) is a way to
# quickly find a good approximation for the root of a real-valued function
from sympy import diff
from decimal import Decimal
from math import sin,cos,tan,log,exp


PRECISION = 10 ** -10


def NewtonRaphson(func, a):
    """ Finds root from the point 'a' onwards by Newton-Raphson method """
    x = a
    while True:

        x = Decimal(x) - (Decimal(eval(func)) / Decimal(eval(str(diff(func)))))

        # This number dictates the accuracy of the answer
        if abs(eval(func)) < PRECISION:
            return x


# Let's Execute
if __name__ == "__main__":
    # Find root of trigonometric function
    # Find value of pi
    print("The root of sin(x) = 0 is ", NewtonRaphson("sin(x)", 2))

    # Find root of polynomial
    print("The root of x**2 - 5*x +2 = 0 is ", NewtonRaphson("x**2 - 5*x +2", 0.4))

    # Find Square Root of 5
    print("The root of log(x) - 1 = 0 is ", NewtonRaphson("log(x)- 1", 2))

    # Exponential Roots
    print("The root of exp(x) - 1 = 0 is", NewtonRaphson("exp(x) - 1", 0))
