import numpy as np
import requests


def collect_dataset():
    """
    Collect dataset of CSGO.

    The dataset contains ADR vs Rating of a Player.

    :return: dataset obtained from the link, as a matrix

    Example:
    >>> dataset = collect_dataset()
    >>> dataset.shape
    (100, 2)
    >>> dataset[0, 0]
    75.45
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
    """
    Run steep gradient descent and update the Feature vector accordingly.

    :param data_x: contains the dataset
    :param data_y: contains the output associated with each data-entry
    :param len_data: length of the data
    :param alpha: Learning rate of the model
    :param theta: Feature vector (weights for our model)
    :return: Updated Feature's using curr_features - alpha * gradient(w.r.t. feature)

    Example:
    >>> data_x = np.array([[1, 2], [1, 3], [1, 4]])
    >>> data_y = np.array([3, 4, 5])
    >>> len_data = 3
    >>> alpha = 0.01
    >>> theta = np.array([0, 0])
    >>> updated_theta = run_steep_gradient_descent(data_x, data_y, len_data, alpha, theta)
    >>> updated_theta
    array([0.08, 0.23])
    """
    n = len_data

    prod = np.dot(theta, data_x.transpose())
    prod -= data_y.transpose()
    sum_grad = np.dot(prod, data_x)
    theta = theta - (alpha / n) * sum_grad
    return theta


def sum_of_square_error(data_x, data_y, len_data, theta):
    """
    Return sum of square error for error calculation.

    :param data_x: contains our dataset
    :param data_y: contains the output (result vector)
    :param len_data: length of the dataset
    :param theta: contains the feature vector
    :return: sum of square error computed from given features

    Example:
    >>> data_x = np.array([[1, 2], [1, 3], [1, 4]])
    >>> data_y = np.array([3, 4, 5])
    >>> len_data = 3
    >>> theta = np.array([0.08, 0.23])
    >>> error = sum_of_square_error(data_x, data_y, len_data, theta)
    >>> round(error, 2)
    0.01
    """
    prod = np.dot(theta, data_x.transpose())
    prod -= data_y.transpose()
    sum_elem = np.sum(np.square(prod))
    error = sum_elem / (2 * len_data)
    return error


def run_linear_regression(data_x, data_y):
    """
    Implement Linear regression over the dataset.

    :param data_x: contains our dataset
    :param data_y: contains the output (result vector)
    :return: feature for the line of best fit (Feature vector)

    Example:
    >>> data_x = np.array([[1, 2], [1, 3], [1, 4]])
    >>> data_y = np.array([3, 4, 5])
    >>> theta = run_linear_regression(data_x, data_y)
    >>> theta
    array([0.07, 0.22])
    """
    iterations = 100000
    alpha = 0.0001550

    no_features = data_x.shape[1]
    len_data = data_x.shape[0] - 1

    theta = np.zeros((1, no_features))

    for i in range(iterations):
        theta = run_steep_gradient_descent(
            data_x, data_y, len_data, alpha, theta)
        error = sum_of_square_error(data_x, data_y, len_data, theta)
        print(f"At Iteration {i + 1} - Error is {error:.5f}")

    return theta


def mean_absolute_error(predicted_y, original_y):
    """
    Return mean absolute error for error calculation.

    :param predicted_y: contains the output of prediction (result vector)
    :param original_y: contains values of the expected outcome
    :return: mean absolute error computed from given features

    Example:
    >>> predicted_y = np.array([2, 4, 6])
    >>> original_y = np.array([1, 3, 5])
    >>> error = mean_absolute_error(predicted_y, original_y)
    >>> error
    1.0
    """
    total = sum(abs(y - predicted_y[i]) for i, y in enumerate(original_y))
    return total / len(original_y)


def main():
    """
    Driver function
    """
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
