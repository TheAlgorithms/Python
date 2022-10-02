"""
Implementation of the XGBoost Classifier.
Dataset - Iris Dataset
Know more about XGBoost - https://en.wikipedia.org/wiki/XGBoost
"""

import warnings

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, confusion_matrix, plot_confusion_matrix
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier  # might have to do `!pip install xgboost`

warnings.filterwarnings("ignore")


def main():
    # load the iris dataset
    iris = load_iris()

    print(type(iris))  # Currently the type is sklearn.utils.Bunch

    # convert it to a dataframe
    df = pd.DataFrame(iris.data, columns=iris.feature_names)

    # add the target column
    df["target"] = iris.target

    print(df["target"].unique())  # 0 -> sentosa, 1 -> versicolor, 2 -> virginica

    # how the dataset looks
    print(df.head())

    X = df.drop("target", axis=1)
    y = df["target"]

    # split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=0
    )

    # initialize the model
    xgb = XGBClassifier(random_state=0)

    # start the training on training set
    xgb.fit(X_train, y_train)

    # get the prediction on testing set
    y_pred = xgb.predict(X_test)

    # calculate the accuracy
    acc = accuracy_score(y_test, y_pred)

    # print the accuracy
    print(f"Accuracy: {round(100 * acc, 2)}%")

    # print the confusion matrix
    print(confusion_matrix(y_test, y_pred))

    # plot the confusion matrix
    plot_confusion_matrix(
        xgb,
        X_test,
        y_test,
        display_labels=iris["target_names"],
        cmap="Blues",
        normalize="true",
    )
    plt.title("Normalized Confusion Matrix - IRIS Dataset")
    plt.show()


if __name__ == "__main__":
    main()
