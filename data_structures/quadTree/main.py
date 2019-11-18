from quadTree import quadTree
from draw import Rect, win, head, plot
import random
import turtle

def clicked(x, y):
    qt.insertDraw([x, y])
    if qt.contains([x, y]) : plot([x, y])
    print("You clicked : ", x, ", ", y)

boundary = Rect([0, 0], 250, 250)
boundary.draw()
qt = quadTree(boundary, 4)

for _ in [0]*600:
    rand_x = random.uniform(-250, 251)
    rand_y = random.uniform(-250, 251)
    qt.insertDraw([rand_x, rand_y])
    plot([rand_x, rand_y])

win.onclick(clicked)

qt.draw()
win.mainloop()
#win.exitonclick()