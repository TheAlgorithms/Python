# https://en.wikipedia.org/wiki/B%C3%A9zier_curve
# https://www.tutorialspoint.com/computer_graphics/computer_graphics_curves.htm
from __future__ import annotations
from scipy.special import comb  
from matplotlib import pyplot as plt  

class BezierCurve:
    def __init__(self, list_of_points: list[tuple[float, float]]):
        self.list_of_points = list_of_points
        self.degree = len(list_of_points) - 1
        self.combinations = [comb(self.degree, i) for i in range(self.degree + 1)]

    def basis_function(self, t: float) -> list[float]:
        assert 0 <= t <= 1, "Time t must be between 0 and 1."
        output_values: list[float] = []
        for i in range(len(self.list_of_points)):
            output_values.append(
                self.combinations[i] * ((1 - t) ** (self.degree - i)) * (t ** i)
            )
        assert round(sum(output_values), 5) == 1
        return output_values

    def bezier_curve_function(self, t: float) -> tuple[float, float]:
        assert 0 <= t <= 1, "Time t must be between 0 and 1."
        basis_function = self.basis_function(t)
        x = sum(bf * point[0] for bf, point in zip(basis_function, self.list_of_points))
        y = sum(bf * point[1] for bf, point in zip(basis_function, self.list_of_points))
        return (x, y)

    def plot_curve(self, step_size: float = 0.01):
        to_plot = [self.bezier_curve_function(t) for t in self.frange(0, 1, step_size)]

        x = [i[0] for i in self.list_of_points]
        y = [i[1] for i in self.list_of_points]

        to_plot_x, to_plot_y = zip(*to_plot)

        plt.plot(
            to_plot_x,
            to_plot_y,
            color="blue",
            label="Curve of Degree " + str(self.degree),
        )
        plt.scatter(x, y, color="red", label="Control Points")
        plt.legend()
        plt.show()

    def frange(self, start, stop, step):
        current = start
        while current < stop:
            yield current
            current += step

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    BezierCurve([(1, 2), (3, 5)]).plot_curve()  # degree 1
    BezierCurve([(0, 0), (5, 5), (5, 0)]).plot_curve()  # degree 2
    BezierCurve([(0, 0), (5, 5), (5, 0), (2.5, -2.5)]).plot_curve()  # degree 3
