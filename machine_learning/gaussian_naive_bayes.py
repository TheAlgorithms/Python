"""
Gaussian Naive Bayes Example using sklearn.

This implementation demonstrates the Gaussian Naive Bayes classifier
on the Iris dataset with proper visualization using modern sklearn methods.
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


def main() -> None:
    """
    Gaussian Naive Bayes classifier example.

    Uses the Iris dataset to demonstrate the algorithm with
    confusion matrix visualization.

    >>> # Test that the model can be created and trained
    >>> iris = load_iris()
    >>> x_train, x_test, y_train, y_test = train_test_split(
    ...     iris.data, iris.target, test_size=0.3, random_state=1
    ... )
    >>> nb_model = GaussianNB()
    >>> nb_model.fit(x_train, y_train)
    GaussianNB()
    >>> y_pred = nb_model.predict(x_test)
    >>> accuracy = accuracy_score(y_test, y_pred)
    >>> accuracy > 0.9
    True
    """
    iris = load_iris()

    x_train, x_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.3, random_state=1
    )

    nb_model = GaussianNB()
    nb_model.fit(x_train, y_train)
    y_pred = nb_model.predict(x_test)

    disp = ConfusionMatrixDisplay.from_estimator(
        nb_model,
        x_test,
        y_test,
        display_labels=iris.target_names,
        cmap="Blues",
        normalize="true",
    )
    disp.ax_.set_title("Normalized Confusion Matrix - IRIS Dataset")
    disp.figure_.show()

    final_accuracy = 100 * accuracy_score(y_true=y_test, y_pred=y_pred)
    print(f"The overall accuracy of the model is: {final_accuracy:.2f}%")


if __name__ == "__main__":
    main()
