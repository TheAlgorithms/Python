"""
Linear regression is the most basic type of regression commonly used for
predictive analysis. The idea is pretty simple: we have a dataset and we have
features associated with it. Features should be chosen very cautiously
as they determine how much our model will be able to make future predictions.
We try to set the weight of these features, over many iterations, so that they best
fit our dataset. In this particular code, I had used a CSGO dataset (ADR vs
Rating). We try to best fit a line through dataset and estimate the parameters.
"""

import numpy as np
import requests


def collect_dataset():
    """Collect dataset of CSGO
    The dataset contains ADR vs Rating of a Player
    :return : dataset obtained from the link, as matrix
    """
    response = requests.get(
        "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/"
        "master/Week1/ADRvsRating.csv"
    )
    lines = response.text.splitlines()
    data = []
    for item in lines:
        item = item.split(",")
        data.append(item)
    data.pop(0)  # This is for removing the labels from the list
    dataset = np.matrix(data)
    return dataset


def run_steep_gradient_descent(data_x, data_y, len_data, alpha, theta):
    """Run steep gradient descent and updates the Feature vector accordingly_
    :param data_x   : contains the dataset
    :param data_y   : contains the output associated with each data-entry
    :param len_data : length of the data_
    :param alpha    : Learning rate of the model
    :param theta    : Feature vector (weight's for our model)
    ;param return    : Updated Feature's, using
                       curr_features - alpha_ * gradient(w.r.t. feature)
    """
    n = len_data

    prod = np.dot(theta, data_x.transpose())
    prod -= data_y.transpose()
    sum_grad = np.dot(prod, data_x)
    theta = theta - (alpha / n) * sum_grad
    return theta


def sum_of_square_error(data_x, data_y, len_data, theta):
    """Return sum of square error for error calculation
    :param data_x    : contains our dataset
    :param data_y    : contains the output (result vector)
    :param len_data  : len of the dataset
    :param theta     : contains the feature vector
    :return          : sum of square error computed from given feature's
    """
    prod = np.dot(theta, data_x.transpose())
    prod -= data_y.transpose()
    sum_elem = np.sum(np.square(prod))
    error = sum_elem / (2 * len_data)
    return error


def run_linear_regression(data_x, data_y):
    """Implement Linear regression over the dataset
    :param data_x  : contains our dataset
    :param data_y  : contains the output (result vector)
    :return        : feature for line of best fit (Feature vector)
    """
    iterations = 100000
    alpha = 0.0001550

    no_features = data_x.shape[1]
    len_data = data_x.shape[0] - 1

    theta = np.zeros((1, no_features))

    for i in range(iterations):
        theta = run_steep_gradient_descent(data_x, data_y, len_data, alpha, theta)
        error = sum_of_square_error(data_x, data_y, len_data, theta)
        print(f"At Iteration {i + 1} - Error is {error:.5f}")

    return theta


def mean_absolute_error(predicted_y, original_y):
    """Return sum of square error for error calculation
    :param predicted_y   : contains the output of prediction (result vector)
    :param original_y    : contains values of expected outcome
    :return          : mean absolute error computed from given feature's
    """
    total = sum(abs(y - predicted_y[i]) for i, y in enumerate(original_y))
    return total / len(original_y)


def main():
    """Driver function"""
    data = collect_dataset()

    len_data = data.shape[0]
    data_x = np.c_[np.ones(len_data), data[:, :-1]].astype(float)
    data_y = data[:, -1].astype(float)

    theta = run_linear_regression(data_x, data_y)
    len_result = theta.shape[1]
    print("Resultant Feature vector : ")
    for i in range(len_result):
        print(f"{theta[0, i]:.5f}")


if __name__ == "__main__":
    main()
