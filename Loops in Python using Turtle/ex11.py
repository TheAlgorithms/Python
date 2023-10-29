from turtle import *

speed('fastest')

move = 5
while True:
    for i in range(6):
        fd(100+move)
        rt(60)
        pencolor('yellow')
        begin_fill()
        for i in range(6):
            fd(50)
            rt(60)
        end_fill()
    pencolor('red')
    rt(60)
    move += 5

hideturtle()
mainloop()
