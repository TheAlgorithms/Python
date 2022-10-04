import matplotlib.pyplot as p
import numpy as np

a = p.axes()
a.spines["bottom"].set_color("red")
a.spines["left"].set_color("yellow")
x_coordinates = np.array([0, 1, 2, 3, 5])
y_coordinates = np.array([0, 4, 6, 8, 5])
p.scatter(x_coordinates, y_coordinates)
p.ylabel("Y-axis")
p.xlabel("X-axis")
p.savefig(r"D:\pycharm/technology.svg", dpi=350)
p.show()
