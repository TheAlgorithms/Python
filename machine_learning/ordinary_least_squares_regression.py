"""
Ordinary Least Squares Regression (OLSR):

Ordinary Least Squares Regression (OLSR) is a statistical method for
estimating the parameters of a linear regression model.
It is the most commonly used regression method,
and it is based on the principle of minimizing
the sum of the squared residuals.

Below is simple implementation of OLSR
without using any external libraries.

WIKI: https://en.wikipedia.org/wiki/Ordinary_least_squares
"""

import numpy as np


def ols_regression(x_point: np.ndarray, y_point: np.ndarray) -> tuple:
    """
    Performs Ordinary Least Squares Regression (OLSR) on the given data.

    Args:
        x (numpy.ndarray): The independent variable.
        y (numpy.ndarray): The dependent variable.

    Returns:
        a (float): The intercept of the regression line.
        b (float): The slope of the regression line.

    Examples:
    >>> x = np.array([1, 2, 3, 4, 5])
    >>> y = np.array([2, 4, 6, 8, 10])
    >>> a, b = ols_regression(x, y)
    >>> a  # Intercept should be 0.0
    0.0
    >>> round(b, 2)  # Slope should be 2.0
    2.0
    """

    # Calculate the mean of the independent variable and
    # the dependent variable.
    x_mean = np.mean(x_point)
    y_mean = np.mean(y_point)

    # Calculate the slope of the regression line.
    slope = np.sum((x_point - x_mean) * (y_point - y_mean)) / np.sum(
        (x_point - x_mean) ** 2
    )

    # Calculate the intercept of the regression line.
    intercept = y_mean - slope * x_mean

    return intercept, slope


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Load the data
    x_points = np.array([1, 2, 3, 4, 5])
    y_points = np.array([2, 4, 6, 8, 10])

    # Perform OLS regression
    intercept, slope = ols_regression(x_points, y_points)

    # Intercept (a) and slope (b) of the regression line
    print("Intercept:", intercept)
    print("Slope:", slope)

    # Predict the target variable for a new data point with
    # an independent variable value of 6
    x_new = 6

    # Make a prediction
    y_pred = intercept + slope * x_new

    print("Prediction:", y_pred)
