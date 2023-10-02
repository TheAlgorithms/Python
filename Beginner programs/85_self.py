class Employee:
    company="Google"
    def getsalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

naksh=Employee()
naksh.salary=100000
# if we remove self than it will convert into below line thrrow an error
naksh.getsalary() # Employee.getsalary()