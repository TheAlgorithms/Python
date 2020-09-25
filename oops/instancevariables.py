#Instance variables cannot be accessed by using class name....only by using objects
#Instance variables are only restricted to objects
#Class variables can be accessed by both class and objects
#whenever an object calls its method, the object itself is passed as the first argument. So, ob.func() translates into MyClass.func(ob)
#but its not the same case with classes calling functions
class example:
    classatrribute="Wh"
    
    def __init__(self,name,age,exvariable):    #instance variables
        self.name=name
        self.age=age
        self.exvariable=exvariable
        self.ex2variable=None
    def basic(self):
        return ("He")

class exampe2:
    def exr(self):
        #accessing class variables of other class just by using classname.variable name
        print("{}".format(example.classatrribute))
        #accessing instance variable of other class by passing object of that class as a reference 
        print(self.name)
        print(example.classatrribute)
        #print(self.age)

    
ex=example("ram","19","20")
ex.ex2variable=45
#print(ex.ex2variable)
#print(ex.classatrribute)
#print(example.classatrribute)
#print(example.name)        #error since accessing instance variable with class name
#print("{} says {}".format(ex.name,ex.__class__.classatrribute))
print(ex.basic())     #...>> translates internally  into example.basic(ex)
print(example.basic(example))
ob2=exampe2()
#To access instance variables of other class call method using class name and pass the object of previous class as reference
exampe2.exr(ex)           
#ob2.exr()   ....>> this is used just to access the instance variables of that class 

