#Hiding the complexity and showing only the essential features of object
#A TV set where we enjoy programs with out knowing the inner details of how TV works.
#Abstract class can’t be instantiated so it is not possible to create objects of an abstract class
#Abstract class can have both concrete methods as well as abstract methods.
#Generally abstract methods defined in abstract class don’t have any body but it is possible to have abstract methods with implementation in abstract class. Any sub class deriving from such
# abstract class still needs to provide implementation for such abstract methods.
#If any abstract method is not implemented by the derived class Python throws an error.
#Since abstract class are supposed to have abstract methods having no body so abstract classes
# are not considered as complete concrete classes thus it is not possible to instantiate an abstract class
from abc import ABC, abstractmethod


class Parent(ABC):
    def common(self):
        print("I'm common")
    """@abstractmethod
    def vary(self):
        pass"""


class child1(Parent):
    def vary(self):
        print("Child1")


class child2(Parent):
    def vary(self):
        print("Child2")


ob = Parent()
obj = child1()
obj.common()
obj.vary()
