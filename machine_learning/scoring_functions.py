import numpy as np

""" Here I implemented the scoring functions.
    MAE, MAPE, MSE, RMSE, RMSLE are included.

    Those are used for calculating differences between
    predicted values and actual values.

    Metrics are slightly differentiated. Sometimes squared, rooted,
    even log is used.

    Using log and roots can be perceived as tools for penalizing big
    errors. However, using appropriate metrics depends on the situations,
    and types of data.
"""


# Mean Absolute Error
def mae(predict: list, actual: list) -> float:
    """
    Function: mae
        The MAE score is measured as the average of the absolute error values.
        This function calculates the absolute difference between actual value
        and predict value. Lower MAE means that a model's predictions are
        closer the actual value, which usually tells that the model has high
        forecast accuracy.
    Parameters:
        predict - list - the predict value
        actual - list - the actual value
    Examples(rounded for precision):
    >>> predict = [1,4,3]; actual = [1,2,3]
    >>> np.around(mae(predict,actual),decimals = 2)
    0.67
    >>> actual = [1,1,1];predict = [1,1,1]
    >>> mae(predict,actual)
    0.0
    """
    predict = np.array(predict)
    actual = np.array(actual)

    difference = abs(predict - actual)
    score = difference.mean()

    return score


def mape(predict: list, actual: list) -> float:
    """
    Function: mape
        The MAPE score is measured as the average of the percentage absolute
        error values. This function calculates the absolute percentage
        difference between actual value and predict value. Lower MAPE means
        that a model's predictions are closer the actual value, which usually
        tells that the model has high forecast accuracy.
    Parameters:
        predict - list - the predict value
        actual - list - the actual value
    Example(rounded for precision):
    >>> predict = [1,4,3]; actual = [1,2,3]
    >>> np.around(mape(predict,actual), decimals = 2)
    0.33
    >>> predict = [1,1,1]; actual = [1,1,1]
    >>> mape(predict, actual)
    0.0

    """
    predict = np.array(predict)
    actual = np.array(actual)
    pct_difference = abs((predict - actual) / actual)
    score = pct_difference.mean()

    return score


# Mean Squared Error
def mse(predict: list, actual: list) -> float:
    """
    Function: mse
        The MSE score is measured as the average squared error values.
        This function calculates the square of absolute difference
        between actual value and predict value. Lower MSE means that
        a model's predictions are closer the actual value, which usually
        tells that the model has high forecast accuracy.
    Parameters:
        predict - list - the predict value
        actual - list - the actual value
    Examples(rounded for precision):
    >>> predict = [1,4,3]; actual = [1,2,3]
    >>> np.around(mse(predict,actual),decimals = 2)
    1.33
    >>> predict = [1,1,1]; actual = [1,1,1]
    >>> mse(predict,actual)
    0.0
    """
    predict = np.array(predict)
    actual = np.array(actual)

    difference = predict - actual
    square_diff = np.square(difference)

    score = square_diff.mean()
    return score


# Root Mean Squared Error
def rmse(predict, actual):
    """
    Function: mse
        The RMSE (root-mean-square error) represents the square root
        of MSE. The RMSE score is measured as the average difference
        between model's predicted value and the actual value.
        This function calculates the average difference between actual
        value and predict value. Lower RMSE means that a model's
        predictions are closer the actual value, which usually tells
        that the model has high forecast accuracy.
    Parameters:
        predict - list - the predict value
        actual - list - the actual value
    Examples(rounded for precision):
    >>> predict = [1,4,3]; actual = [1,2,3]
    >>> np.around(rmse(predict,actual),decimals = 2)
    1.15

    >>> actual = [1,1,1];predict = [1,1,1]
    >>> rmse(predict,actual)
    0.0
    """
    predict = np.array(predict)
    actual = np.array(actual)

    difference = predict - actual
    square_diff = np.square(difference)
    mean_square_diff = square_diff.mean()
    score = np.sqrt(mean_square_diff)
    return score


# Root Mean Square Logarithmic Error
def rmsle(predict, actual):
    """
    Examples(rounded for precision):
    >>> predict = [10,2,30]; actual = [10,10,30]
    >>> np.around(rmsle(predict,actual),decimals = 2)
    0.75

    >>> actual = [1,1,1];predict = [1,1,1]
    >>> rmsle(predict,actual)
    0.0
    """
    predict = np.array(predict)
    actual = np.array(actual)

    log_predict = np.log(predict + 1)
    log_actual = np.log(actual + 1)

    difference = log_predict - log_actual
    square_diff = np.square(difference)
    mean_square_diff = square_diff.mean()

    score = np.sqrt(mean_square_diff)

    return score


# Mean Bias Deviation
def mbd(predict, actual):
    """
    This value is Negative, if the model underpredicts,
    positive, if it overpredicts.

    Example(rounded for precision):

    Here the model overpredicts
    >>> predict = [2,3,4]; actual = [1,2,3]
    >>> np.around(mbd(predict,actual),decimals = 2)
    50.0

    Here the model underpredicts
    >>> predict = [0,1,1]; actual = [1,2,3]
    >>> np.around(mbd(predict,actual),decimals = 2)
    -66.67
    """
    predict = np.array(predict)
    actual = np.array(actual)

    difference = predict - actual
    numerator = np.sum(difference) / len(predict)
    denumerator = np.sum(actual) / len(predict)
    # print(numerator, denumerator)
    score = float(numerator) / denumerator * 100

    return score


def manual_accuracy(predict, actual):
    return np.mean(np.array(actual) == np.array(predict))


if __name__ == "__main__":
    import doctest
<<<<<<< HEAD
=======

>>>>>>> dc285eb2a1adcd0883b4d3fbcb0d4134b536e2c4
    doctest.testmod()
