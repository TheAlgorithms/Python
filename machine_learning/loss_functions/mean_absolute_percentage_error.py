import numpy as np
import doctest

"""
Mean Absolute Percentage Error (MAPE): 
MAPE calculates the average of the absolute percentage differences between the
predicted and true values.

MAPE = (Σ|y_true[i]-Y_pred[i]/y_true[i]|)/n

https://stephenallwright.com/good-mape-score/

"""


def mean_absolute_percentage_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calculate the Mean Absolute Percentage Error (MAPE) between y_true and y_pred.

    Parameters:
    y_true (np.ndarray): Numpy array containing true/target values.
    y_pred (np.ndarray): Numpy array containing predicted values.

    Returns:
    float: The MAPE between y_true and y_pred.
    """
    try:
        if len(y_true) != len(y_pred):
            raise ValueError(
                f"The length of the target array ({len(y_true)}) and"
                f" the predicted array ({len(y_pred)}) are not the same."
            )

        # Calculate the absolute percentage difference between y_true and y_pred
        # addded 1e-9 to avoid divison by 0 (smoothing).
        absolute_percentage_diff = np.abs((y_true - y_pred) / (y_true + 1e-9))

        # Calculate the mean and multiply by 100 for percentage.
        mape = np.mean(absolute_percentage_diff) * 100

        return mape

    except ValueError as e:
        raise e


if __name__ == "__main__":
    doctest.testmod()
