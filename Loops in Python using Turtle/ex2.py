from turtle import *

speed('fastest')
bgcolor('black')
pencolor('yellow')
pensize(3)
for i in range(1, 500, 5):
    fd(i)
    lt(360/6)
    write(i)

hideturtle()
mainloop()