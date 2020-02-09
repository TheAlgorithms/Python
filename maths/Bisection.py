'''Given a function f(x) on floating number x and two numbers ‘a’ and ‘b’ 
such that f(a)*f(b) < 0 and f(x) is continuous in [a, b]. Here f(x) represents algebraic or transcendental equation. 
Find root of function in interval [a, b] (Or find a value of x such that f(x) is 0)
'''


import math

def equation(x):
    return math.cos(x) + x

def bisection(a, b):
    #Bolzano theory in order to find if there is a root between a and b
    if equation(a) * equation(b) >= 0:
        print("There is not a root between a and b\n")
        return

    half = a
    while ((b - a) >= 0.01):

        # Find middle point
        c = (a + b) / 2

        # Check if middle point is root
        if equation(c) == 0.0:
            break

        # Decide the side to repeat the steps
        if equation(c) * equation(a) < 0:
            b = c
        else:
            a = c

    print("The value of root is : ", "%.4f" % c)

#Testing
print("Testing for a = -3 and b = 2")
a = -3
b = 2
bisection(a, b)

a = 1
b = 3
print("\nTesting for a = 1 and b = 3")
bisection(a, b)

print("\nTesting for a = -5 and b = 0")
a = -5
b=0
bisection(a,b)
