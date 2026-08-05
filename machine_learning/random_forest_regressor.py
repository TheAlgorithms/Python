"""
Random Forest Regressor Example using sklearn.

This implementation demonstrates the Random Forest regressor
on the California housing dataset with visualization.
"""

import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def main() -> None:
    """
    Random Forest regressor example.

    Uses the California housing dataset to demonstrate the algorithm.

    >>> # Test that the model can be created and trained
    >>> housing = fetch_california_housing()
    >>> x_train, x_test, y_train, y_test = train_test_split(
    ...     housing.data, housing.target, test_size=0.25, random_state=0
    ... )
    >>> model = RandomForestRegressor(n_estimators=100, random_state=42)
    >>> model.fit(x_train, y_train)
    RandomForestRegressor(random_state=42)
    >>> y_pred = model.predict(x_test)
    >>> r2 = r2_score(y_test, y_pred)
    >>> r2 > 0.7
    True
    """
    housing = fetch_california_housing()

    x_train, x_test, y_train, y_test = train_test_split(
        housing.data, housing.target, random_state=0, test_size=0.25
    )

    model = RandomForestRegressor(
        n_estimators=100, max_depth=10, min_samples_split=4, random_state=42
    )
    model.fit(x_train, y_train)

    training_score = model.score(x_train, y_train)
    test_score = model.score(x_test, y_test)
    print(f"Training score of RandomForest: {training_score:.3f}")
    print(f"Test score of RandomForest: {test_score:.3f}")

    y_pred = model.predict(x_test)

    print(f"Mean squared error: {mean_squared_error(y_test, y_pred):.2f}")
    print(f"Test R² score: {r2_score(y_test, y_pred):.2f}")

    _fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred, edgecolors=(0, 0, 0), alpha=0.4)
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--", lw=3)
    ax.set_xlabel("Actual")
    ax.set_ylabel("Predicted")
    ax.set_title("Actual vs Predicted - California Housing")
    plt.show()


if __name__ == "__main__":
    main()
