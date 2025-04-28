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
    try:
        response = requests.get(
            "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/"
            "master/Week1/ADRvsRating.csv",
            timeout=10,
        )
        response.raise_for_status()  # Raise an error for failed HTTP requests
        lines = response.text.splitlines()
        data = [line.split(",") for line in lines]
        data.pop(0)  # Remove the labels from the list
        dataset = np.matrix(data)
        return dataset
    except requests.exceptions.RequestException as e:
        print(f"Error fetching dataset: {e}")
        return None  # Return None if dataset fetching fails


def run_steep_gradient_descent(data_x, data_y, len_data, alpha, theta):
    """Run steep gradient descent and updates the Feature vector accordingly_
    :param data_x   : contains the dataset
    :param data_y   : contains the output associated with each data-entry
    :param len_data : length of the data_
    :param alpha    : Learning rate of the model
    :param theta    : Feature vector (weight's for our model)
    ;param return    : Updated Feature's, using
                       curr_features - alpha_ * gradient(w.r.t. feature)
    >>> import numpy as np
    >>> data_x = np.array([[1, 2], [3, 4]])
    >>> data_y = np.array([5, 6])
    >>> len_data = len(data_x)
    >>> alpha = 0.01
    >>> theta = np.array([0.1, 0.2])
    >>> run_steep_gradient_descent(data_x, data_y, len_data, alpha, theta)
    array([0.196, 0.343])
    """
    try:
        prod = np.dot(theta, data_x.transpose()) - data_y.transpose()
        sum_grad = np.dot(prod, data_x)
        theta = theta - (alpha / len_data) * sum_grad
        return theta
    except (TypeError, ValueError) as e:
        print(f"Error in gradient descent: {e}")
        return theta


def sum_of_square_error(data_x, data_y, len_data, theta):
    """Return sum of square error for error calculation
    :param data_x    : contains our dataset
    :param data_y    : contains the output (result vector)
    :param len_data  : len of the dataset
    :param theta     : contains the feature vector
    :return          : sum of square error computed from given feature's

    Example:
    >>> vc_x = np.array([[1.1], [2.1], [3.1]])
    >>> vc_y = np.array([1.2, 2.2, 3.2])
    >>> round(sum_of_square_error(vc_x, vc_y, 3, np.array([1])),3)
    np.float64(0.005)
    """
    try:
        prod = np.dot(theta, data_x.transpose()) - data_y.transpose()
        sum_elem = np.sum(np.square(prod))
        error = sum_elem / (2 * len_data)
        return error
    except (TypeError, ValueError) as e:
        print(f"Error in calculating sum of square error: {e}")
        return float("inf")


def run_linear_regression(data_x, data_y):
    """Implement Linear regression over the dataset
    :param data_x  : contains our dataset
    :param data_y  : contains the output (result vector)
    :return        : feature for line of best fit (Feature vector)
    """
    iterations = 100000
    alpha = 0.0001550
    len_data = data_x.shape[0] - 1
    no_features = data_x.shape[1]
    theta = np.zeros((1, no_features))

    try:
        for i in range(iterations):
            theta = run_steep_gradient_descent(data_x, data_y, len_data, alpha, theta)
            error = sum_of_square_error(data_x, data_y, len_data, theta)
            print(f"At Iteration {i + 1} - Error is {error:.5f}")
    except (OverflowError, ValueError) as e:
        print(f"Error during linear regression: {e}")
    return theta


def mean_absolute_error(predicted_y, original_y):
    """Return sum of square error for error calculation
    :param predicted_y   : contains the output of prediction (result vector)
    :param original_y    : contains values of expected outcome
    :return          : mean absolute error computed from given feature's

    >>> predicted_y = [3, -0.5, 2, 7]
    >>> original_y = [2.5, 0.0, 2, 8]
    >>> mean_absolute_error(predicted_y, original_y)
    0.5
    """
    try:
        total = sum(abs(y - predicted_y[i]) for i, y in enumerate(original_y))
        return total / len(original_y)
    except (TypeError, ZeroDivisionError) as e:
        print(f"Error in calculating mean absolute error: {e}")
        return float("inf")


def main():
    """Driver function."""
    data = collect_dataset()
    if data is None:
        print("Failed to retrieve dataset. Exiting.")
        return

    try:
        len_data = data.shape[0]
        data_x = np.c_[np.ones(len_data), data[:, :-1]].astype(float)
        data_y = data[:, -1].astype(float)

        theta = run_linear_regression(data_x, data_y)
        len_result = theta.shape[1]
        print("Resultant Feature vector : ")
        for i in range(len_result):
            print(f"{theta[0, i]:.5f}")
    except (IndexError, TypeError) as e:
        print(f"Error in main execution: {e}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
