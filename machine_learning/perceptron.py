import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def usf(val):
    """Unit Step Function"""
    return 1 if val >= 0 else 0


def sign(val):
    """Sign Function"""
    return 1 if val >= 0 else -1


class Perceptron:

    """
    Implementation of a basic Perceptron for LINEARLY solvable problems.
    Input data set: The input data set must be 2-dimensional with [0,1] labels.
    Output: The perceptron maps a test set and calculates overall acuraciy.
    """

    def __init__(self, eta: float = 0.01, epochs: int = 100, bias: int = 1) -> None:
        self.eta = eta
        self.epochs = epochs
        self.bias = bias
        self.theta = 0

    def __repr__(self) -> str:
        return (
            f"Perceptron -> eta: {self.eta} - epocs: {self.epochs} - bias: {self.bias}"
        )

    def fit(self, x, y):
        """fitting the perceptron on given data features X (train set)
        and labels Y to calculate error on"""
        self.activation_function = usf if min(set(y)) == 0 else sign
        self.theta = np.zeros(x.shape[1])
        self.errors = []

        for _ in range(self.epochs):
            # errors per epoch
            n_wrong = 0

            for idx, x_i in enumerate(x):
                # calculate dot product WX
                y_hat = self.activation_function(np.dot(x_i, self.theta) + self.bias)

                # calculating error
                error = y[idx] - y_hat
                if error:
                    # updating weights and bias
                    self.theta += self.eta * error * x_i
                    self.bias += self.eta * error
                    n_wrong += 1

            self.errors.append(n_wrong)

    def predict(self, x) -> np.array:
        """predicting on given data: X"""
        y_pred = []

        # calculate dot product WX
        for x_i in x:
            y_pred.append(self.activation_function(np.dot(x_i, self.theta) + self.bias))

        return y_pred


def main():
    # importing iris data
    iris = datasets.load_iris()

    # creating iris Pandas DF
    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names).iloc[:, 2:]
    iris_df["target"] = iris.target

    # keep only 0/1 classes records
    iris_df = iris_df[iris_df.target.isin([0, 1])]

    x = iris_df.iloc[:, :-1].to_numpy()
    y = iris_df.iloc[:, -1].to_numpy()
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, shuffle=True, random_state=42
    )

    ### INITIALIZE PERCEPTRON AND CALCULATE PERFORMANCES ###
    perceptron = Perceptron(epochs=1000)

    # fitting on training set
    perceptron.fit(x_train, y_train)

    y_pred_test = perceptron.predict(x_test)
    acc_test = accuracy_score(y_test, y_pred_test)

    print(f"Test Accuracy =  {acc_test*100}%")


if __name__ == "__main__":
    main()
