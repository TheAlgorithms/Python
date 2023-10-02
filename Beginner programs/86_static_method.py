class Employee:
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

naksh = Employee()
naksh.greet()
naksh.salary = 10000
# if we remove self than it will convert into below line thrrow an error
naksh.getsalary("Thanks!")  # Employee.getsalary()
naksh.greet()  # Employee.greet()
# method for without self is known as static method
naksh.time()