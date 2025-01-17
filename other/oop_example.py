# Class Creation
class Person:
    # Initialization function (when you create an object this named initialization)
    def __init__(self, name, age):
        # changing objects attributes to arguments that we enter when calling an class to create an object
        self.name = name
        self.age = age

    # String function that returns a string that will be returned if you will print class
    # Without __str__(): <__main__.Person object at 0x000001AC025E7230>
    # With __str__():
    def __str__(self):
        return f"Name: {self.name}. Age: {self.age}"


# Creating an object using class
p = Person("John", 21)
print(p)

# Output:
# Name: John. Age: 21
