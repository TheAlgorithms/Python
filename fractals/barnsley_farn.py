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

import matplotlib.pyplot as plt
import numpy as np


def barnsley_fern(n_points: int = 100000) -> np.ndarray:
    """
    Generates the points of the Barnsley fern.

    Args:
        n_points (int): Number of points to generate.

    Returns:
        np.ndarray: An array of shape (n_points, 2) containing the x and y coordinates.
    """
    x, y = 0.0, 0.0
    points = np.zeros((n_points, 2), dtype=np.float64)

    rng = np.random.default_rng()

    for i in range(n_points):
        r = rng.random()
        if r < 0.01:
            x, y = 0.0, 0.16 * y
        elif r < 0.86:
            x_new = 0.85 * x + 0.04 * y
            y = -0.04 * x + 0.85 * y + 1.6
            x = x_new
        elif r < 0.93:
            x_new = 0.20 * x - 0.26 * y
            y = 0.23 * x + 0.22 * y + 1.6
            x = x_new
        else:
            x_new = -0.15 * x + 0.28 * y
            y = 0.26 * x + 0.24 * y + 0.44
            x = x_new
        points[i] = [x, y]

    return points


def plot_barnsley_fern(points: np.ndarray) -> None:
    """
    Plots the Barnsley fern using matplotlib.

    Args:
        points (np.ndarray): An array of shape (n_points, 2) containing coordinates.
    """
    x, y = points[:, 0], points[:, 1]
    plt.figure(figsize=(6, 10))
    plt.scatter(x, y, s=0.1, color="green", marker="o")
    plt.title("Barnsley Fern")
    plt.axis("off")  # Hide the axes for better visualization
    plt.show()


if __name__ == "__main__":
    fern_points = barnsley_fern()
    plot_barnsley_fern(fern_points)
