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


def ols_regression(x, y):
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
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # Calculate the slope of the regression line.
    b = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)

    # Calculate the intercept of the regression line.
    a = y_mean - b * x_mean

    return a, b


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Load the data
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 6, 8, 10])

    # Perform OLS regression
    a, b = ols_regression(x, y)

    # Intercept (a) and slope (b) of the regression line
    print("Intercept:", a)
    print("Slope:", b)

    # Predict the target variable for a new data point with
    # an independent variable value of 6
    x_new = 6

    # Make a prediction
    y_pred = a + b * x_new

    print("Prediction:", y_pred)
