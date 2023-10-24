import matplotlib.pyplot as plt


class DdaLine:
    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """
        >>> line = DdaLine(1, 2, 3, 4)
        >>> line.x1
        1
        >>> line.y1
        2
        >>> line.x2
        3
        >>> line.y2
        4
        """
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        self.x_values: list[float] = []
        self.y_values: list[float] = []

    def draw_line(self) -> None:
        """
        >>> line = DdaLine(1, 1, 4, 4)
        >>> line.draw_line()
        >>> line.x_values
        [1.0, 2.0, 3.0, 4.0]
        >>> line.y_values
        [1.0, 2.0, 3.0, 4.0]
        """
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1

        steps = max(abs(dx), abs(dy))

        x_increment = dx / steps
        y_increment = dy / steps

        x: float = self.x1
        y: float = self.y1

        self.x_values.append(x)
        self.y_values.append(y)

        for _ in range(steps):
            x += x_increment
            y += y_increment

            self.x_values.append(x)
            self.y_values.append(y)

    def plot_line(self) -> None:
        """ """
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

    line = DdaLine(x1, y1, x2, y2)

    line.draw_line()
    line.plot_line()
