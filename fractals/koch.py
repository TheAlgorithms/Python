
def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
      
        for angle in [60, -120, 60, 0]:
           koch(t, order-1, size/3)
           t.left(angle)
def snow(t,order,size):
    for i in range(3):
        koch(t,order,size)
        t.left(-120)
if __name__=='__main__':
    import turtle
    wn=turtle.Screen()
    nivi=turtle.Turtle()
    nivi.color('blue')
    #nivi.speed(10)
    nivi.hideturtle()
    wn.bgcolor('lightgreen')
    nivi.speed(0)
    nivi.penup()
    nivi.goto(-100,0)
    sz=240#change size 
    nivi.pendown()
    snow(nivi,4,sz)#change 2nd parameter to change order of fractal
