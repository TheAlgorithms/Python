# Multinomial_Naive_Bayes example
# know more about in https://en.wikipedia.org/wiki/Naive_Bayes_classifier

# Packages:

import numpy as np  # Array and matrix math operations
import pandas as pd  # Used for reading CSV files
from sklearn import metrics
from sklearn.metrics import confusion_matrix, mean_absolute_error, mean_squared_error
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.naive_bayes import (  # sklearn is liberay for Using Machine learning algorithms
    MultinomialNB,
)


def main():

    "Dataset used is Iris link-https://archive.ics.uci.edu/ml/datasets/iris"

    # Load Iris dataset:

    # if csv is not stored in the same directory as your python code:
    # iris = pd.read_csv("Enter the loction of your csv file ")# example:  pd.read_csv("E:\\Bokey\\Excelr Data\\Python Codes\\all_py\\KNN\\iris.csv")

    # else:
    iris = pd.read_csv("iris.csv")

    X = [
        "Sepal.Length",
        "Sepal.Width",
        "Petal.Length",
        "Petal.Width",
    ]  # X is the inputs
    Y = ["Species"]  # Y is the outputs

    # Splitting data into train and test
    Xtrain, Xtest, ytrain, ytest = train_test_split(
        iris[X], iris[Y], test_size=0.3, random_state=0
    )  # Test_size:Out of 100 % data we split 30 % for testing  & random_state : controls the shuffling process

    # Multinomial_Naive_Bayes
    MNB = MultinomialNB()

    # Building the model
    PRED_mnb = MNB.fit(Xtrain, ytrain.values.ravel())

    # Predict target for test data
    predict = PRED_mnb.predict(Xtest)
    predict = predict.reshape(len(predict), 1)

    # the score, or accuracy of the model
    # print(imnb.score(Xtest, ytest))
    print(f"Accuracy of the model:\t {MNB.score(Xtest, ytest)}")

    # Confusion matrix MultinomialNB model
    confusion_matrix(ytest, predict)

    print(
        f"Cross Val Accuracy:\t {np.mean(cross_val_score(MNB, Xtrain, ytrain.values.ravel(), cv=10)) }"
    )


if __name__ == "__main__":
    main()
