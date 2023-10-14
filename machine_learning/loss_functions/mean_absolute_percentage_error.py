import numpy as np

"""
Mean Absolute Percentage Error :
It calculates the average of the absolute percentage differences between the
predicted and true values.

Formula = (Σ|y_true[i]-Y_pred[i]/y_true[i]|)/n

https://stephenallwright.com/good-mape-score/

"""


def mean_absolute_percentage_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calculate the Mean Absolute Percentage Error between y_true and y_pred.

    Parameters:
    y_true (np.ndarray): Numpy array containing true/target values.
    y_pred (np.ndarray): Numpy array containing predicted values.

    Returns:
    float: The Mean Absolute Percentage error between y_true and y_pred.

    Examples:
    >>> y_true = np.array([10, 20, 30, 40])
    >>> y_pred = np.array([12, 18, 33, 45])
    >>> mean_absolute_percentage_error(y_true, y_pred)
    9.722222222222221

    >>> y_true = np.array([1, 2, 3, 4])
    >>> y_pred = np.array([2, 3, 4, 5])
    >>> mean_absolute_percentage_error(y_true, y_pred)
    25.0

    >>> y_true = np.array([5, 0, 10, 20])
    >>> y_pred = np.array([5, 0, 9, 15])
    >>> mean_absolute_percentage_error(y_true, y_pred)
    18.75
    """
    try:
        if len(y_true) != len(y_pred):
            error_message = "the length of the two arrays should be same."
            raise ValueError(error_message)

        # Calculate the absolute percentage difference between y_true and y_pred
        # added 1e-9 to avoid division by 0 (smoothing).
        absolute_percentage_diff = np.abs((y_true - y_pred) / (y_true + 1e-9))

        # Calculate the mean and multiply by 100 for percentage.
        error = np.mean(absolute_percentage_diff) * 100

        return error

    except ValueError as e:
        raise e


if __name__ == "__main__":
    import doctest
    doctest.testmod()
