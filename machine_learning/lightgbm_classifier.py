"""Implementation of lightgbm using the breast cancer dataset which is very
popular dataset for classification problem.
 """
from sklearn.datasets import load_breast_cancer
import lightgbm as lgb
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import numpy as np


def model():
    # loading the dataset from sklearn
    df = load_breast_cancer()
    # selection of X and y for train the model
    print(df.keys())
    X, y = df.data, df.target
    print("the number of classes:", np.unique(y))
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1
    )
    classifier = lgb.LGBMClassifier()
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("lightGBM model accuracy socore is:", accuracy)
    # classification report
    clr = classification_report(y_test, y_pred)
    print("classification report is:", clr)


if __name__ == "__main__":
    model()
