class Employee:
    company="Google"

    def showdetails(self):
        print("This is an employee")

class Programmer(Employee):
    language="Python"

    def getLanguage(self):
        print(f"The language is {self.language}")
    def showdetails(self):
        print("This is an Programmer")


e=Employee()
e.showdetails()
p=Programmer()
p.showdetails()
print(p.company)