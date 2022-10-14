# XGBoost Regressor Example
from sklearn.datasets import load_boston
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor


def dataset(datatype: dict) -> tuple:
    # Split dataset into train and test data
    x = (datatype["data"], datatype["target"])  # features
    return x


def xgboost(features: list, target: list, test_features: list) -> list:
    xgb = XGBRegressor()
    xgb.fit(features, target)
    # Predict target for test data
    predictions = xgb.predict(test_features)
    predictions = predictions.reshape(len(predictions), 1)
    return predictions


def main() -> None:

    """
    The Url for the algorithm
    https://xgboost.readthedocs.io/en/stable/
    Boston house price dataset is used to demonstrate the algorithm.
    """
    # Load Boston house price dataset
    boston = load_boston()
    print(boston.keys())

    features, target = dataset(boston)
    x_train, x_test, y_train, y_test = train_test_split(
        features, target, test_size=0.25, random_state=1
    )
    predictions = xgboost(x_train, y_train, x_test)

    # Error printing
    print(f"Mean Absolute Error:\t {mean_absolute_error(y_test, predictions)}")
    print(f"Mean Square Error  :\t {mean_squared_error(y_test, predictions)}")


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="main", verbose=True)
    doctest.testmod(name="dataset", verbose=True)
    doctest.testmod(name="xgboost", verbose=True)
    main()
