import numpy as np
import requests


def collect_dataset():
    """Collect dataset of CSGO
    The dataset contains ADR vs Rating of a Player
    :return: dataset obtained from the link, as a matrix
    """
    response = requests.get(
        "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/master/Week1/ADRvsRating.csv",
        timeout=10,
    )
    data = np.loadtxt(response.text.splitlines()[1:], delimiter=",")  # Skip the header
    return data


def normalize_features(data):
    """Normalize feature values to have mean 0 and variance 1"""
    means = np.mean(data[:, :-1], axis=0)
    stds = np.std(data[:, :-1], axis=0)
    data[:, :-1] = (data[:, :-1] - means) / stds
    return data


def run_steep_gradient_descent(data_x, data_y, len_data, alpha, theta):
    """Run steep gradient descent and updates the Feature vector accordingly
    :param data_x: contains the dataset
    :param data_y: contains the output associated with each data-entry
    :param len_data: length of the data
    :param alpha: Learning rate of the model
    :param theta: Feature vector (weights for our model)
    :return: Updated Features, using curr_features - alpha * gradient(w.r.t. feature)
    """
    n = len_data

    prod = np.dot(theta, data_x.transpose())
    prod -= data_y.transpose()
    sum_grad = np.dot(prod, data_x)
    theta = theta - (alpha / n) * sum_grad
    return theta


def sum_of_square_error(data_x, data_y, len_data, theta):
    """Return sum of square error for error calculation
    :param data_x: contains our dataset
    :param data_y: contains the output (result vector)
    :param len_data: length of the dataset
    :param theta: contains the feature vector
    :return: sum of square error computed from given features
    """
    prod = np.dot(theta, data_x.transpose())
    prod -= data_y.transpose()
    sum_elem = np.sum(np.square(prod))
    error = sum_elem / (2 * len_data)
    return error


def run_linear_regression(data_x, data_y):
    """Implement Linear regression over the dataset
    :param data_x: contains our dataset
    :param data_y: contains the output (result vector)
    :return: feature for the line of best fit (Feature vector)
    """
    iterations = 100000
    alpha = 0.0001550

    no_features = data_x.shape[1]
    len_data = data_x.shape[0]

    theta = np.zeros((1, no_features))
    rng = np.random.default_rng()  # Create a random generator instance

    for i in range(iterations):
        indices = rng.choice(len_data, size=32, replace=False)  # Randomly sample indices using the generator
        x_batch = data_x[indices]
        y_batch = data_y[indices]

        theta = run_steep_gradient_descent(x_batch, y_batch, len(x_batch), alpha, theta)
        error = sum_of_square_error(x_batch, y_batch, len(x_batch), theta)
        print(f"At Iteration {i + 1} - Error is {error:.5f}")

    return theta


def mean_absolute_error(predicted_y, original_y):
    """Return mean absolute error for error calculation
    :param predicted_y: contains the output of prediction (result vector)
    :param original_y: contains values of expected outcome
    :return: mean absolute error computed from given features
    """
    total = sum(abs(y - predicted_y[i]) for i, y in enumerate(original_y))
    return total / len(original_y)


def main():
    """Driver function"""
    data = collect_dataset()
    data = normalize_features(data)  # Normalize the features

    len_data = data.shape[0]
    data_x = np.c_[np.ones(len_data), data[:, :-1]].astype(float)  # Add bias term
    data_y = data[:, -1].astype(float)

    theta = run_linear_regression(data_x, data_y)
    len_result = theta.shape[1]
    print("Resultant Feature vector : ")
    for i in range(len_result):
        print(f"{theta[0, i]:.5f}")


if __name__ == "__main__":
    main()
