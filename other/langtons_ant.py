"""Langton´s ant

Requirements:
  - turtle

Usage:
  - $python3 langtons_ant

Langton´s ant rules:

Squares on a plane are colored variously either black or white. We arbitrarily identify one square as the "ant".
The ant can travel in any of the four cardinal directions at each step it takes. The "ant" moves according to these rules:
At a white square, turn 90° clockwise, flip the color of the square, move forward one unit
At a black square, turn 90° counter-clockwise, flip the color of the square, move forward one unit

See https://en.wikipedia.org/wiki/Langton%27s_ant and https://www.geeksforgeeks.org/python-langtons-ant/
 """
import turtle
from collections import defaultdict


def langtons_ant(max_steps=100000):
    grid_map = defaultdict(lambda: "white")
    window = turtle.Screen()
    window.bgcolor('white')
    window.screensize(1000, 1000)

    ant = turtle.Turtle()
    ant.shape('square')
    ant.shapesize(0.5)
    ant.speed(0)

    position = coordinate(ant)  # the position of our ant

    for _ in range(max_steps):
        if grid_map[position] == "white":
            ant.fillcolor("black")
            ant.right(90)
        elif grid_map[position] == "black":
            ant.fillcolor("white")
            ant.left(90)

        ant.stamp()
        grid_map[position] = "white" if [position] == "black" else "black"  # invert the color
        ant.forward(10)
        position = coordinate(ant)


def coordinate(ant):
    return round(ant.xcor()), round(ant.ycor())


if __name__ == "__main__":
    langtons_ant()
