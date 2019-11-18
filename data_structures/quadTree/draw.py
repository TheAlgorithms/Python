import turtle

win = turtle.Screen()
win.title("Quad Trees")
head = turtle.Turtle()
head.hideturtle()
head.speed(0)

class Rect():

    def __init__(self, center, height, width):
        self.center = center
        self.height = height
        self.width = width

    def draw(self):
        head.setheading(0)
        head.penup()
        head.goto(self.center[0] - self.width, self.center[1] + self.height)
        head.pendown()
        head.forward(2*self.width)
        head.right(90)
        head.forward(2*self.height)
        head.right(90)
        head.forward(2*self.width)
        head.right(90)
        head.forward(2*self.height)

    def drawDivision(self):
        head.setheading(0)
        head.penup()
        head.goto(self.center[0] - self.width, self.center[1])
        head.pendown()
        head.forward(2*self.width)
        head.penup()
        head.goto(self.center[0], self.center[1] + self.height)
        head.right(90)
        head.pendown()
        head.forward(2*self.height)

def plot(point):
    head.penup()
    head.goto(point)
    head.pendown()
    head.dot()