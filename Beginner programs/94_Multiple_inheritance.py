class Employee:
    company="Visa"
    ecode=120

class Freelancer:
    company="Fiverr"
    level=0

    def upgradeLevel(self):
        self.level=self.level+1

class Programmer(Employee,Freelancer):
    name="Naksh"

p=Programmer()
p.upgradeLevel()    
print(p.level)