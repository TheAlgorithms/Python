#code redundancy
#code reusability
#Parent class or subclass
#One way that oops achieves code redundancy and reusability is through Inheritance
#Multiple inheritance is when when a class inherits attributes and methods from more than one parent class


class Fish:
    def __init__(self, firstname, lastname="fish", skeleton="bone", eyelids="false"):
        self.firstname = firstname
        self.lastname = lastname
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print("Fish can swim")

    def swimBackwards(self):
        print("Fish can swim backwards")

#Child class or SubClass..>>Classes that make use of all variables and all methods of parent class


class trout(Fish):
    #if we dont want to define any other methods for child class just pass it
    def __init__(self, water="freshWater"):
        self.water = water
        super().__init__(self)

    def trFun(self):
        print("this is trout func")
        print(self.firstname)


class clownfish(Fish):
    def clFun(self):
        print("this is clownfish func")


class example(Fish):
    pass


class Shark(Fish):
    def __init__(self, firstname, lastname="shark", skeleton="cartilage", eyelids="true"):
        self.firstname = firstname
        self.lastname = lastname
        self.eyelids = eyelids
        self.skeleton = skeleton

    def swimBackwards(self):
        print("The shark can only shink backwards but not swim")


class Coral:
    def community(self):
        print("Coral lives in community")


class Anemoe:
    def anfunc(self):
        print("I'm a anemoe function")


class multiinheritance(Coral, Anemoe):
    pass


if __name__ == "__main__":
    multi = multiinheritance()
    parent = Fish("Whats")
    terry = trout()
    cl = clownfish("Cfish")
    ex = example("exfish")
    sammy = Shark("Sammy")
    #print("{}".format(terry.firstname))
    print(terry.lastname)
    terry.swim()
    cl.swim()
    ex.swimBackwards()
    print(sammy.lastname, sammy.eyelids)
    terry.firstname = "Terry"
    print(terry.water, terry.lastname)
    terry.trFun()
    multi.community()
    multi.anfunc()

    #cannot access childs methods using parents object
    #parent.trFun() ...>>Error
