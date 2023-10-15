import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score
from sklearn.model_selection import train_test_split
import doctest

"""
AdaBoost, short for Adaptive Boosting, is a powerful ensemble learning technique in machine learning.
It operates by combining multiple weak learners, often decision trees, in an iterative manner.
AdaBoost assigns varying weights to data points, prioritizing misclassified samples with each iteration.
"""


def data_handling(data: dict) -> tuple:
    """
    Split dataset into features and target.

    >>> data_handling({'data':'[5.1, 3.5, 1.4, 0.2]','target':([0])})
    ('[5.1, 3.5, 1.4, 0.2]', [0])
    >>> data_handling({'data': '[4.9, 3.0, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]', 'target': ([0, 0])})
    ('[4.9, 3.0, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]', [0, 0])
    """
    return (data["data"], data["target"])


def adaboost(features: np.ndarray, target: np.ndarray) -> AdaBoostClassifier:
    """
    Initialize and train an AdaBoost classifier.

    >>> adaboost(np.array([[5.1, 3.6, 1.4, 0.2]]), np.array([0]))
    AdaBoostClassifier(...)
    """
    classifier = AdaBoostClassifier()
    classifier.fit(features, target)
    return classifier


def main():
    """
    Url for the algorithm:
    https://scikit-learn.org/stable/modules/ensemble.html#adaboost
    Iris type dataset is used to demonstrate the algorithm.
    """

    # Load Iris dataset
    iris = load_iris()
    features, targets = data_handling(iris)
    x_train, x_test, y_train, y_test = train_test_split(
        features, targets, test_size=0.25
    )

    names = iris["target_names"]
    # Creating an AdaBoost Classifier from the training data
    adaboost_classifier = adaboost(x_train, y_train)

    # Making predictions on the test set
    y_pred = adaboost_classifier.predict(x_test)

    # Displaying the accuracy of the AdaBoost classifier
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy of the AdaBoost classifier: {accuracy}")

    # Displaying the confusion matrix of the classifier with both training and test sets
    ConfusionMatrixDisplay.from_estimator(
        adaboost_classifier,  # Use AdaBoost classifier
        x_test,
        y_test,
        display_labels=names,
        cmap="Blues",
        normalize="true",
    )
    plt.title("Normalized Confusion Matrix - IRIS Dataset")
    plt.show()


if __name__ == "__main__":
    doctest.testmod(verbose=True)
    main()
