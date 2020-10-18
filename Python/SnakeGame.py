import turtle

import time

import random

delay = 0.1



segments=[]



wn = turtle.Screen()

wn.bgcolor("black")

wn.title("SNAKE GAME")

wn.setup(width=600, height=600)

wn.tracer(0)



i=0

h=0

pen = turtle.Turtle()

pen.speed(0)

pen.color("white")

pen.shape("square")

pen.penup()

pen.hideturtle()

pen.goto(0,260)

pen.write("Score : 0 Highscore: 0",align="center",font=("Courier",24,"normal"))



head = turtle.Turtle()

head.speed(0)

head.color("Green")

head.shape("square")

head.penup()

head.goto(0,0)

head.direction = "stop"

m=90

n=90

p=0

breakers = []

for i in range(5):

    breaker = turtle.Turtle()

    breaker.speed(0)

    breaker.shape("square")

    breaker.color("purple")

    breaker.penup()

    breaker.goto(m+p,n)

    breaker.direction = "stop"

    breakers.append(breaker)

    p+=20

m=-100

n=-90

p=0

for i in range(5):

    breaker2 = turtle.Turtle()

    breaker2.speed(0)

    breaker2.shape("square")

    breaker2.color("purple")

    breaker2.penup()

    breaker2.goto(m,n+p)

    breaker2.direction = "stop"

    breakers.append(breaker2)

    p+=20



m=-200

n=90

p=0



for i in range(5):

    breaker3 = turtle.Turtle()

    breaker3.speed(0)

    breaker3.shape("square")

    breaker3.color("purple")

    breaker3.penup()

    breaker3.goto(m+p,n)

    breaker3.direction = "stop"

    breakers.append(breaker3)

    p+=20





food = turtle.Turtle()

food.speed(0)

food.color("red")

food.shape("circle")

food.penup()

food.goto(0,100)



def go_up():

    if head.direction != "down":



        head.direction = "up"



def go_down():

    if head.direction != "up":

        head.direction = "down"



def go_left():

    if head.direction != "right":

        head.direction = "left"



def go_right():

    if head.direction != "left":

        head.direction = "right"





def move():

    if head.direction == "up":

        y = head.ycor()

        head.sety(y + 20)

    if head.direction == "down":

        y = head.ycor()

        head.sety(y - 20)

    if head.direction == "left":

        x = head.xcor()

        head.setx(x - 20)

    if head.direction == "right":

        x = head.xcor()

        head.setx(x + 20)





wn.listen()

wn.onkeypress(go_up, "8")

wn.onkeypress(go_down, "2")

wn.onkeypress(go_right, "6")

wn.onkeypress(go_left, "4")



while True:



    wn.update()

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:

        time.sleep(1)

        head.goto(0,0)

        head.direction="stop"

        for segment in segments:

            segment.goto(1000,1000)

        segments.clear()

        time.sleep(0.2)

        i=0

        pen.clear()



    for b in breakers:

        if b.distance(head) < 20:

            time.sleep(1)

            head.goto(0, 0)

            head.direction = "stop"

            i = 0

            pen.clear()



    for segment in segments:

        if segment.distance(head) < 20:

            time.sleep(0.001)



            head.goto(0,0)

            head.direction="stop"

            for segment in segments:

                segment.goto(1000, 1000)

            segments.clear()

            time.sleep(0.2)

            i = 0

            pen.clear()

            

            

    if head.distance(food) < 20:

        x = random.randint(-290,290)

        y = random.randint(-290, 290)

        food.goto(x,y)

        for b in breakers:

            if food.distance(b) < 20:

                food.goto(random.randint(-290,290),random.randint(-290,290))





        child = turtle.Turtle()

        child.speed(0)

        child.shape("square")

        child.color("grey")

        child.penup()

        segments.append(child)



        i+=10

        if i>h:

            h=i

        pen.clear()

        pen.write("Score: {} Highscore: {}".format(i,h),align="center",font=("Courier",24,"normal"))

    for index in range(len(segments)-1,0,-1):

        x = segments[index-1].xcor()

        y = segments[index - 1].ycor()

        segments[index].goto(x,y)



    if(len(segments) > 0):

        x = head.xcor()

        y = head.ycor()

        segments[0].goto(x,y)



    move()



    time.sleep(delay)



wn.mainloop()
