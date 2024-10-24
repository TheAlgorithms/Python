"""
Barnsley Fern

The Barnsley fern is a fractal that uses an iterated function system (IFS) 
to generate a realistic-looking fern shape.

Reference:
https://en.wikipedia.org/wiki/Barnsley_fern

Requirements:
    - matplotlib
    - numpy
"""

import numpy as np
import matplotlib.pyplot as plt


def barnsley_farn(n_points=100000):
    """
    Generates the points of the Barnsley fern.
    """
    x, y = 0, 0
    points = np.zeros((n_points, 2))

    for i in range(n_points):
        r = np.random.random()
        if r < 0.01:
            x, y = 0, 0.16 * y
        elif r < 0.86:
            x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
        elif r < 0.93:
            x, y = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        else:
            x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44
        points[i] = [x, y]

    return points


def plot_barnsley_farn(points):
    """
    Plots the Barnsley fern using matplotlib.
    """
    x, y = points[:, 0], points[:, 1]
    plt.scatter(x, y, s=0.1, color='green')
    plt.title("Barnsley Fern")
    plt.show()


if __name__ == "__main__":
    fern_points = barnsley_farn()
    plot_barnsley_farn(fern_points)
