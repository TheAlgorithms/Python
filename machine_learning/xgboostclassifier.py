# XGBoost Classifier Example
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier


def data_handling(data: list) -> tuple[int, str]:
    # Split dataset into train and test data
    x = data["data"]  # features
    y = data["target"]
    return x, y


def xgboost(features: list, target: list):
    classifier = XGBClassifier()
    classifier.fit(features, target)
    return classifier


def main() -> None:

    """
    The Url for the algorithm
    https://xgboost.readthedocs.io/en/stable/
    Iris type dataset is used to demonstrate algorithm.
    """

    # Load Iris dataset
    iris = load_iris()
    features, target = data_handling(iris)
    x_train, x_test, y_train, y_test = train_test_split(
        features, target, test_size=0.25, random_state=1
    )

    # XGBoost Classifier
    xgb = xgboost(x_train, y_train)

    # Display Confusion Matrix of Classifier
    # with both train and test sets
    plot_confusion_matrix(
        xgb,
        x_test,
        y_test,
        display_labels=iris["target_names"],
        cmap="Blues",
        normalize="true",
    )
    plt.title("Normalized Confusion Matrix - IRIS Dataset")
    plt.show()


if __name__ == "__main__":
    main()
