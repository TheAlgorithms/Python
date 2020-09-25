#Polymorphism in inheritance lets us define methods in the child class that have the same name as the methods in the parent class
#Polymorphism means having many forms.
#Same function name(different parameters)being used for different implementations


class Bird:
    def intro(self):
        print("There are many type of birds")

    def fly(self):
        print("Many birds fly but some cannot")


class sparrow(Bird):
    def fly(self):
        print("Sparrows can fly")


class ostritch(Bird):
    def fly(self):
        print("Ostritches cannot fly")


if __name__ == "__main__":
    obbird = Bird()
    obsparrow = sparrow()
    obsotritch = ostritch()
    for bird in (obsparrow, obsotritch):
        bird.intro()
        bird.fly()
        print()
