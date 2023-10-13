# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle

pen = turtle.Turtle()
pen.speed(0)
# it will make a 3D look like circle
pen.fillcolor("white")
pen.begin_fill()

# Radius of circle
pen.circle(100)
pen.end_fill()
pen.hideturtle()

# for the colour of rainbow
colors = ["red", "purple", "blue", "green", "orange", "yellow"]
# to generate the benzene
t = turtle.Pen()
t.screen.bgcolor("black")
for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x // 100 + 1)
    t.forward(x)
    t.left(59)
