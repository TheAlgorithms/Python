class Person:
    country="India"

    def __init__(self):
        print("Initializing Person....\n")

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company="Honda"

    def __init__(self):
        super().__init__()
        print("Intializing Employee...\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takebreath(self):
        super().takebreath()
        print("I am an Employee so I am luckily breathing....")


class Programmer(Employee):
    company="Fiverr"

    def __init__(self):
        print("Intializing Programmer...\n")

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Programmer so I am breathing++...")  

    
'''p=Person()
p.takeBreath()

e=Employee()
e.takebreath()

pr=Programmer()
pr.takebreath()'''
p=Person()
e=Employee()
pr=Programmer()
