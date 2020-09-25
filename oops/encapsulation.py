#Idea of wrapping data and methods that work on data within one unit
#hiding the data
#you can Restrict access to methods and variables.
#This can prevent the data from being modified by accident
#Encapsulation prevents from accessing accidentally, but not intentionally
#A private variable can only be changed within a class method and not outside of the class(prefixes using double underscore)
#every variable by default is a public variable,accessed and modifies anywhere
#protected(single underScore) can be accessed in subclass unlike privates cannot be accessed outside class


class Car:

    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
        print("Constructor created")

    def __del__(self):
        #@abstractmethod
        print("Constructor destroyed")

    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))

    def setMaxspeed(self, speed):
        self.__maxspeed = speed


redcar = Car()
redcar.drive()
redcar.setMaxspeed(10)  # will not change variable because its private
redcar.drive()
print(redcar._Car__maxspeed)
del redcar  # kind of garbage collector(destructor) that deletes reference
