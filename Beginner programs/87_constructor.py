class Employee:

    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee is created")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

    company = "Google"
    '''def getsalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")'''

    def getsalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod  # BY this we run greet function without self because it is mark as static
    def greet():
        print("Good Morning,Sir")

    @staticmethod
    def time():
        print("the time is 9 am in the morning")

naksh=Employee("Naksh",10000,"Open Source")
naksh.getDetails()