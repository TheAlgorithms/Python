from warnings import simplefilter
import numpy as np
import pandas as pd
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVR
from statsmodels.tsa.statespace.sarimax import SARIMAX


def linear_regression_prediction(
    train_dt: list[float], train_usr: list[float], train_mtch: list[float],
    test_dt: list[float], test_mtch: list[float]
) -> float:
    """
    Perform linear regression to predict total users.
    
    Args:
        train_dt: Training dates
        train_usr: Total users for training data
        train_mtch: Total matches for training data
        test_dt: Testing dates
        test_mtch: Total matches for testing data
    
    Returns:
        Predicted total users for the test date.
    """
    x = np.array([[1, dt, mtch] for dt, mtch in zip(train_dt, train_mtch)])
    y = np.array(train_usr)
    beta = np.linalg.inv(x.T @ x) @ (x.T @ y)  # More stable than manual dot products
    return float(beta[0] + test_dt[0] * beta[1] + test_mtch[0] * beta[2])


def sarimax_predictor(train_user: list[float], train_match: list[float], test_match: list[float]) -> float:
    """
    Use SARIMAX for predicting total users based on training data.
    
    Args:
        train_user: Total users in training data
        train_match: Total matches in training data
        test_match: Total matches for testing data
    
    Returns:
        Predicted total users for the test match.
    """
    simplefilter("ignore", UserWarning)  # Suppress warnings from SARIMAX
    model = SARIMAX(train_user, exog=train_match, order=(1, 2, 1), seasonal_order=(1, 1, 1, 7))
    model_fit = model.fit(disp=False, maxiter=600, method="nm")
    result = model_fit.predict(start=len(train_user), end=len(train_user), exog=[test_match])
    return float(result[0])


def support_vector_regressor(x_train: np.ndarray, x_test: np.ndarray, train_user: list[float]) -> float:
    """
    Predict total users using Support Vector Regressor.
    
    Args:
        x_train: Training features (dates and matches)
        x_test: Testing features (dates and matches)
        train_user: Total users for training data
    
    Returns:
        Predicted total users for the test features.
    """
    regressor = SVR(kernel="rbf", C=1, gamma=0.1, epsilon=0.1)
    regressor.fit(x_train, train_user)
    y_pred = regressor.predict(x_test)
    return float(y_pred[0])


def interquartile_range_checker(train_user: list[float]) -> float:
    """
    Calculate the low limit for detecting outliers using IQR.
    
    Args:
        train_user: List of total users
    
    Returns:
        Low limit for detecting outliers.
    """
    train_user = np.array(train_user)
    q1 = np.percentile(train_user, 25)
    q3 = np.percentile(train_user, 75)
    iqr = q3 - q1
    low_lim = q1 - (iqr * 1.5)  # Common multiplier for outlier detection
    return float(low_lim)


def data_safety_checker(list_vote: list[float], actual_result: float) -> bool:
    """
    Check if the predictions are safe based on actual results.
    
    Args:
        list_vote: List of predictions
        actual_result: Actual result to compare against
    
    Returns:
        True if the data is considered safe; otherwise False.
    """
    if not isinstance(actual_result, float):
        raise TypeError("Actual result should be a float.")

    safe_count = sum(
        1 for prediction in list_vote if abs(prediction - actual_result) <= 0.1
    )
    not_safe_count = len(list_vote) - safe_count
    
    return safe_count > not_safe_count


if __name__ == "__main__":
    # Load data from CSV file
    data_input_df = pd.read_csv("ex_data.csv")

    # Start normalization
    normalize_df = Normalizer().fit_transform(data_input_df.values)
    
    # Split data
    total_user = normalize_df[:, 0].tolist()
    total_match = normalize_df[:, 1].tolist()
    total_date = normalize_df[:, 2].tolist()

    # Prepare data for models
    x = normalize_df[:, [1, 2]]  # Total matches and dates
    x_train = x[:-1]
    x_test = x[-1:]

    train_user = total_user[:-1]
    test_user = total_user[-1:]

    # Forecasting using multiple methods
    res_vote = [
        linear_regression_prediction(train_date, train_user, train_match, total_date[-1:], total_match[-1:]),
        sarimax_predictor(train_user, total_match[:-1], total_match[-1:]),
        support_vector_regressor(x_train, x_test, train_user),
    ]

    # Check the safety of today's data
    is_safe = data_safety_checker(res_vote, test_user[0])
    status = "" if is_safe else "not "
    print(f"Today's data is {status}safe.")
