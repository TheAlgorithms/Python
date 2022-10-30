#Python Program to obtain x,y,z from the user and calculate the expression.
               #4x to the power of 4 + 3x to the power of 2 + 9z + 6 pi


x=int(input("Enter x="))
y=int(input("Enter y="))
z=int(input("Enter z="))
import math
a= (4*(x**4)+3*(y**3)+9*z+6*math.pi)
b= (4*(x**4)+3*(y**3)+9*z+6*(22/7))
print("with math",a)
print("without math",b)