"""
Random Forest Classifier Example using sklearn.

This implementation demonstrates the Random Forest classifier
on the Iris dataset with proper visualization using modern sklearn methods.
"""

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score
from sklearn.model_selection import train_test_split


def main() -> None:
    """
    Random Forest classifier example.

    Uses the Iris dataset to demonstrate the algorithm with
    confusion matrix visualization.

    >>> # Test that the model can be created and trained
    >>> iris = load_iris()
    >>> x_train, x_test, y_train, y_test = train_test_split(
    ...     iris.data, iris.target, test_size=0.3, random_state=1
    ... )
    >>> rf_model = RandomForestClassifier(random_state=42, n_estimators=100)
    >>> rf_model.fit(x_train, y_train)
    RandomForestClassifier(random_state=42)
    >>> y_pred = rf_model.predict(x_test)
    >>> accuracy = accuracy_score(y_test, y_pred)
    >>> accuracy > 0.9
    True
    """
    iris = load_iris()

    x_train, x_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.3, random_state=1
    )

    rand_for = RandomForestClassifier(random_state=42, n_estimators=100)
    rand_for.fit(x_train, y_train)
    y_pred = rand_for.predict(x_test)

    disp = ConfusionMatrixDisplay.from_estimator(
        rand_for,
        x_test,
        y_test,
        display_labels=iris.target_names,
        cmap="Blues",
        normalize="true",
    )
    disp.ax_.set_title("Normalized Confusion Matrix - IRIS Dataset")
    disp.figure_.show()

    accuracy = 100 * accuracy_score(y_true=y_test, y_pred=y_pred)
    print(f"The overall accuracy of the model is: {accuracy:.2f}%")


if __name__ == "__main__":
    main()
