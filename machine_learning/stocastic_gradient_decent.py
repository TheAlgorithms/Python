"""
Implementation of stochastic gradient decent algorithm for minimizing cost
of a Mean Square Error function [MSE]
For Further Reading see https://en.wikipedia.org/wiki/Stochastic_gradient_descent
"""
from typing import Tuple

import numpy as np

"""
function looks like y = w_0 + w_1 * x [For a single Feature[Column]]
"""


def generate_data(seed: int, takeout: int) -> Tuple:
    """
    param seed: to seed to random randn function to get reproducible result
    param takeout: to divide the data set into train and test sets
    e.g [here its 0.7 to divide the set int o 70% train and 30% test]
    Note:
    here bias column is added which is column full of ones
    """
    total_no = 100
    np.random.seed(seed)
    x_linear = 2 * np.random.randn(total_no, 1)
    y_linear = 4 - 10 * x_linear + np.random.randn(total_no, 1)
    _data = np.c_[x_linear, y_linear]

    bias_column = np.ones(total_no)
    data_modified = np.c_[bias_column, _data]

    amount = int(total_no * 0.7)
    train_data, test_data = data_modified[:amount, :], data_modified[amount:, :]

    np.random.shuffle(train_data)
    np.random.shuffle(test_data)

    return (train_data, test_data)


def _output_val(record_no: int, data_set: np.ndarray) -> np.ndarray:
    """
    param record_no: data point no. in data_set
    param data_set: dataset in which record 's output needed
    return : output for that specific data point value
    """
    return data_set[record_no, -1]


def mse_error(record_no: int, data_set: np.ndarray, param_vec: np.ndarray) -> float:
    """
    param record_no: data point no.
    param dataset: data_set whose data points needs to be taken
    param_vec: parameter_vector
    """
    error = np.power(
        _calc_hypothesis_val(record_no, data_set, param_vec)
        - _output_val(record_no, data_set),
        2,
    )

    return error * 0.5


def _calc_hypothesis_val(
    record_no: int, data_set: np.ndarray, param_vec: np.ndarray
) -> float:
    """
    param record_no: data point no.
    param dataset: data_set whose data points needs to be taken
    param_vec: parameter_vector
    """
    data_set = data_set.reshape(-1, n)
    hypothesis_val = np.dot(data_set[record_no, :], param_vec)
    return hypothesis_val


def _calc_gradient(
    data: np.ndarray, output: np.ndarray, param_vec: np.ndarray
) -> np.ndarray:
    """
    param data: data points/observations
    param output: output values
    param_vec: parameter vector
    Note:
    the expression below is the derivative of the MSE function
    with respect to all parameters
    """
    x_index_transpose = np.transpose(data)

    result = np.dot(x_index_transpose, np.dot(data, param_vec) - output)
    return result


def learning_rate_decay(initial_learning_rate: float, epoch_no: int) -> float:
    """
    param intial_learning_rate: the learning rate in the previous epoch
    param epoch_no: current epoch_no
    """
    decay_rate = 0.01
    new_learning_rate = initial_learning_rate * decay_rate ** epoch_no
    return new_learning_rate


def stocastic_gradient_decent(
    data_set: np.ndarray, param_vec: np.ndarray, seed: int, epochs: int
) -> np.ndarray:
    """
    param dataset: data_set whose data points needs to be taken
    param_vec: parameter_vectors
    param seed: to seed the random shuffle function to get reproducible results
    param epochs: how many times to loop over the data set
    return: parameter vector
    """
    global learning_rate
    np.random.seed(seed)
    np.random.shuffle(data_set)
    X = data_set[:, :n]
    y = data_set[:, -1].reshape(-1, 1)

    for i in range(epochs):
        for _ in range(m):
            random_index = np.random.randint(m)
            x_i = X[random_index : random_index + 1]
            y_i = y[random_index : random_index + 1]
            gradient = _calc_gradient(x_i, y_i, param_vec)
            param_vec -= learning_rate * gradient

        learning_rate = learning_rate_decay(learning_rate, i)

    return param_vec


# Create the train and test data sets
train_data, test_data = generate_data(seed=0, takeout=0.7)

m = train_data.shape[0]
n = train_data.shape[1] - 1

parameter_vector = np.random.randn(n, 1)
learning_rate = 0.1

if __name__ == "__main__":

    print("Testing Stochastic Gradient Descent...")
    parameter_vector = stocastic_gradient_decent(
        train_data, parameter_vector, seed=1907, epochs=100
    )
    print("Converged.")
    print("Done..")
    error = 0.0
    for i in range(test_data.shape[0]):
        error += mse_error(i, test_data, parameter_vector)

    print(np.sqrt(error) / test_data.shape[0])
    print(parameter_vector)
