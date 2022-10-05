# Multinomial_Naive_Bayes example
# know more about in https://en.wikipedia.org/wiki/Naive_Bayes_classifier

# Packages:

import numpy as np  # Array and matrix math operations
import pandas as pd  # Used for reading CSV files
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.naive_bayes import MultinomialNB # sklearn is liberay for Using Machine learning algorithms

def main() -> None:

    "Dataset used is Iris link-https://archive.ics.uci.edu/ml/datasets/iris"

    # Load Iris dataset:

    # if csv is not stored in the same directory as your python code:
    # iris = pd.read_csv("Enter the loction of your csv file ")# example:  pd.read_csv("E:\iris.csv")

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
    x_train, x_test, y_train, y_test = train_test_split(
        iris[X], iris[Y], test_size=0.3, random_state=0
    )

    # Multinomial_Naive_Bayes
    MNB = MultinomialNB()

    # Building the model
    pred_mnb = MNB.fit(x_train, y_train.values.ravel())

    # Predict target for test data
    predict = pred_mnb.predict(x_test)
    predict = predict.reshape(len(predict), 1)
    
    # the score, or accuracy of the model
    # print(imnb.score(Xtest, ytest))
    print(f"Accuracy of the model:\t {MNB.score(x_test, y_test)}")

    # Confusion matrix MultinomialNB model
    confusion_matrix(y_test, predict)

    print(
        f"Cross Val Accuracy:\t {np.mean(cross_val_score(MNB, x_train, y_train.values.ravel(), cv=10)) }"
    )
    
if __name__ == "__main__":
    main()
    import doctest

    doctest.testmod()
