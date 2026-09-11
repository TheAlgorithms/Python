import numpy as np
import requests


def collect_dataset():
    """Collect dataset of CSGO
    The dataset contains ADR vs Rating of a Player
    :return : dataset obtained from the link, as matrix
    """
    response = requests.get(
        "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/"
        "master/Week1/ADRvsRating.csv",
        timeout=10,
    )
    lines = response.text.splitlines()
    data = []
    for item in lines:
        item = item.split(",")
        data.append(item)
    data.pop(0)  # This is for removing the labels from the list
    dataset = np.matrix(data)
    return dataset


def run_steep_gradient_descent(data_x, data_y, len_data, alpha, theta, lambda_reg):
    """Run steep gradient descent and updates the Feature vector accordingly
    :param data_x   : contains the dataset
    :param data_y   : contains the output associated with each data-entry
    :param len_data : length of the data
    :param alpha    : Learning rate of the model
    :param theta    : Feature vector (weights for our model)
    :param lambda_reg: Regularization parameter
    :return : Updated Features using
              curr_features - alpha_ * gradient(w.r.t. feature)
    """
    n = len_data

    prod = np.dot(theta, data_x.transpose())
    prod -= data_y.transpose()
    sum_grad = np.dot(prod, data_x)

    # Add regularization to the gradient
    theta_regularized = np.copy(theta)
    theta_regularized[0, 0] = 0  # Don't regularize the bias term
    sum_grad += lambda_reg * theta_regularized  # Add regularization to gradient

    theta = theta - (alpha / n) * sum_grad
    return theta


def sum_of_square_error(data_x, data_y, len_data, theta, lambda_reg):
    """Return sum of square error for error calculation
    :param data_x    : contains our dataset
    :param data_y    : contains the output (result vector)
    :param len_data  : len of the dataset
    :param theta     : contains the feature vector
    :param lambda_reg: Regularization parameter
    :return          : sum of square error computed from given features
    """
    prod = np.dot(theta, data_x.transpose())
    prod -= data_y.transpose()
    sum_elem = np.sum(np.square(prod))

    # Add regularization to the cost function
    regularization_term = lambda_reg * np.sum(
        np.square(theta[:, 1:])
    )  # Don't regularize the bias term
    error = (sum_elem / (2 * len_data)) + (regularization_term / (2 * len_data))
    return error


def run_ridge_regression(data_x, data_y, lambda_reg=1.0):
    """Implement Ridge Regression over the dataset
    :param data_x  : contains our dataset
    :param data_y  : contains the output (result vector)
    :param lambda_reg: Regularization parameter
    :return        : feature for line of best fit (Feature vector)
    """
    iterations = 100000
    alpha = 0.0001550

    no_features = data_x.shape[1]
    len_data = data_x.shape[0]

    theta = np.zeros((1, no_features))

    for i in range(iterations):
        theta = run_steep_gradient_descent(
            data_x, data_y, len_data, alpha, theta, lambda_reg
        )
        error = sum_of_square_error(data_x, data_y, len_data, theta, lambda_reg)
        print(f"At Iteration {i + 1} - Error is {error:.5f}")

    return theta


def mean_absolute_error(predicted_y, original_y):
    """Return mean absolute error for error calculation
    :param predicted_y   : contains the output of prediction (result vector)
    :param original_y    : contains values of expected outcome
    :return          : mean absolute error computed from given features
    """
    total = sum(abs(y - predicted_y[i]) for i, y in enumerate(original_y))
    return total / len(original_y)


def main():
    """Driver function"""
    data = collect_dataset()

    len_data = data.shape[0]
    data_x = np.c_[np.ones(len_data), data[:, :-1]].astype(float)
    data_y = data[:, -1].astype(float)

    lambda_reg = 1.0  # Set your desired regularization parameter
    theta = run_ridge_regression(data_x, data_y, lambda_reg)

    len_result = theta.shape[1]
    print("Resultant Feature vector : ")
    for i in range(len_result):
        print(f"{theta[0, i]:.5f}")


if __name__ == "__main__":
    main()
