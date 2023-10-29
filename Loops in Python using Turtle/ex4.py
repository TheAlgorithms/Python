from turtle import *

speed('slowest')
data = [12,55,10,25,62,66,10,96,120,252,55]  # list

for val in data:
    fd(val)
    lt(360/6)
    circle(val, 180)

hideturtle()
mainloop()  
