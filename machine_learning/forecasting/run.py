"""
This code forecasts user activity and checks data safety in an online shop context.
It predicts total users based on historical data and checks if the current data is within a safe range.
It utilizes various machine learning models and evaluates their performance.

Usage:
- Load your data from a CSV file via command-line argument.
- Ensure the CSV has columns for total users, events, and dates.
"""

import logging
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from warnings import simplefilter
import joblib
import argparse

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Hyperparameters
CONFIG = {
    "svr": {"kernel": "rbf", "C": 1, "gamma": 0.1, "epsilon": 0.1},
    "random_forest": {"n_estimators": 100, "max_depth": None, "min_samples_split": 2},
    "xgboost": {"n_estimators": 100, "learning_rate": 0.1, "max_depth": 3},
    "sarimax_order": (1, 2, 1),
    "sarimax_seasonal_order": (1, 1, 1, 7),  # Weekly seasonality
}


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


def feature_engineering(data: pd.DataFrame) -> pd.DataFrame:
    """Create new features from the existing data."""
    data["day_of_week"] = pd.to_datetime(data["date"]).dt.dayofweek
    data["week_of_year"] = pd.to_datetime(data["date"]).dt.isocalendar().week
    return data


def train_test_split_data(normalize_df: np.ndarray) -> tuple:
    """Split the normalized data into training and test sets."""
    total_user = normalize_df[:, 0].tolist()
    total_match = normalize_df[:, 1].tolist()
    total_date = normalize_df[:, 2].tolist()

    x = normalize_df[:, [1, 2]].tolist()
    x_train, x_test = train_test_split(x, test_size=0.2, random_state=42)

    train_user = total_user[: len(x_train)]
    test_user = total_user[len(x_train) :]

    return (
        x_train,
        x_test,
        train_user,
        test_user,
        total_match[: len(x_train)],
        total_match[len(x_train) :],
        total_date,
    )


def linear_regression_prediction(
    train_dt: list, train_usr: list, train_mtch: list, test_dt: list, test_mtch: list
) -> float:
    """Predict total users using linear regression."""
    x = np.array([[1, item, train_mtch[i]] for i, item in enumerate(train_dt)])
    y = np.array(train_usr)

    # Compute coefficients using Normal Equation
    beta = np.linalg.inv(x.T @ x) @ x.T @ y
    return float(beta[0] + test_dt[0] * beta[1] + test_mtch[0] * beta[2])


def sarimax_predictor(train_user: list, train_match: list, test_match: list) -> float:
    """Predict total users using SARIMAX."""
    simplefilter("ignore", UserWarning)

    model = SARIMAX(
        train_user,
        exog=train_match,
        order=CONFIG["sarimax_order"],
        seasonal_order=CONFIG["sarimax_seasonal_order"],
    )
    model_fit = model.fit(disp=False, maxiter=600, method="nm")

    result = model_fit.predict(
        start=len(train_user),
        end=len(train_user) + len(test_match) - 1,
        exog=test_match,
    )
    return float(result[0])


def support_vector_regressor(x_train: list, x_test: list, train_user: list) -> float:
    """Predict total users using Support Vector Regressor."""
    regressor = SVR(**CONFIG["svr"])
    regressor.fit(x_train, train_user)
    y_pred = regressor.predict(x_test)
    return float(y_pred[0])


def random_forest_regressor(x_train: list, x_test: list, train_user: list) -> float:
    """Predict total users using Random Forest Regressor."""
    model = RandomForestRegressor(**CONFIG["random_forest"])
    model.fit(x_train, train_user)
    return model.predict(x_test)[0]


def xgboost_regressor(x_train: list, x_test: list, train_user: list) -> float:
    """Predict total users using XGBoost Regressor."""
    model = XGBRegressor(**CONFIG["xgboost"])
    model.fit(x_train, train_user)
    return model.predict(x_test)[0]


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


def evaluate_predictions(actual: list, predictions: list):
    """Evaluate model predictions using various metrics."""
    mse = mean_squared_error(actual, predictions)
    mae = mean_absolute_error(actual, predictions)
    r2 = r2_score(actual, predictions)
    logging.info(f"Evaluation Metrics:\nMSE: {mse}\nMAE: {mae}\nR²: {r2}")


def plot_results(res_vote: list, actual: float):
    """Plot the predicted vs actual results."""
    plt.figure(figsize=(10, 5))
    plt.plot(range(len(res_vote)), res_vote, label="Predictions", marker="o")
    plt.axhline(y=actual, color="r", linestyle="-", label="Actual Result")
    plt.title("Predicted vs Actual User Count")
    plt.xlabel("Model")
    plt.ylabel("User Count")
    plt.xticks(
        range(len(res_vote)),
        ["Linear Regression", "SARIMAX", "SVR", "Random Forest", "XGBoost"],
    )
    plt.legend()
    plt.show()


def save_model(model, filename):
    """Save the trained model to a file."""
    joblib.dump(model, filename)
    logging.info(f"Model saved to {filename}.")


if __name__ == "__main__":
    # Argument parser for command line execution
    parser = argparse.ArgumentParser(
        description="User Activity Forecasting and Safety Checker"
    )
    parser.add_argument(
        "file_path", type=str, help="Path to the CSV file containing the data"
    )
    args = parser.parse_args()

    # Load and process data
    data_input_df = load_data(args.file_path)

    # Feature Engineering
    data_input_df = feature_engineering(data_input_df)

    # Normalize data
    normalize_df = normalize_data(data_input_df)

    # Split data into relevant lists
    x_train, x_test, train_user, test_user, train_match, test_match, total_date = (
        train_test_split_data(normalize_df)
    )

    # Voting system with forecasting
    res_vote = [
        linear_regression_prediction(
            total_date[: len(train_user)],
            train_user,
            train_match,
            total_date[len(train_user) : len(train_user) + len(test_user)],
            test_match,
        ),
        sarimax_predictor(train_user, train_match, test_match),
        support_vector_regressor(x_train, x_test, train_user),
        random_forest_regressor(x_train, x_test, train_user),
        xgboost_regressor(x_train, x_test, train_user),
    ]

    # Evaluate predictions
    evaluate_predictions(test_user, res_vote)

    # Check the safety of today's data
    is_safe = data_safety_checker(res_vote, test_user[0])
    not_str = "" if is_safe else "not "
    logging.info(f"Today's data is {not_str}safe.")

    # Plot the results
    plot_results(res_vote, test_user[0])

    # Save models for future use
    save_model(support_vector_regressor, "svr_model.joblib")
    save_model(RandomForestRegressor(**CONFIG["random_forest"]), "rf_model.joblib")
    save_model(XGBRegressor(**CONFIG["xgboost"]), "xgb_model.joblib")
