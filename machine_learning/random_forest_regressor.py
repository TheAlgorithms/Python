# Random Forest Regressor Example

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error


def main():

    """
    Random Tree Regressor Example using sklearn function.
    Boston house price dataset is used to demonstrate algorithm.
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

    # Random Forest Regressor
    rand_for = RandomForestRegressor(random_state=42, n_estimators=300)
    rand_for.fit(x_train, y_train)

    # Predict target for test data
    predictions = rand_for.predict(x_test)
    predictions = predictions.reshape(len(predictions), 1)

    # Error printing
    print(f"Mean Absolute Error:\t {mean_absolute_error(y_test, predictions)}")
    print(f"Mean Square Error  :\t {mean_squared_error(y_test, predictions)}")


if __name__ == "__main__":
    main()
