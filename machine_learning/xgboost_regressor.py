# XGBoost Regressor Example
from sklearn.datasets import load_boston
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split


def main():

    """
    XGBoost Regressor Example using sklearn function.
    Boston house price dataset is used to demonstrate the algorithm.
    """

    # Load Boston house price dataset
    boston = load_boston()
    print(boston.keys())

    # Split dataset into train and test data
    X = boston["data"]  # features
    Y = boston["target"]
    x_train, x_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.3, random_state=1
    )

    # XGBoost Regressor
    xgb = XGBRegressor(random_state=42, n_estimators=500,learning_rate=0.03)
    xgb.fit(x_train, y_train)

    # Predicting target variable for test set
    predictions = xgb.predict(x_test)
    predictions = predictions.reshape(len(predictions), 1)

    # Printing Errors
    print(f"Mean Absolute Error:\t {mean_absolute_error(y_test, predictions)}")
    print(f"Mean Square Error  :\t {mean_squared_error(y_test, predictions)}")


if __name__ == "__main__":
    main()