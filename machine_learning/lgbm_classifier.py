# LGBM Classifier Example
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from lightgbm import LGBMClassifier


def data_handling(data: dict) -> tuple:
    """
    Splits dataset into features and target labels.

    >>> data_handling({'data': '[5.1, 3.5, 1.4, 0.2]', 'target': [0]})
    ('[5.1, 3.5, 1.4, 0.2]', [0])
    >>> data_handling({'data': '[4.9, 3.0, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]', 'target': [0, 0]})
    ('[4.9, 3.0, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]', [0, 0])
    """
    return data["data"], data["target"]


def lgbm_classifier(features: np.ndarray, target: np.ndarray) -> LGBMClassifier:
    """
    Trains an LGBM Classifier on the given features and target labels.

    >>> lgbm_classifier(np.array([[5.1, 3.6, 1.4, 0.2]]), np.array([0]))
    LGBMClassifier()
    """
    classifier = LGBMClassifier()
    classifier.fit(features, target)
    return classifier


def main() -> None:
    """
    Main function to demonstrate LGBM classification on the Iris dataset.

    URL for LightGBM documentation:
    https://lightgbm.readthedocs.io/en/latest/
    """
    # Load the Iris dataset
    iris = load_iris()
    features, targets = data_handling(iris)

    # Split the dataset into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(
        features, targets, test_size=0.25, random_state=42
    )

    # Class names for display
    names = iris["target_names"]

    # Train the LGBM classifier
    lgbm_clf = lgbm_classifier(x_train, y_train)

    # Display the confusion matrix for the classifier
    ConfusionMatrixDisplay.from_estimator(
        lgbm_clf,
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
