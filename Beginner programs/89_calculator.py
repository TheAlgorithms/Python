class Calculator:
    def __init__(self,num):
        self.number=num
    def square(self):
        print(f"the value of {self.number} square is {self.number **2}")
    def squareroot(self):
        print(f"the value of {self.number} squareroot is {self.number **0.5}")

    def cube(self):
        print(f"the value of {self.number} cube is {self.number **3}")

    @staticmethod
    def greet():
        print("***** Hello welcome to the best calculator of the world *****")



a=Calculator(4)
a.greet()
a.square()
a.squareroot()
a.cube()
