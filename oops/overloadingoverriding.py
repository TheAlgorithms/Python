#method overloading:
#more than one function of same class shares the same function name but different parameters
#python does not support method overloading.We can overload the methods but can only use the latest function
#example of compile time polymorphism
#_______________________OverLoading_________________#
from multipledispatch import dispatch


class function_overload:
    @dispatch(int, int)
    def add(self, a, b):
        return a+b

    @dispatch(int, int, int)
    def add(self, a, b, c):
        return a+b+c


obj = function_overload()
print(obj.add(10, 20))  # cause error without multipledispatch
print(obj.add(10, 20, 30))  # prints 60

#_____________________OverRiding_______________________#
#example of runtime polymorphism
#in method overriding the specific ipmlementation of method provided by the parent class is again altered by the child class
#Inheritance is always required in overriding as it is done between parent class and child class
#there is a need for two classes for overriding


class function_override():
    def function1(self):
        print("feature 1 of class A")

    def function2(self):
        print("feature 2 of class A")


class function_override_2(function_override):
    #function that is modifying existing function of class 1
    def function1(self):
        print("over written by class 2")


obj = function_override_2()
obj.function1()
