import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline

# Define control points (x, y)
control_points = np.array([[1, 2], [2, 3], [3, 5], [4, 4], [5, 2]])

# Create B-spline object with degree=3 (cubic B-spline)
degree = 3
t = range(len(control_points) + degree + 1)
spl = BSpline(t, control_points, degree)

# Evaluate the B-spline curve
num_points = 1000
curve_points = np.array([spl(i) for i in np.linspace(0, len(control_points) - degree, num_points)])

# Plot control points and B-spline curve
plt.plot(control_points[:, 0], control_points[:, 1], 'ro-', label='Control Points')
plt.plot(curve_points[:, 0], curve_points[:, 1], 'b-', label='B-spline Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('B-spline Curve')
plt.grid(True)
plt.show()
