class Employee:
    company="Bharat gas"
    salary=5500
    salarybonus=500

    @property
    def totalSalary(self):
        return self.salary+self.salarybonus

    @totalSalary.setter # it is a property for change a value
    def totalSalary(self,val):
        self.salarybonus=val-self.salary

e=Employee()
print(e.totalSalary)
e.totalSalary=5800
print(e.salary)
print(e.salarybonus)