"""
this is code for forecasting
but I modified it and used it for safety checker of data
for ex: you have an online shop and for some reason some data are
missing (the amount of data that u expected are not supposed to be)
        then we can use it
*ps : 1. ofc we can use normal statistic method but in this case
         the data is quite absurd and only a little^^
      2. ofc u can use this and modified it for forecasting purpose
         for the next 3 months sales or something,
         u can just adjust it for ur own purpose
"""

from warnings import simplefilter

import numpy as np
import pandas as pd
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVR
from statsmodels.tsa.statespace.sarimax import SARIMAX


def linear_regression_prediction(
    train_dt: list, train_usr: list, train_mtch: list, test_dt: list, test_mtch: list
) -> float:
    """
    First method: linear regression
    input : training data (date, total_user, total_event) in list of float
    output : list of total user prediction in float
    >>> n = linear_regression_prediction([2,3,4,5], [5,3,4,6], [3,1,2,4], [2,1], [2,2])
    >>> abs(n - 5.0) < 1e-6  # Checking precision because of floating point errors
    True
    """
    x = np.array([[1, item, train_mtch[i]] for i, item in enumerate(train_dt)])
    y = np.array(train_usr)
    beta = np.dot(np.dot(np.linalg.inv(np.dot(x.transpose(), x)), x.transpose()), y)
    return abs(beta[0] + test_dt[0] * beta[1] + test_mtch[0] + beta[2])


def sarimax_predictor(train_user: list, train_match: list, test_match: list) -> float:
    """
    second method: Sarimax
    sarimax is a statistic method which using previous input
    and learn its pattern to predict future data
    input : training data (total_user, with exog data = total_event) in list of float
    output : list of total user prediction in float
    >>> sarimax_predictor([4,2,6,8], [3,1,2,4], [2])
    6.6666671111109626
    """
    # Suppress the User Warning raised by SARIMAX due to insufficient observations
    simplefilter("ignore", UserWarning)
    order = (1, 2, 1)
    seasonal_order = (1, 1, 1, 7)
    model = SARIMAX(
        train_user, exog=train_match, order=order, seasonal_order=seasonal_order
    )
    model_fit = model.fit(disp=False, maxiter=600, method="nm")
    result = model_fit.predict(1, len(test_match), exog=[test_match])
    return result[0]


def support_vector_regressor(x_train: list, x_test: list, train_user: list) -> float:
    """
    Third method: Support vector regressor
    svr is quite the same with svm(support vector machine)
    it uses the same principles as the SVM for classification,
    with only a few minor differences and the only different is that
    it suits better for regression purpose
    input : training data (date, total_user, total_event) in list of float
    where x = list of set (date and total event)
    output : list of total user prediction in float
    >>> support_vector_regressor([[5,2],[1,5],[6,2]], [[3,2]], [2,1,4])
    1.634932078116079
    """
    regressor = SVR(kernel="rbf", C=1, gamma=0.1, epsilon=0.1)
    regressor.fit(x_train, train_user)
    y_pred = regressor.predict(x_test)
    return y_pred[0]


def interquartile_range_checker(train_user: list) -> float:
    """
    Optional method: interquatile range
    input : list of total user in float
    output : low limit of input in float
    this method can be used to check whether some data is outlier or not
    >>> interquartile_range_checker([1,2,3,4,5,6,7,8,9,10])
    2.8
    """
    train_user.sort()
    q1 = np.percentile(train_user, 25)
    q3 = np.percentile(train_user, 75)
    iqr = q3 - q1
    low_lim = q1 - (iqr * 0.1)
    return low_lim


def data_safety_checker(list_vote: list, actual_result: float) -> bool:
    """
    Used to review all the votes (list result prediction)
    and compare it to the actual result.
    input : list of predictions
    output : print whether it's safe or not
    >>> data_safety_checker([2, 3, 4], 5.0)
    False
    """
    safe = 0
    not_safe = 0

    if not isinstance(actual_result, float):
        raise TypeError("Actual result should be float. Value passed is a list")

    for i in list_vote:
        if i > actual_result:
            safe = not_safe + 1
        elif abs(abs(i) - abs(actual_result)) <= 0.1:
            safe += 1
        else:
            not_safe += 1
    return safe > not_safe


if __name__ == "__main__":
    """
    data column = total user in a day, how much online event held in one day,
    what day is that(sunday-saturday)
    """
    data_input_df = pd.read_csv("ex_data.csv")

    # start normalization
    normalize_df = Normalizer().fit_transform(data_input_df.values)
    # split data
    total_date = normalize_df[:, 2].tolist()
    total_user = normalize_df[:, 0].tolist()
    total_match = normalize_df[:, 1].tolist()

    # for svr (input variable = total date and total match)
    x = normalize_df[:, [1, 2]].tolist()
    x_train = x[: len(x) - 1]
    x_test = x[len(x) - 1 :]

    # for linear regression & sarimax
    train_date = total_date[: len(total_date) - 1]
    train_user = total_user[: len(total_user) - 1]
    train_match = total_match[: len(total_match) - 1]

    test_date = total_date[len(total_date) - 1 :]
    test_user = total_user[len(total_user) - 1 :]
    test_match = total_match[len(total_match) - 1 :]

    # voting system with forecasting
    res_vote = [
        linear_regression_prediction(
            train_date, train_user, train_match, test_date, test_match
        ),
        sarimax_predictor(train_user, train_match, test_match),
        support_vector_regressor(x_train, x_test, train_user),
    ]

    # check the safety of today's data
    not_str = "" if data_safety_checker(res_vote, test_user[0]) else "not "
    print(f"Today's data is {not_str}safe.")
