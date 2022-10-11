# Random Forest Classifier Example
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import GridSearchCV, train_test_split


def main():

    """
    Random Forest Classifier Example using sklearn function.
    Iris type dataset is used to demonstrate algorithm.
    """

    # Load Iris dataset
    iris = load_iris()

    # Split dataset into train and test data
    X = iris["data"]  # features
    Y = iris["target"]
    x_train, x_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.3, random_state=1
    )

    # Random Forest Classifier
    rand_for = RandomForestClassifier(random_state=42)

    # various hyperparameters
    randomgrid = {
        "n_estimators": np.arange(100, 500, 40),
        "max_depth": [None, 10, 20, 30],
        "min_samples_split": [2, 6],
        "min_samples_leaf": [2, 4],
    }

    # using GridSearchCV to improve our model
    np.random.seed(43)
    gs_random = GridSearchCV(rand_for, randomgrid, cv=5, verbose=1, n_jobs=-1)
    gs_random.fit(x_train, y_train)

    # Display Confusion Matrix of Classifier
    plot_confusion_matrix(
        gs_random,
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
