# Random Forest Classifier Example

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt


def main():

    """
    Random Tree Classifier Example using sklearn function.
    Iris type dataset is used to demonstrate algorithm.
    """

    # Load Iris house price dataset
    iris = load_iris()

    # Split dataset into train and test data
    X = iris["data"]  # features
    Y = iris["target"]
    x_train, x_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.3, random_state=1
    )

    # Random Forest Classifier
    rand_for = RandomForestClassifier(random_state=42, n_estimators=100)
    rand_for.fit(x_train, y_train)

    # Display Confusion Matrix of Classifier
    plot_confusion_matrix(
        rand_for,
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
