class Employee:
    company="camel"
    salary=100      
    location="Delhi"

    def changeSalary(self,sal):     # it doesn't change the salary attribute it will create a new attribute  
        self.salary=sal         # for changing this value we have to write this self.__class__.salary=sal or crate given below function

        '''
        @classmethod
        def changeSalary(cls,sal):     
        cls.salary=sal 
        '''

e=Employee()
print(e.salary)
e.changeSalary(500)
print(e.salary)
print(Employee.salary)