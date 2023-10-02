class Number:
    def __init__(self,num):
        self.num=num

    def __add__(self,num2): # add and mul is given method in python module for you can refer on google
        print("Let's add")
        return self.num+num2.num

    def __mul__(self,num2):
        print("Let's multiply")
        return self.num*num2.num


n1=Number(4)
n2=Number(6)
sum=n1+n2
mul=n1*n2
print(sum)
print(mul)