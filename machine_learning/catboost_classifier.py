# Catboost Classifier Example
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier


def data_handling(data: dict) -> tuple:
    # Split dataset into features and target
    # data is features
    """
    >>> data_handling(({'data':'[5.1, 3.5, 1.4, 0.2]','target':([0])}))
    ('[5.1, 3.5, 1.4, 0.2]', [0])
    >>> data_handling(
    ...     {'data': '[4.9, 3.0, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]', 'target': ([0, 0])}
    ... )
    ('[4.9, 3.0, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]', [0, 0])
    """
    return (data["data"], data["target"])


def catboost(features: np.ndarray, target: np.ndarray) -> CatBoostClassifier:
    """
    >>> catboost(np.array([[5.1, 3.6, 1.4, 0.2]]), np.array([0]))
    <catboost.core.CatBoostClassifier object at 0x...>
    """
    classifier = CatBoostClassifier(verbose=0)
    classifier.fit(features, target)
    return classifier


def main() -> None:
    """
    >>> main()

    Url for the algorithm:
    https://catboost.ai/
    Iris type dataset is used to demonstrate algorithm.
    """

    # Load Iris dataset
    iris = load_iris()
    features, targets = data_handling(iris)
    x_train, x_test, y_train, y_test = train_test_split(
        features, targets, test_size=0.25
    )

    names = iris["target_names"]

    # Create a CatBoost Classifier from the training data
    catboost_classifier = catboost(x_train, y_train)

    # Display the confusion matrix of the classifier with both training and test sets
    ConfusionMatrixDisplay.from_estimator(
        catboost_classifier,
        x_test,
        y_test,
        display_labels=names,
        cmap="Blues",
        normalize="true",
    )
    plt.title("Normalized Confusion Matrix - IRIS Dataset (CatBoost)")
    plt.show()


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
