# Implementing Secant method in Python
# Author: dimgrichr


from math import cos, sin, exp
def f(x):
    return 8*x-2*exp(-x);


def SecantMethod(lowerBound, upperBound, repeats):
    x0 = lowerBound;
    x1 = upperBound;
    for i in range(0,repeats):
        x2 = x1 - (f(x1)*(x1-x0))/(f(x1)-f(x0));
        x0=x1;
        x1=x2;
    return x2;

print('The solution is: ' ,SecantMethod(1,3,2));
