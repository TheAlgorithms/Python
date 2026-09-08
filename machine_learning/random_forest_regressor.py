# Random Forest Regressor Example

from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split


def main():
    """
    Random Forest Regressor Example using sklearn function.
    The diabetes dataset is used to demonstrate the algorithm.

    Note: this example previously used the Boston house-price dataset,
    which was removed from scikit-learn (>=1.2) for ethical reasons.
    ``load_diabetes`` is a drop-in bundled alternative that ships with
    scikit-learn, so the example runs offline.
    """
    # Load the diabetes dataset
    diabetes = load_diabetes()
    print(diabetes.keys())

    # Split dataset into train and test data
    x = diabetes["data"]  # features
    y = diabetes["target"]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=1
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
