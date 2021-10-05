import math
from typing import List

import numpy as np
import pandas as pd

"""
lagrange is a mathematical interpolation methods that approximate
a polynomial of degree n given n-1 points
"""


def lagrange(x_coordinate: List, y_coordinate: List) -> List:
    """
    the lagrange method that takes n points as input and return a pandas dataframe
    """
    my_columns = ["x", "y"]
    dataframe = pd.DataFrame(columns=my_columns)

    for pt in np.arange(-1, 2, 0.001):
        condition = False
        for i in range(0, len(X)):
            check = False
            for j in range(0, len(X)):
                if i is not j and check is False:
                    line = (pt - x_coordinate[j]) / (x_coordinate[i] - x_coordinate[j])
                    L = line
                    check = True
                elif i is not j:
                    L = L * (pt - x_coordinate[j]) / (x_coordinate[i] - x_coordinate[j])
            if condition is False:
                P = y_coordinate[i] * L
                condition = True
            else:
                P = y_coordinate[i] * L + P
        dataframe = dataframe.append(
            pd.Series([pt, P], index=my_columns), ignore_index=True
        )
    return dataframe


if __name__ == "__main__":
    """
    creating the polynome that we want to approximate
    using lagrange method
    """
    my_columns = ["x", "y"]
    dataframe = pd.DataFrame(columns=my_columns)
    for i in np.arange(-1, 2, 0.001):
        dataframe = dataframe.append(
            pd.Series([i, pow(i, 3)], index=my_columns), ignore_index=True
        )
    """
    calculating the mean square error from the given polynome and the result
    """
    res = lagrange(np.array([-1, 1, 2]), np.array([-1, 1, 8]))
    m = len(dataframe)
    diff = pow(dataframe["y"] - res["y"], 2).sum()
    RMSE = 1 / m * (math.sqrt(diff))
    print(RMSE)
    """
    >>> my_columns = ["x", "y"]
    >>> dataframe = pd.DataFrame(columns=my_columns)
    >>> for i in np.arange(-1, 2, 0.001):
    ...    dataframe = dataframe.append(
    ...        pd.Series([i, pow(i, 3)], index=my_columns), ignore_index=True)
    >>> res = lagrange(np.array([-1, 1, 2]), np.array([-1, 1, 8]))
    >>> m = len(dataframe)
    >>> diff = pow(dataframe["y"] - res["y"], 2).sum()
    >>> RMSE = 1 / m * (math.sqrt(diff))
    >>> print(RMSE)
    0.02267786838055191
    """
