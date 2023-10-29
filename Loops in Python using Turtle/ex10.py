from turtle import *

for i in range(6):
    if i == 4: break
    fd(150)
    rt(60)
else:
    penup()
    goto(75,-140)
    pendown()
    write("Hexagon", align='center')

hideturtle()
mainloop()