import matplotlib.pyplot as plt


def dda_line(x1, y1, x2, y2):
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
        x_points.append(round(x))
        y_points.append(round(y))

    return x_points, y_points


if __name__ == "__main__":
    # Input the coordinates of the two endpoints of the line
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    # Calculate the points using DDA algorithm
    x_points, y_points = dda_line(x1, y1, x2, y2)

    # Plot the line using Matplotlib
    plt.plot(x_points, y_points, marker="o")
    plt.title("DDA Line Drawing Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid()
    plt.show()
