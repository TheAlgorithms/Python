"""Implementation of HistGradientBoostingClassifer in sklearn using the
breast cancer dataset"""

from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
import numpy as np


def main():
    # loading the dataset from sklearn.datasets
    df_cancer = load_breast_cancer()
    print(df_cancer.keys())
    X = df_cancer.data
    y = df_cancer.target
    print("number of classes are: ", np.unique(y))
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=0
    )
    # create object of historgradientboosting
    hist = HistGradientBoostingClassifier()
    # training the model
    hist.fit(X_train, y_train)
    y_pred = hist.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("accuracy of the model is: ", accuracy)
    clr = classification_report(y_test, y_pred)
    print("Classification report is:", clr)


if __name__ == "__main__":
    main()
