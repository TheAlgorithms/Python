# https://en.wikipedia.org/wiki/B%C3%A9zier_curve
# https://www.tutorialspoint.com/computer_graphics/computer_graphics_curves.htm

from typing import List, Tuple
import scipy.special as sp


class BezierCurve:
    """
    A class to generate bezier curves for a given set of points. The implementation works only for 2d points.
    """

    def __init__(self, list_of_points: List[Tuple]):
        """
        The constructor of the Bezier Curve class.
            list_of_points: List of tuples on which to interpolate.
        """
        self.list_of_points = list_of_points
        self.degree = (
            len(list_of_points) - 1
        )  # degree of the curve produced will be n - 1

    def basis_function(self, t: float) -> List[float]:
        """
        The function to cater the need for the basis function.
            t: the 1-d co-ordinate at which to evaluate the basis function(s).
            returns a returns list of floating point numbers, a number at index i represents the value of
            basis function i at t.

        >>> curve1 = BezierCurve([(1,1), (1,2)])
        >>> curve1.basis_function(0)
        [1.0, 0.0]
        >>> curve1.basis_function(1)
        [0.0, 1.0]
        """
        output_values: List[float] = list()
        for i in range(len(self.list_of_points)):
            output_values.append(
                sp.comb(self.degree, i) * ((1 - t) ** (self.degree - i)) * (t ** i)
            )  # basis function for each i

        assert (
            round(sum(output_values), 5) == 1
        )  # the basis must sum up to 1 for it to produce a valid bezier curve.
        return output_values

    def bezier_curve_function(self, t: float) -> Tuple[float, float]:
        """
        The function to produce the values of the bezier curve at time t. At t = 0,
        it must return the first point, and at t = 1, it must return the last point.
            t: the value of t at which to evaluate the bezier function
        returns a 2-d tuple of floats, representing the value of the bezier curve at the given t.

        >>> curve1 = BezierCurve([(1,1), (1,2)])
        >>> curve1.bezier_curve_function(0)
        (1.0, 1.0)
        >>> curve1.bezier_curve_function(1)
        (1.0, 2.0)
        """
        basis_function = self.basis_function(t)
        x = 0.0
        y = 0.0
        for i in range(
            len(self.list_of_points)
        ):  # summing up the product of i-th basis function and ith point, for all points
            x += basis_function[i] * self.list_of_points[i][0]
            y += basis_function[i] * self.list_of_points[i][1]

        return (x, y)

    def plot_curve(self, step_size: float = 0.01):
        """
        plots the bezier curve using matplotlib plotting function.
            step_size: defines the step(s) at which to evaluate the bezier curve and plot. The smaller the step size,
            the finer the curve produced.
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

        plt.scatter(x, y, color="red", label="Control Points")
        plt.plot(to_plot_x, to_plot_y, color="blue", label="Curve")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    curve1 = BezierCurve([(1, 2), (3, 5)])
    curve1.plot_curve()

    curve1 = BezierCurve([(0, 0), (5, 5), (5, 0)])
    curve1.plot_curve()
