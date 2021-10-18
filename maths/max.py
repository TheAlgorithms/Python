# Python function that calculates maximum point in a specified interval of a unimodal function. Simply change the maxF variable to the function you'd like to test and set the parameters of max_grs.
# ---WORKS ONLY FOR ONE VARIABLE FUNCTIONS----
# ---  IT IS RECOMMENDED TO  USE 'x' AS VARIABLE---

from matplotlib import pyplot as plt  # import module to plot the result
import numpy as np
from numpy.core.function_base import (
    linspace,
)  # import module to get access to square root and linspace


def f(x):  # define your function that goes into parameter f here
    maxF = x ** 3 - 6 * x ** 2 + 4 * x + 12
    return maxF


def max_golden_search(f, u: float, l: float, tol: float = 1e-8) -> float:

    """
    Function in python that calculates the maximum point of function in a specified interval
        f : the function to maximize
        u: upper boundary of interval
        l: lower boundary of interval
        tol: set an appropriate tolerance value
        return: maximum of specified interval


    >>> max_golden_search(f, -2, 4)
    count = 43
    0.3670068499227286
    >>> max_golden_search(f, 'm', 4)
    Traceback (most recent call last):
            ...
    ValueError: Please give numerical values for upper, lower limits

    """

    if type(u) is str or type(l) is str:
        raise ValueError("Please give numerical values for upper, lower limits")
    else:

        inv_gr = (np.sqrt(5) - 1) * 0.5  # ~ 0.618
        d_max = (u - l) * inv_gr  # # Sets initial value for d
        q1 = l + d_max  # Sets initial value for q1
        q2 = u - d_max  # and q2

        count = 0  # Creates a count variable with initial value zero

        while (
            abs(u - l) > tol
        ):  # Sets the tolerance condition. Will stop running once |u -l| < tol

            if f(q1) > f(q2):
                l = q2
            else:
                u = q1
            d_max = (u - l) * inv_gr
            q1 = l + d_max
            q2 = u - d_max
            count += 1  # Adds one to the count per iteration

        print("count =", count)  # Prints the count number

        return (
            q1 + q2
        ) * 0.5  # Returns the midpoint of the final interval as the maximum point in the range


def plot_point(
    point, x_axis=np.linspace(-5, 5, 200)
):  # 1st parameter is the maximum point 2nd parameter is a numpy linspace
    """
    Plots function and maximum point
    """
    plt.plot(x_axis, f(x_axis))
    plt.plot(point, f(point), "bo")
    plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
"""
# References
https://en.wikipedia.org/wiki/Golden-section_search



"""
