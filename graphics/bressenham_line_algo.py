# https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm

import matplotlib.pyplot as plt


class BressenhamLineAlgo:
    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """
        Initialize the BresenhamLineAlgo object.

        Args:
            x1 (int): X-coordinate of the first point.
            y1 (int): Y-coordinate of the first point.
            x2 (int): X-coordinate of the second point.
            y2 (int): Y-coordinate of the second point.

        Initializes the object with the given coordinates and initializes
        empty lists for storing the x and y values of the line.

        >>> line = BresenhamLineAlgo(1, 2, 4, 5)
        >>> line.x1
        1
        >>> line.y1
        2
        >>> line.x2
        4
        >>> line.y2
        5
        """

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.dx: int = abs(self.x2 - self.x1)
        self.dy: int = abs(self.y2 - self.y1)
        self.p: int = 2 * self.dy - self.dx

        self.x_values: list(float) = []
        self.y_values: list(float) = []

    def draw_line(self) -> None:
        """
        Implement the Bresenham Line Algorithm to calculate the line's points.

        Calculates the points along the line using Bresenham's algorithm
        and stores them in x_values and y_values lists.

        >>> line = BresenhamLineAlgo(1, 1, 4, 4)
        >>> line.draw_line()
        >>> line.x_values
        [1, 2, 3, 4]
        >>> line.y_values
        [1, 2, 3, 4]

        """
        x: int = self.x1
        y: int = self.y1

        while x <= self.x2:
            self.x_values.append(x)
            self.y_values.append(y)

            if self.p < 0:
                self.p += 2 * self.dy
            else:
                self.p += 2 * self.dy - 2 * self.dx
                y += 1

            x += 1

        print(self.x_values)
        print(self.y_values)

    def plot_line(self) -> None:
        """
        Plot the line using Matplotlib.

        Plots the line using the x and y values calculated in the draw_line
        method. It adds labels, a title, and displays the plot.

        """
        plt.plot(self.x_values, self.y_values)
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        plt.title("Bressenham Line Algo Implementation")
        plt.grid()
        plt.show()


if __name__ == "__main__":
    x1 = int(input("Enter the X1 Coordinate: "))
    y1 = int(input("Enter the Y1 Coordinate: "))
    x2 = int(input("Enter the X2 Coordinate: "))
    y2 = int(input("Enter the Y2 Coordinate: "))

    line = BressenhamLineAlgo(x1, y1, x2, y2)

    line.draw_line()
    line.plot_line()
