# XGBoost Classifier Example
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier


def data_handling(data: dict) -> tuple:
    # Split dataset into train and test data
    # data is features
    """
    >>> data_handling(({'data':'[5.1, 3.5, 1.4, 0.2]','target':([0])}))
    ('[5.1, 3.5, 1.4, 0.2],[4.6, 3.4, 1.4, 0.3]', [0, 1])
    >>> data_handling({'data':'[4.9, 3. , 1.4, 0.2],[4.7, 3.2, 1.3, 0.2],[4.6, 3.1, 1.5, 0.2]','target':([0,0, 0])})
    ('[4.9, 3. , 1.4, 0.2],[4.7, 3.2, 1.3, 0.2],[4.6, 3.1, 1.5, 0.2]', [0, 0, 0])
    """
    x = (data["data"], data["target"])
    return x


def xgboost(features: np.ndarray, target: np.ndarray) -> XGBClassifier:
    """
    >>> xgboost(np.array([[5.1, 3.6, 1.4, 0.2],[4.6, 3.4, 1.4, 0.7]]), np.array([1,2]))
    XGBClassifier()
    """
    classifier = XGBClassifier()
    classifier.fit(features, target)
    return classifier


def main() -> None:

    """
    >>> main()

    The Url for the algorithm
    https://xgboost.readthedocs.io/en/stable/
    Iris type dataset is used to demonstrate algorithm.
    """

    # Load Iris dataset
    iris = load_iris()
    features, targets = data_handling(iris)
    x_train, x_test, y_train, y_test = train_test_split(
        features, targets, test_size=0.25
    )

    names = iris["target_names"]

    # XGBoost Classifier
    xgb = xgboost(x_train, y_train)

    # Display Confusion Matrix of Classifier
    # with both train and test sets
    plot_confusion_matrix(
        xgb,
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

    doctest.testmod(name="main", verbose=True)
    doctest.testmod(name="xgboost", verbose=True)
    doctest.testmod(name="data_handling", verbose=True)
    main()
