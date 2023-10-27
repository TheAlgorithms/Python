import matplotlib.pyplot as plt
from typing import list, tuple


def digital_differential_analyzer_line(
    x1: int, y1: int, x2: int, y2: int
) -> tuple[list[int], list[int]]:
    """
    Draw a line using the Digital Differential Analyzer (DDA) algorithm.

    Parameters:
        x1 (int): The x-coordinate of the starting point.
        y1 (int): The y-coordinate of the starting point.
        x2 (int): The x-coordinate of the ending point.
        y2 (int): The y-coordinate of the ending point.

    Returns:
        tuple of two lists, where the first list contains the x-coordinates of the line points,
        and the second list contains the y-coordinates.

    Example:
        >>> digital_differential_analyzer_line(0, 0, 3, 2)
        ([0, 1, 2, 3], [0, 1, 1, 2])
    """

    # Calculate the differences in x and y coordinates
    dx = x2 - x1
    dy = y2 - y1

    # Determine the number of steps to take
    steps = max(abs(dx), abs(dy))

    # Calculate the increments for x and y
    x_increment = dx / steps
    y_increment = dy / steps

    # Lists to store the x and y coordinates of the line
    x_points = [x1]
    y_points = [y1]

    # Calculate and store the intermediate points
    x = x1
    y = y1
    for _ in range(steps):
        x += x_increment
        y += y_increment
        x_points.append(int(round(x)))
        y_points.append(int(round(y)))

    return x_points, y_points


if __name__ == "__main__":
    # Input the coordinates of the two endpoints of the line
    x1 = int(input("Enter the x-coordinate of the starting point: "))
    y1 = int(input("Enter the y-coordinate of the starting point: "))
    x2 = int(input("Enter the x-coordinate of the ending point: "))
    y2 = int(input("Enter the y-coordinate of the ending point: "))

    # Calculate the points using the Digital Differential Analyzer (DDA) algorithm
    x_points, y_points = digital_differential_analyzer_line(x1, y1, x2, y2)

    # Plot the line using Matplotlib
    plt.plot(x_points, y_points, marker="o")
    plt.title("Digital Differential Analyzer Line Drawing Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid()
    plt.show()
