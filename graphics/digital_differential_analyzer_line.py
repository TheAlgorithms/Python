import matplotlib.pyplot as plt


def digital_differential_analyzer_line(
    x1: int, y1: int, x2: int, y2: int
) -> list[tuple[int, int]]:
    """
    Draw a line using the Digital Differential Analyzer (DDA) algorithm.

    Parameters:
        x1 (int): The x-coordinate of the starting point.
        y1 (int): The y-coordinate of the starting point.
        x2 (int): The x-coordinate of the ending point.
        y2 (int): The y-coordinate of the ending point.

    Returns:
        list of coordinate pairs (x, y).

    Example:
        >>> digital_differential_analyzer_line(0, 0, 3, 2)
        [(0, 0), (1, 1), (2, 1), (3, 2)]
    """

    # Calculate the differences in x and y coordinates
    dx = x2 - x1
    dy = y2 - y1

    # Determine the number of steps to take
    steps = max(abs(dx), abs(dy))

    # Calculate the increments for x and y
    x_increment = dx / steps
    y_increment = dy / steps

    # List to store the coordinate pairs
    coordinates = []

    # Calculate and store the intermediate points
    x = x1
    y = y1
    for _ in range(steps):
        x += x_increment
        y += y_increment
        coordinates.append((int(round(x)), int(round(y))))

    return coordinates


if __name__ == "__main__":
    # Input the coordinates of the two endpoints of the line
    x1 = int(input("Enter the x-coordinate of the starting point: "))
    y1 = int(input("Enter the y-coordinate of the starting point: "))
    x2 = int(input("Enter the x-coordinate of the ending point: "))
    y2 = int(input("Enter the y-coordinate of the ending point: "))

    # Calculate the points using the Digital Differential Analyzer (DDA) algorithm
    coordinates = digital_differential_analyzer_line(x1, y1, x2, y2)

    # Plot the line using Matplotlib
    x_points, y_points = zip(*coordinates)
    plt.plot(x_points, y_points, marker="o")
    plt.title("Digital Differential Analyzer Line Drawing Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid()
    plt.show()
