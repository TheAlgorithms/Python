import matplotlib.pyplot as plt


class DDA_Lines:
    def __init__(self, x1, y1, x2, y2) -> None:
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        self.x_values = []
        self.y_values = []

    def draw_line(self):
        dx = x2 - x1
        dy = y2 - y1

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

    def plot_line(self):
        plt.plot(self.x_values, self.y_values)
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        plt.title("DDA Line Algo Implementation")
        plt.grid()
        plt.show()


if __name__ == "__main__":
    x1 = int(input("Enter the X1 Cordinate: "))
    y1 = int(input("Enter the Y1 Cordinate: "))
    x2 = int(input("Enter the X2 Cordinate: "))
    y2 = int(input("Enter the Y2 Cordinate: "))

    line = DDA_Lines(x1, y1, x2, y2)

    line.draw_line()
    line.plot_line()
