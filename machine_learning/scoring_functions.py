import numpy as np

""" Here I implemented the scoring functions.
    MAE, MSE, RMSE, RMSLE are included.

    Those are used for calculating differences between
    predicted values and actual values.

    Metrics are slightly differentiated. Sometimes squared, rooted,
    even log is used.

    Using log and roots can be perceived as tools for penalizing big
    errors. However, using appropriate metrics depends on the situations,
    and types of data
"""


# Mean Absolute Error
def mae(predict, actual):
    """
    Examples(rounded for precision):
    >>> actual = [1,2,3];predict = [1,4,3]
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


# Mean Squared Error
def mse(predict, actual):
    """
    Examples(rounded for precision):
    >>> actual = [1,2,3];predict = [1,4,3]
    >>> np.around(mse(predict,actual),decimals = 2)
    1.33

    >>> actual = [1,1,1];predict = [1,1,1]
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
    Examples(rounded for precision):
    >>> actual = [1,2,3];predict = [1,4,3]
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
    >>> actual = [10,10,30];predict = [10,2,30]
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
    >>> actual = [1,2,3];predict = [2,3,4]
    >>> np.around(mbd(predict,actual),decimals = 2)
    50.0

    Here the model underpredicts
    >>> actual = [1,2,3];predict = [0,1,1]
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


def binary_precision(predict, actual):
    """
    an important metric for binary classification problems
    See https://en.wikipedia.org/wiki/Precision_and_recall#Definition_(classification_context)

    Examples(rounded for precision):
    >>> predicted = [1, 1, 0, 0, 1]; true = [1, 0, 0, 1, 1]
    >>> np.around(binary_precision(predicted, true), decimals = 2)
    0.67

    >>> predicted = [1, 1, 0]; true = [1, 1, 1]
    >>> binary_precision(predicted, true)
    1.0
    """
    pred, true = np.array(predict), np.array(actual)
    true_positives = np.sum(np.logical_and(pred == 1, true == 1))
    false_positives = np.sum(np.logical_and(pred == 1, true == 0))
    return true_positives / (true_positives + false_positives)


def binary_recall(predict, actual):
    """
    an important metric for binary classification problems
    See https://en.wikipedia.org/wiki/Precision_and_recall#Definition_(classification_context)

    Examples(rounded for precision):
    >>> predicted = [1, 1, 0, 0, 1]; true = [1, 0, 0, 1, 1]
    >>> np.around(binary_recall(predicted, true), decimals = 2)
    0.67

    >>> predicted = [1, 1, 0]; true = [1, 1, 1]
    >>> np.around(binary_recall(predicted, true), decimals = 2)
    0.67
    """
    pred, true = np.array(predict), np.array(actual)
    true_positives = np.sum(np.logical_and(pred == 1, true == 1))
    false_negatives = np.sum(np.logical_and(pred == 0, true == 1))
    return true_positives / (true_positives + false_negatives)


def binary_f1(predict, actual):
    """
    an important metric for binary classification problems combining precision and recall
    See https://en.wikipedia.org/wiki/F1_score

    Examples(rounded for precision):
    >>> predicted = [1, 1, 0, 0, 1]; true = [1, 0, 0, 1, 1]
    >>> np.around(binary_f1(predicted, true), decimals = 2)
    0.67

    >>> predicted = [1, 1, 0]; true = [1, 1, 1]
    >>> np.around(binary_f1(predicted, true), decimals = 2)
    0.8
    """
    precision = binary_precision(predict, actual)
    recall = binary_recall(predict, actual)
    return 2 * precision * recall / (precision + recall)
