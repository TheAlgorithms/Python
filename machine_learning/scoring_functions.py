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


def cross_entropy(actual, predicted):
    """
    Cross Entropy can be used to calculate the difference between two sets of probability distributions
    """
    sum = 0

    for i in range(len(actual)):
        sum += actual[i] * np.log(predicted[i])

    return (
        -sum
    )  # as cross_entropy = -sum(P(x)*log(Q(x))) where x is the event and P,Q are 2 probability distributions


def binary_crossentropy(y, yhat):

    """
    let y be our actual label and yhat be our model prediction.
    To use cross entropy we must create the probability distribution first

    Examples(rounded for precision):
    >>> y=[1, 1, 0, 0]
    >>> yhat = [0.8, 0.9, 0.1, 0.3]
    >>> print("Average cross entropy=",binary_crossentropy(y,yhat))
    For y=1 and yhat=0.8, cross entropy= 0.2231435513142097
    For y=1 and yhat=0.9, cross entropy= 0.10536051565782628
    For y=0 and yhat=0.1, cross entropy= 0.10536051565782628
    For y=0 and yhat=0.3, cross entropy= 0.35667494393873245
    Average cross entropy= 0.19763488164214868

    >>> y=[0, 1, 1, 0]
    >>> yhat = [0.6, 0.7, 0.8, 0.4]
    >>> print("Average cross entropy=",binary_crossentropy(y,yhat))
    For y=0 and yhat=0.6, cross entropy= 0.916290731874155
    For y=1 and yhat=0.7, cross entropy= 0.35667494393873245
    For y=1 and yhat=0.8, cross entropy= 0.2231435513142097
    For y=0 and yhat=0.4, cross entropy= 0.5108256237659907
    Average cross entropy= 0.5017337127232719

    Creating probability distribution
    Since we are caclulating binary cross entropy we need to create the probability distribution for these 2 classes
    """
    elements = []
    for i in range(len(y)):
        actual = [
            1 - y[i],
            y[i],
        ]  # Zeroth index stores the probabilty of class 0 and first index stores the probability of class 1 calculated from our actual outputs
        predicted = [
            1 - yhat[i],
            yhat[i],
        ]  # Zeroth index stores the probabilty of class 0 and first index stores the probability of class 1 calculated from our actual outputs
        ans = cross_entropy(actual, predicted)
        print(f"For y={y[i]} and yhat={yhat[i]}, cross entropy= {ans}")
        elements.append(ans)

    avg_score = np.mean(elements)
    return avg_score


def manual_accuracy(predict, actual):
    return np.mean(np.array(actual) == np.array(predict))
