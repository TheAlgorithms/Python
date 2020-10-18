"""Generally in Object oriented programming like python, 
we have different concepts that are often applied to different algorithms
like Classes, Methods, Variables, etc.

We also need to implement a few or more lines of code multiple times.
Therefore, we use reusability concepts like Inheritance and Polymorphism.

Method Overloading is a part of polymorphism.

Normally we do not have multiple methods in same class with same names.
Sometimes that might be the case and hence,
the method overloading concept comes into action.

In Method overloading, one can implement multiple methods with similar names 
within a single class, 
BUT with different arguments in those methods."""

#In the below example, we'll try overloading the area of shapes method

class Compute:

    def area(self, x = None, y = None): #Creating a method named area
        if x != None and y != None:
            return x * y
        elif x != None:
            return x * x
        else:
            return 0

obj = Compute() #Creating the object of the class

print("Area Value:", obj.area()) 
#Passing no argument and hence it'll return 0 as output

print("Area Value:", obj.area(4)) 
"""Passing 1 argument and hence it'll return the square of passed argument, 
thinking the argument to be the dimension of a square"""

print("Area Value:", obj.area(3, 5)) 
"""Passing 2 arguments and hence it'll return the product of passed
arguments, thinking the arguments to be the dimensions of a rectangle"""