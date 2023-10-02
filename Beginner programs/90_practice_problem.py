''' if we set an instance attribute then it would change the class atrribute
'''
class Sample:
    a="Yash"    # class attribute 

obj=Sample()
obj.a="Naksh" #instance attribute
# Sample.a="Naksh" it will change the class attribute
print(Sample.a)
print(obj.a)