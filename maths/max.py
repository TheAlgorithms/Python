# Python function that calculates maximum
# point in a specified interval of a unimodal function.
# Simply change the maxF variable to the function
# you'd like to test and set the parameters of max_grs.
# ---WORKS ONLY FOR ONE VARIABLE FUNCTIONS----
# ---  IT IS RECOMMENDED TO  USE 'x' AS VARIABLE---

from matplotlib import pyplot as plt  # import module to plot the result
import numpy as np


# import module to get access to square root and linspace


def your_function(
    x,
) -> np.poly1d:  # define your function that goes into parameter func_to_max here

    max_f = (
        x ** 3 - 6 * x ** 2 + 4 * x + 12
    )  # change this to the function you'd like to test (use x as variable preferably)
    return max_f


def max_golden_search(
    func_to_max: np.poly1d, upper: float, lower: float, tol: float = 1e-8
) -> float:

    """
    Function in python that calculates the maximum
    point of function in a specified interval
        f : the function to maximize
        upper: upper boundary of interval
        lower: lower boundary of interval
        tol: set an appropriate tolerance value
        return: maximum of specified interval
    >>> max_golden_search(your_function, -2, 4)
    count = 43
    0.3670068499227286
    >>> max_golden_search(your_function, 'm', 4)
    Traceback (most recent call last):
            ...
    ValueError: give numerical values for upper, lower limits
    """
    if type(upper) is str or type(lower) is str:
        raise ValueError("give numerical values for upper, lower limits")
    else:

        inv_gr = (np.sqrt(5) - 1) * 0.5  # ~ 0.618, this is the inverse golden ratio
        d_max = (upper - lower) * inv_gr  # # Sets initial value for d
        q1 = lower + d_max  # Sets initial value for q1
        q2 = upper - d_max  # and q2

        count = 0  # Creates a count variable with initial value zero

        while (
            abs(upper - lower) > tol
        ):  # Sets the tolerance condition. Will stop running once |u -l| < tol

            if func_to_max(q1) > func_to_max(q2):
                lower = q2
            else:
                upper = q1
            d_max = (upper - lower) * inv_gr
            q1 = lower + d_max
            q2 = upper - d_max
            count += 1  # Adds one to the count per iteration

        print("count =", count)  # Prints the count number

        return (q1 + q2) * 0.5  # Returns the midpoint of the
        # final interval as the maximum point in the range


def plot_point(
    point: float = max_golden_search(your_function, -2, 4),
    x_axis: np.linspace = np.linspace(-5, 5, 200),
)->None:  # 1st parameter is the maximum point 2nd parameter is a numpy linspace
    """
    Plots function and maximum point
    """
    plt.plot(x_axis, your_function(x_axis))
    plt.plot(point, your_function(point), "bo")
    plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

"""
# References

https://en.wikipedia.org/wiki/Golden-section_search


"""
