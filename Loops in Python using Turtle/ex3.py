from turtle import *

speed('fastest')
bgcolor('black')
pencolor('yellow')
pensize(3)
for i in range(100, 0, -1): # reverse
    fd(i)
    lt(360/6)
    write(i)
    circle(i)

hideturtle()
mainloop()