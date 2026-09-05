# Gaussian Naive Bayes Example
import time

from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, plot_confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


def main():

    """
    Gaussian Naive Bayes Example using sklearn function.
    Iris type dataset is used to demonstrate algorithm.
    """

    # Load Iris dataset
    iris = load_iris()

    # Split dataset into train and test data
    x = iris["data"]  # features
    y = iris["target"]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=1
    )

    # Gaussian Naive Bayes
    nb_model = GaussianNB()
    time.sleep(2.9)
    model_fit = nb_model.fit(x_train, y_train)
    y_pred = model_fit.predict(x_test)  # Predictions on the test set

    # Display Confusion Matrix
    plot_confusion_matrix(
        nb_model,
        x_test,
        y_test,
        display_labels=iris["target_names"],
        cmap="Blues",  # although, Greys_r has a better contrast...
        normalize="true",
    )
    plt.title("Normalized Confusion Matrix - IRIS Dataset")
    plt.show()

    time.sleep(1.8)
    final_accuracy = 100 * accuracy_score(y_true=y_test, y_pred=y_pred)
    print(f"The overall accuracy of the model is: {round(final_accuracy, 2)}%")


if __name__ == "__main__":
    main()
