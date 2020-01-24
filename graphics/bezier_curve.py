# https://en.wikipedia.org/wiki/B%C3%A9zier_curve
# https://www.tutorialspoint.com/computer_graphics/computer_graphics_curves.htm

from typing import List, Tuple
from scipy.special import comb


class BezierCurve:
    """
    Generate bezier curves for a given set of points.
    The implementation works only for 2d points.
    """

    def __init__(self, list_of_points: List[Tuple[float, float]]):
        """
        The constructor of the Bezier Curve class.
            list_of_points: Data points in the xy plane on which to interpolate. These
            basically serve as the control points (control the behavior of curve),
            of the bezier curve.
        """
        self.list_of_points = list_of_points
        self.degree = (
            len(list_of_points)
            - 1  # determines the flexibility of the curve. Degree = 1 produces a straight line.
        )

    def basis_function(self, t: float) -> List[float]:
        """
        Bezier Curve is a weighted sum of the control points. Weight of each control point, as
            a function of time t is called the basis function.
            t: time value between 0 and 1 inclusive at which to evaluate the basis of the curve.
        returns the x, y values of basis function at time t

        >>> curve1 = BezierCurve([(1,1), (1,2)])
        >>> curve1.basis_function(0)
        [1.0, 0.0]
        >>> curve1.basis_function(1)
        [0.0, 1.0]
        """
        assert 0 <= t <= 1  # t must be between 0 and 1
        output_values: List[float] = list()
        for i in range(len(self.list_of_points)):
            # basis function for each i
            output_values.append(
                comb(self.degree, i) * ((1 - t) ** (self.degree - i)) * (t ** i)
            )

        assert (
            round(sum(output_values), 5)
            == 1  # the basis must sum up to 1 for it to produce a valid bezier curve.
        )
        return output_values

    def bezier_curve_function(self, t: float) -> Tuple[float, float]:
        """
        The function to produce the values of the bezier curve at time t. At t = 0,
        it must return the first point, and at t = 1, it must return the last point.
            t: the value of t at which to evaluate the bezier function
        Returns the x, y coordinates of the Bezier curve at time t.
            The first point in the curve is when t = 0.
            The last point in the curve is when t = 1.

        >>> curve1 = BezierCurve([(1,1), (1,2)])
        >>> curve1.bezier_curve_function(0)
        (1.0, 1.0)
        >>> curve1.bezier_curve_function(1)
        (1.0, 2.0)
        """

        assert 0 <= t <= 1  # t must be between 0 and 1.

        basis_function = self.basis_function(t)
        x = 0.0
        y = 0.0
        for i in range(len(self.list_of_points)):
            # summing up the product of i-th basis function and i-th point, for all points.
            x += basis_function[i] * self.list_of_points[i][0]
            y += basis_function[i] * self.list_of_points[i][1]

        return (x, y)

    def plot_curve(self, step_size: float = 0.01):
        """
        plots the bezier curve using matplotlib plotting function.
            step_size: defines the step(s) at which to evaluate the bezier curve and plot.
            The smaller the step size, the finer the curve produced.
        """
        import matplotlib.pyplot as plt

        to_plot_x: List[float] = []  # x coordinates of points to plot
        to_plot_y: List[float] = []  # y coordinates of points to plot

        t = 0
        while t <= 1:
            value = self.bezier_curve_function(t)
            to_plot_x.append(value[0])
            to_plot_y.append(value[1])
            t += step_size

        x = [i[0] for i in self.list_of_points]
        y = [i[1] for i in self.list_of_points]

        plt.plot(
            to_plot_x,
            to_plot_y,
            color="blue",
            label="Curve of Degree " + str(self.degree),
        )
        plt.scatter(x, y, color="red", label="Control Points")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    BezierCurve([(1, 2), (3, 5)]).plot_curve()  # degree 1

    BezierCurve([(0, 0), (5, 5), (5, 0)]).plot_curve()  # degree 2

    BezierCurve([(0, 0), (5, 5), (5, 0), (2.5, -2.5)]).plot_curve()  # degree 3
