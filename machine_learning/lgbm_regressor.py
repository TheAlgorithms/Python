# LGBM Regressor Example using Bank Marketing Dataset
import numpy as np
from lightgbm import LGBMRegressor
from sklearn.datasets import fetch_openml
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split


def data_handling(data: dict) -> tuple:
    # Split dataset into features and target. Data is features.
    """
    >>> data_handling((
    ...  {'data':'[0.12, 0.02, 0.01, 0.25, 0.09]',
    ...  'target':([1])}))
    ('[0.12, 0.02, 0.01, 0.25, 0.09]', [1])
    """
    return (data["data"], data["target"])


def lgbm_regressor(
    features: np.ndarray, target: np.ndarray, test_features: np.ndarray
) -> np.ndarray:
    """
    >>> lgbm_regressor(np.array([[0.12, 0.02, 0.01, 0.25, 0.09]]),
    ... np.array([1]), np.array([[0.11, 0.03, 0.02, 0.28, 0.08]]))
    array([[0.98]], dtype=float32)
    """
    lgbm = LGBMRegressor(random_state=42)
    lgbm.fit(features, target)
    # Predict target for test data
    predictions = lgbm.predict(test_features)
    predictions = predictions.reshape(len(predictions), 1)
    return predictions


def main() -> None:
    """
    The URL for this algorithm:
    https://lightgbm.readthedocs.io/en/latest/
    Bank Marketing Dataset is used to demonstrate the algorithm.
    """
    # Load Bank Marketing dataset
    bank_data = fetch_openml(name="bank-marketing", version=1, as_frame=False)
    data, target = data_handling(bank_data)
    x_train, x_test, y_train, y_test = train_test_split(
        data, target, test_size=0.25, random_state=1
    )
    predictions = lgbm_regressor(x_train, y_train, x_test)
    # Error printing
    print(f"Mean Absolute Error: {mean_absolute_error(y_test, predictions)}")
    print(f"Mean Square Error: {mean_squared_error(y_test, predictions)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
