# XGBoost Classifier Example
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier


def data_handling(data: dict) -> tuple:
    # Split dataset into train and test data
    x = (data["data"], data["target"], data["target_names"])  # data is features
    return x


def xgboost(
    features: list,
    target: list,
    test_features: list,
    test_targets: list,
    namesofflowers: list,
) -> None:
    classifier = XGBClassifier()
    classifier.fit(features, target)
    # Display Confusion Matrix of Classifier
    # with both train and test sets
    plot_confusion_matrix(
        classifier,
        test_features,
        test_targets,
        display_labels=namesofflowers,
        cmap="Blues",
        normalize="true",
    )
    plt.title("Normalized Confusion Matrix - IRIS Dataset")
    plt.show()


def main() -> None:

    """
    The Url for the algorithm
    https://xgboost.readthedocs.io/en/stable/
    Iris type dataset is used to demonstrate algorithm.
    """

    # Load Iris dataset
    iris = load_iris()

    features, target, names = data_handling(iris)

    x_train, x_test, y_train, y_test = train_test_split(
        features, target, test_size=0.25
    )

    # XGBoost Classifier
    xgboost(x_train, y_train, x_test, y_test, names)


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="main", verbose=True)
    doctest.testmod(name="xgboost", verbose=True)
    doctest.testmod(name="data_handling", verbose=True)
    # main()
