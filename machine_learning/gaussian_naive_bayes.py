# # Gaussian Naive Bayes Example
# import time

# from matplotlib import pyplot as plt
# from sklearn.datasets import load_iris
# from sklearn.metrics import accuracy_score, plot_confusion_matrix
# from sklearn.model_selection import train_test_split
# from sklearn.naive_bayes import GaussianNB


# def main():

#     """
#     Gaussian Naive Bayes Example using sklearn function.
#     Iris type dataset is used to demonstrate algorithm.
#     """

#     # Load Iris dataset
#     iris = load_iris()

#     # Split dataset into train and test data
#     x = iris["data"]  # features
#     y = iris["target"]
#     x_train, x_test, y_train, y_test = train_test_split(
#         x, y, test_size=0.3, random_state=1
#     )

#     # Gaussian Naive Bayes
#     nb_model = GaussianNB()
#     time.sleep(2.9)
#     model_fit = nb_model.fit(x_train, y_train)
#     y_pred = model_fit.predict(x_test)  # Predictions on the test set

#     # Display Confusion Matrix
#     plot_confusion_matrix(
#         nb_model,
#         x_test,
#         y_test,
#         display_labels=iris["target_names"],
#         cmap="Blues",  # although, Greys_r has a better contrast...
#         normalize="true",
#     )
#     plt.title("Normalized Confusion Matrix - IRIS Dataset")
#     plt.show()

#     time.sleep(1.8)
#     final_accuracy = 100 * accuracy_score(y_true=y_test, y_pred=y_pred)
#     print(f"The overall accuracy of the model is: {round(final_accuracy, 2)}%")


# if __name__ == "__main__":
#     main()


import time
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix


class GaussianNaiveBayes:
    def fit(self, X, y):
        self.classes = np.unique(y)
        self.parameters = []
        for c in self.classes:
            X_c = X[y == c]
            self.parameters.append(
                {
                    "mean": X_c.mean(axis=0),
                    "var": X_c.var(axis=0),
                    "prior": len(X_c) / len(X),
                }
            )

    def _calculate_likelihood(self, mean, var, x):
        return (1 / np.sqrt(2 * np.pi * var)) * np.exp(-((x - mean) ** 2) / (2 * var))

    def _calculate_posterior(self, x):
        posteriors = []
        for i, c in enumerate(self.classes):
            prior = np.log(self.parameters[i]["prior"])
            likelihood = np.sum(
                np.log(
                    self._calculate_likelihood(
                        self.parameters[i]["mean"], self.parameters[i]["var"], x
                    )
                )
            )
            posterior = prior + likelihood
            posteriors.append(posterior)
        return self.classes[np.argmax(posteriors)]

    def predict(self, X):
        y_pred = [self._calculate_posterior(x) for x in X]
        return np.array(y_pred)


def main():
    # Load Iris dataset
    iris = load_iris()

    # Split dataset into train and test data
    x = iris["data"]  # features
    y = iris["target"]

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=1
    )

    # Gaussian Naive Bayes
    nb_model = GaussianNaiveBayes()
    time.sleep(2.9)
    nb_model.fit(x_train, y_train)
    y_pred = nb_model.predict(x_test)  # Predictions on the test set

    # Display Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.imshow(cm, interpolation="nearest", cmap=plt.cm.Blues)
    plt.title("Normalized Confusion Matrix - IRIS Dataset")
    plt.colorbar()
    plt.xticks(np.arange(len(iris.target_names)), iris.target_names, rotation=45)
    plt.yticks(np.arange(len(iris.target_names)), iris.target_names)
    plt.tight_layout()
    plt.ylabel("True label")
    plt.xlabel("Predicted label")
    plt.show()

    # Calculate accuracy
    time.sleep(1.8)
    accuracy = (y_test == y_pred).mean()
    print(f"The overall accuracy of the model is: {round(accuracy * 100, 2)}%")


if __name__ == "__main__":
    main()
