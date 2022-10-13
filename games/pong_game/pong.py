"""
wikipedia - https://en.wikipedia.org/wiki/Pong

"""
import turtle

trtle = turtle.Screen()
trtle.title("My First game using turtle")
trtle.bgcolor("white")
trtle.setup(width=800, height=600)
trtle.tracer(0)  # stops the window from updating

score_a = 0
score_b = 0


# required for game: Paddle A and B, Ball
# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(1)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-370, 0)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(1)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+370, 0)

# Ball

b = turtle.Turtle()
b.speed(1)
b.shape("circle")
b.color("black")
b.penup()
b.goto(0, 0)
b.dx = 0.2
b.dy = 0.2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(
    rf"Player A : {score_a}  Player B : {score_b}",
    align="center",
    font=("Courier", 24, "normal"),
)


def paddle_a_up():
    y = paddle_a.ycor()  # y cordinate ... increases as we go up and vice versa
    y += 30
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 10
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 10
    paddle_b.sety(y)


trtle.listen()
trtle.onkeypress(paddle_a_up, "w")
trtle.onkeypress(paddle_a_down, "s")
trtle.onkeypress(paddle_b_up, "Up")
trtle.onkeypress(paddle_b_down, "Down")

while True:
    trtle.update()
    # Moving the ball
    b.setx(b.xcor() + b.dx)
    b.sety(b.ycor() + b.dy)
    if b.ycor() > 290:
        b.sety(290)
        b.dy *= -1
    if b.ycor() < -290:
        b.sety(-290)
        b.dy *= -1

    if b.xcor() > 390:
        b.goto(0, 0)
        b.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(
            rf"Player A : {score_a}  Player B : {score_b}",
            align="center",
            font=("Courier", 24, "normal"),
        )

    if b.xcor() < -390:
        b.goto(0, 0)
        b.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(
            rf"Player A : {score_a}  Player B : {score_b}",
            align="center",
            font=("Courier", 24, "normal"),
        )

    if (b.xcor() > 340 and b.xcor() < 350) and (
        b.ycor() < paddle_b.ycor() + 50 and b.ycor() > paddle_b.ycor() - 50
    ):
        b.setx(340)
        b.dx *= -1
    if (b.xcor() < -340 and b.xcor() > -350) and (
        b.ycor() < paddle_a.ycor() + 50 and b.ycor() > paddle_a.ycor() - 50
    ):
        b.setx(-340)
        b.dx *= -1
