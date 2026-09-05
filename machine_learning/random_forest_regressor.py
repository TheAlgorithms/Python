# Random Forest Regressor Example
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split


def main():

    """
    Random Forest Regressor Example using sklearn function.
    California housing dataset is used to demonstrate the algorithm.
    """

    # Load California housing dataset
    california = fetch_california_housing()
    print(california.keys())

    # Split dataset into train and test data
    x = california["data"]  # features
    y = california["target"]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=1
    )

    # Random Forest Regressor
    rand_for = RandomForestRegressor(random_state=42, n_estimators=300)
    rand_for.fit(x_train, y_train)

    # Predict target for test data
    predictions = rand_for.predict(x_test)

    # Error printing
    print(f"Mean Absolute Error:\t {mean_absolute_error(y_test, predictions)}")
    print(f"Mean Square Error  :\t {mean_squared_error(y_test, predictions)}")


if __name__ == "__main__":
    main()
