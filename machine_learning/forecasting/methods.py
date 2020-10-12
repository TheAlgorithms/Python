import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.svm import SVR


def lin_reg_pred(train_dt, train_usr, train_mtch, test_dt, test_mtch):
    # linear regression, return float
    x = []
    for i in range(len(train_dt)):
        x.append([1, train_dt[i], train_mtch[i]])
    x = np.array(x)
    y = np.array(train_usr)
    beta = np.dot(np.dot(np.linalg.inv(np.dot(x.transpose(), x)), x.transpose()), y)
    prediction = abs(beta[0] + test_dt[0] * beta[1] + test_mtch[0] + beta[2])
    return prediction


def sarimax_predictor(train_user, train_match, test_match):
    # sarimax, return list of float
    order = (1, 2, 1)
    s_order = (1, 1, 0, 7)
    model = SARIMAX(train_user, exog=train_match, order=order, seasonal_order=s_order)
    model_fit = model.fit(disp=False, maxiter=600, method='nm')
    result = model_fit.predict(1, len(test_match), exog=[test_match])
    return result[0]


def support_machine_regressor(x_train, x_test, train_user):
    # svr, return list of float
    regressor = SVR(kernel='rbf', C=1, gamma=0.1, epsilon=.1)
    regressor.fit(x_train, train_user)
    y_pred = regressor.predict(x_test)

    return y_pred[0]


def interquartile_range_checker(train_user):
    # optional
    # return low limit and upper limit for outlier
    train_user.sort()
    q1 = np.percentile(train_user, 25)
    q3 = np.percentile(train_user, 75)
    iqr = q3 - q1
    low_lim = q1 - (iqr * 0.1)

    return low_lim
