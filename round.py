import turtle

print("1. Draw circle")
print("2. Draw Tangent Circles in Python Turtle")
print("3. Draw Spiral Circles in Python Turtle")
print("4. Draw Concentric Circles in Python Turtle")

num = int(input("Enter a number: "))

if num == 0:
    t = turtle.Turtle()
    t.circle(100)
    print(num)

elif num == 1:
    t = turtle.Turtle()
    for i in range(10):
        t.circle(10 * i)
    print(num)

elif num == 2:
    t = turtle.Turtle()
    for i in range(100):
        t.circle(10 + i, 45)
    print(num)

elif num == 3:
    t = turtle.Turtle()
    for i in range(50):
        t.circle(10 * i)
        t.up()
        t.sety((10 * i) * (-1))
        t.down()
    print(num)
