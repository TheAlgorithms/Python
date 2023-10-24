import matplotlib.pyplot as plt


class Dda_Line:
    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """
        Initialize a Dda_Line object.

        Args:
            x1 (int): X-coordinate of the first point.
            y1 (int): Y-coordinate of the first point.
            x2 (int): X-coordinate of the second point.
            y2 (int): Y-coordinate of the second point.

        Initializes the object with the given coordinates and initializes
        empty lists for storing the x and y values of the line.
        """
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        self.x_values = []
        self.y_values = []

    def draw_line(self) -> None:
        """
        Implement the DDA Line Algorithm to calculate the line's points.

        Calculates the points along the line using the Digital Differential
        Analyzer (DDA) algorithm and stores them in x_values and y_values lists.
        """
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1

        steps = max(abs(dx), abs(dy))

        x_increment = dx / steps
        y_increment = dy / steps

        x = self.x1
        y = self.y1

        self.x_values.append(x)
        self.y_values.append(y)

        for _ in range(steps):
            x += x_increment
            y += y_increment

            self.x_values.append(x)
            self.y_values.append(y)

    def plot_line(self) -> None:
        """
        Plot the line using Matplotlib.

        Plots the line using the x and y values calculated in the draw_line
        method. It adds labels, a title, and displays the plot.
        """
        plt.plot(self.x_values, self.y_values)
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        plt.title("DDA Line Algorithm Implementation")
        plt.grid()
        plt.show()


if __name__ == "__main__":
    x1 = int(input("Enter the X1 Coordinate: "))
    y1 = int(input("Enter the Y1 Coordinate: "))
    x2 = int(input("Enter the X2 Coordinate: "))
    y2 = int(input("Enter the Y2 Coordinate: "))

    line = Dda_Line(x1, y1, x2, y2)

    line.draw_line()
    line.plot_line()
