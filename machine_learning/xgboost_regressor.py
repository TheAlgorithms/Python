import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor


def load_data():
    """
    Load the California housing dataset and return features and target.
    """
    california = fetch_california_housing()
    return california.data, california.target


def train_xgboost_model(features, target):
    """
    Train an XGBoost Regressor model on the given features and target.
    """
    x_train, x_test, y_train, y_test = train_test_split(
        features, target, test_size=0.25, random_state=1
    )

    xgb = XGBRegressor(verbosity=0, random_state=42, tree_method="exact", base_score=0.5)
    xgb.fit(x_train, y_train)

    predictions = xgb.predict(x_test)
    return predictions, y_test


def evaluate_model(predictions, true_values):
    """
    Evaluate the model and print Mean Absolute Error and Mean Squared Error.
    """
    mae = mean_absolute_error(true_values, predictions)
    mse = mean_squared_error(true_values, predictions)
    print(f"Mean Absolute Error: {mae}")
    print(f"Mean Squared Error: {mse}")


def main():
    features, target = load_data()
    predictions, true_values = train_xgboost_model(features, target)
    evaluate_model(predictions, true_values)


if __name__ == "__main__":
    main()
