# XGBoost Classifier Example
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier


def data_handling(data: dict) -> tuple:
    """
    Split dataset into features and target.

    >>> from sklearn.datasets import load_iris
    >>> iris = load_iris()
    >>> features, targets = data_handling(iris)
    >>> features.shape
    (150, 4)
    >>> targets.shape
    (150,)
    """
    return (data["data"], data["target"])


def xgboost(features: np.ndarray, target: np.ndarray) -> XGBClassifier:
    """
    Train an XGBoost classifier.

    >>> from sklearn.datasets import load_iris
    >>> iris = load_iris()
    >>> X_train, y_train = iris.data[:100], iris.target[:100]
    >>> classifier = xgboost(X_train, y_train)
    >>> predictions = classifier.predict(iris.data[:5])
    >>> len(predictions)
    5
    >>> all(pred in [0, 1, 2] for pred in predictions)
    True
    """
    classifier = XGBClassifier()
    classifier.fit(features, target)
    return classifier


def main() -> None:
    """
    Url for the algorithm:
    https://xgboost.readthedocs.io/en/stable/
    Iris type dataset is used to demonstrate algorithm.
    """
    # Load Iris dataset
    iris = load_iris()
    features, targets = data_handling(iris)
    x_train, x_test, y_train, y_test = train_test_split(
        features, targets, test_size=0.25, random_state=42
    )
    names = iris["target_names"]

    # Create an XGBoost Classifier from the training data
    xgboost_classifier = xgboost(x_train, y_train)

    # Display the confusion matrix of the classifier with test set
    ConfusionMatrixDisplay.from_estimator(
        xgboost_classifier,
        x_test,
        y_test,
        display_labels=names,
        cmap="Blues",
        normalize="true",
    )
    plt.title("Normalized Confusion Matrix - IRIS Dataset")
    plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
