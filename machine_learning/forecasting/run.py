"""
This code forecasts user activity and checks data safety in an online shop context.
It predicts total users based on historical data and checks if the current data is within a safe range.

You can modify it for various forecasting purposes or for different datasets.

Usage:
- Load your data from a CSV file.
- Ensure the CSV has columns for total users, events, and dates.
"""

import logging
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVR
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
from warnings import simplefilter

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path: str) -> pd.DataFrame:
    """Load data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        logging.info("Data loaded successfully.")
        return data
    except FileNotFoundError:
        logging.error("The file was not found.")
        raise
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise


def normalize_data(data: pd.DataFrame) -> np.ndarray:
    """Normalize the input data."""
    return Normalizer().fit_transform(data.values)


def train_test_split_data(normalize_df: np.ndarray) -> tuple:
    """Split the normalized data into training and test sets."""
    total_user = normalize_df[:, 0].tolist()
    total_match = normalize_df[:, 1].tolist()
    total_date = normalize_df[:, 2].tolist()
    
    x = normalize_df[:, [1, 2]].tolist()
    x_train, x_test = train_test_split(x, test_size=0.2, random_state=42)
    
    train_user = total_user[:len(x_train)]
    test_user = total_user[len(x_train):]
    
    return x_train, x_test, train_user, test_user, total_match[:len(x_train)], total_match[len(x_train):], total_date


def linear_regression_prediction(train_dt: list, train_usr: list, train_mtch: list, test_dt: list, test_mtch: list) -> float:
    """Predict total users using linear regression."""
    x = np.array([[1, item, train_mtch[i]] for i, item in enumerate(train_dt)])
    y = np.array(train_usr)
    
    # Compute coefficients using Normal Equation
    beta = np.linalg.inv(x.T @ x) @ x.T @ y
    return float(beta[0] + test_dt[0] * beta[1] + test_mtch[0] * beta[2])


def sarimax_predictor(train_user: list, train_match: list, test_match: list) -> float:
    """Predict total users using SARIMAX."""
    simplefilter("ignore", UserWarning)
    order = (1, 2, 1)
    seasonal_order = (1, 1, 1, 7)  # Weekly seasonality assumed
    
    model = SARIMAX(train_user, exog=train_match, order=order, seasonal_order=seasonal_order)
    model_fit = model.fit(disp=False, maxiter=600, method="nm")
    
    result = model_fit.predict(start=len(train_user), end=len(train_user) + len(test_match) - 1, exog=test_match)
    return float(result[0])


def support_vector_regressor(x_train: list, x_test: list, train_user: list) -> float:
    """Predict total users using Support Vector Regressor."""
    regressor = SVR(kernel="rbf", C=1, gamma=0.1, epsilon=0.1)
    regressor.fit(x_train, train_user)
    y_pred = regressor.predict(x_test)
    return float(y_pred[0])


def data_safety_checker(list_vote: list, actual_result: float) -> bool:
    """Check if predictions are within a safe range compared to the actual result."""
    safe = 0
    not_safe = 0

    if not isinstance(actual_result, (float, int)):
        logging.error("Actual result should be float or int.")
        raise TypeError("Actual result should be float or int.")

    for prediction in list_vote:
        if prediction > actual_result:
            safe += 1
        elif abs(prediction - actual_result) <= 0.1:
            safe += 1
        else:
            not_safe += 1
    return safe > not_safe


def plot_results(res_vote: list, actual: float):
    """Plot the predicted vs actual results."""
    plt.figure(figsize=(10, 5))
    plt.plot(range(len(res_vote)), res_vote, label='Predictions', marker='o')
    plt.axhline(y=actual, color='r', linestyle='-', label='Actual Result')
    plt.title('Predicted vs Actual User Count')
    plt.xlabel('Model')
    plt.ylabel('User Count')
    plt.xticks(range(len(res_vote)), ['Linear Regression', 'SARIMAX', 'SVR'])
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # Load and process data
    data_input_df = load_data("ex_data.csv")
    
    # Normalize data
    normalize_df = normalize_data(data_input_df)

    # Split data into relevant lists
    x_train, x_test, train_user, test_user, train_match, test_match, total_date = train_test_split_data(normalize_df)

    # Voting system with forecasting
    res_vote = [
        linear_regression_prediction(total_date[:len(train_user)], train_user, train_match, total_date[len(train_user):len(train_user)+len(test_user)], test_match),
        sarimax_predictor(train_user, train_match, test_match),
        support_vector_regressor(x_train, x_test, train_user)
    ]

    # Check the safety of today's data
    is_safe = data_safety_checker(res_vote, test_user[0])
    not_str = "" if is_safe else "not "
    logging.info(f"Today's data is {not_str}safe.")

    # Plot the results
    plot_results(res_vote, test_user[0])
