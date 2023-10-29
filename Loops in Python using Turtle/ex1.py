from turtle import *    
# Make a square
speed('fastest')
penup()
goto(-200,-200)
pendown()
for i in range(15):
    fd(20)
    lt(90)
    fd(20)
    rt(90)
hideturtle()
mainloop()