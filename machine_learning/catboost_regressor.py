# CatBoost Classifier Example
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier


def data_handling(data: dict) -> tuple:
    """
    Extracts the features and target values from the provided dataset.

    Args:
        data (dict): A dictionary containing the dataset's features and targets.

    Returns:
        tuple: A tuple with features and targets.

    Example:
    >>> data_handling({'data':'[5.1, 3.5, 1.4, 0.2]', 'target': [0]})
    ('[5.1, 3.5, 1.4, 0.2]', [0])
    """
    return data["data"], data["target"]


def catboost(features: np.ndarray, target: np.ndarray) -> CatBoostClassifier:
    """
    Trains a CatBoostClassifier using the provided features and target.

    Args:
        features (np.ndarray): The input features for training the classifier.
        target (np.ndarray): The target labels corresponding to the features.

    Returns:
        CatBoostClassifier: A trained CatBoost classifier.

    Example:
    >>> catboost(np.array([[5.1, 3.6, 1.4, 0.2]]), np.array([0]))
    CatBoostClassifier(...)
    """
    classifier = CatBoostClassifier(verbose=0)  # Suppressing verbose output
    classifier.fit(features, target)
    return classifier


def main() -> None:
    """
    Demonstrates the training and evaluation of a CatBoost classifier
    on the Iris dataset, displaying a confusion matrix of the results.

    The dataset is split into training and testing sets, the model is
    trained on the training data, and then evaluated on the test data.
    A normalized confusion matrix is displayed.
    """

    # Load the Iris dataset
    iris = load_iris()
    features, targets = data_handling(iris)
    x_train, x_test, y_train, y_test = train_test_split(
        features, targets, test_size=0.25
    )

    # Train a CatBoost classifier
    catboost_classifier = catboost(x_train, y_train)

    # Display the confusion matrix for the test data
    ConfusionMatrixDisplay.from_estimator(
        catboost_classifier,
        x_test,
        y_test,
        display_labels=iris["target_names"],
        cmap="Blues",
        normalize="true",
    )
    plt.title("Normalized Confusion Matrix - IRIS Dataset")
    plt.show()


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    main()
