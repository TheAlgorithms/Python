"""
Lorenz Attractor

The Lorenz attractor is a set of chaotic solutions to the Lorenz system,
which are differential equations originally designed to model atmospheric
convection. It exhibits chaotic behavior and is sensitive to initial conditions.

References:
https://en.wikipedia.org/wiki/Lorenz_system

Requirements:
    - matplotlib
    - numpy
"""

import matplotlib.pyplot as plt
import numpy as np


def lorenz(x, y, z, s=10, r=28, b=2.667):
    """
    Calculate the next step of the Lorenz system.
    """
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return x_dot, y_dot, z_dot


def generate_lorenz_attractor(
    num_steps=10000, dt=0.01, initial_values=(0.0, 1.0, 1.05)
):
    """
    Generates the points for the Lorenz attractor based on initial conditions.

    >>> len(generate_lorenz_attractor(1000, 0.01))
    1000
    """
    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)

    xs[0], ys[0], zs[0] = initial_values

    for i in range(num_steps):
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)

    return xs, ys, zs


def plot_lorenz(xs, ys, zs):
    """
    Plot the Lorenz attractor using matplotlib in 3D space.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(xs, ys, zs, lw=0.5)
    ax.set_title("Lorenz Attractor")
    plt.show()


if __name__ == "__main__":
    xs, ys, zs = generate_lorenz_attractor()
    plot_lorenz(xs, ys, zs)
