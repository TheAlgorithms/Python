from math import *
def operation(a,b,o):
    if o == '+':
     a=10
     return a+b
    elif o == '-' and a>b:
        return a-b
    elif o == '-' and b>=a:
        return b-a
    elif o == '*':
        return a*b
    elif o == '%':
        if a>b:
            return a%b
        else:
            return b%a
    elif o == '/':
        if a>b:
            return a/b
        else:
            return b/a


x = input("Enter the number 1: ")
y = input("Enter the number 2: ")
z = input("Enter the operator: ")
result = operation(float(x),float(y),z)
print(result)