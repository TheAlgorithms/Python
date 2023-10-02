class Employee:
    company="Google"
    salary=4000

raj=Employee()
naksh=Employee()
raj.salary=4000
naksh.salary=2800
print(raj.company)
print(naksh.company)
Employee.company="Youtube"
print(raj.company)
print(naksh.company)
print(raj.salary)
print(naksh.salary)