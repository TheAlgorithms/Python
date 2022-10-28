'''
Bohr's model consists of a small nucleus (positively charged) surrounded by negative electrons moving around the nucleus in orbits.
Bohr found that an electron located away from the nucleus has more energy, and the electron which is closer to nucleus has less energy.
Postulates of Bohr's Model of an Atom:
>In an atom, electrons (negatively charged) revolve around the positively charged nucleus in a definite circular path called orbits or shells.
>Each orbit or shell has a fixed energy and these circular orbits are known as orbital shells.

'''


import turtle


def pen_jump(pen, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


def turtle_setup(width=1000, height=1000):
    turtle.Screen()
    turtle.setup(width, height)
    turtle.clearscreen()
    turtle.title("Bohr (circle) atom")


def turtle_pen(shape="circle", speed=10, size=3, colors=("blue", "green")):
    pen = turtle.Turtle()
    pen.shape(shape)
    pen.speed(speed)
    pen.pensize(size)
    pen.color(*colors)
    pen_jump(pen, 0, 0)
    pen.stamp()
    return pen


def turtle_stop(pen):
    pen.hideturtle()
    turtle.exitonclick()


def draw_atom(pen, radius, levels, electrons_per_level, electron_size=15, electron_color="red"):
    full_circle = 360
    for level in range(levels):
        r = radius * (level + 1)                           # concentric circles
        electrons_in_level = electrons_per_level[level]
        arcs = full_circle / electrons_in_level            # arcs between each electron
        circumference = 0
        pen_jump(pen, 0, -r)                               # centering
        while circumference < full_circle:
            pen.dot(electron_size, electron_color)
            pen.circle(r, arcs)
            circumference = circumference + arcs


if __name__ == '__main__':
    electrons_per_level = []
    levels = eval(input('How many levels? '))
    first_level_radius = 45

    for i in range(levels):
        e = eval(input(f'Electrons in level {str(i + 1)}: '))
        electrons_per_level.append(e)

    print(electrons_per_level)

    turtle_setup()
    pen = turtle_pen()
    draw_atom(pen, first_level_radius, levels, electrons_per_level)
    turtle_stop(pen)