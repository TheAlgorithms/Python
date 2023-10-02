class Person:
    country="India"

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company="Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takebreath(self):
        print("I am an Employee so I am luckily breathing....")


class Programmer(Employee):
    company="Fiverr"

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreath(self):
        print("I am an Programmer so I am breathing++...")  

    
p=Person()
p.takeBreath()
# print(p.company) #throws an error

e=Employee()
e.takebreath()
print(e.company)

pr=Programmer()
pr.takebreath()
print(pr.company)
print(pr.country)