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


def generate_data(total_no: int, seed: int, takeout: int) -> Tuple:
    """
    param seed: to seed to random randn function to get reproducible result
    param takeout: to divide the data set into train and test sets
    e.g [here its 0.7 to divide the set int o 70% train and 30% test]
    Note:
    here bias column is added which is column full of ones

    >>> train_set, test_set = generate_data(2 , 19, 0.5)
    >>> train_set
    array([[ 1.        ,  0.44200653, -0.9978138 ]])
    >>> test_set
    array([[ 1.        , -0.68093002, 10.40526862]])
    """
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

    >>> output_value = _output_val(1, np.array([[1, 2], [3, 4] ,[5, 6]]))
    >>> output_value
    4
    """
    return data_set[record_no, -1]


def mse_error(record_no: int, data_set: np.ndarray, param_vec: np.ndarray) -> float:
    """
    param record_no: data point no.
    param dataset: data_set whose data points needs to be taken
    param_vec: parameter_vector

    >>> error = mse_error(1, np.array([[1, 2], [3, 4] ,[5, 6]]), np.array([1, 2]))
    >>> error
    24.5

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

    >>> data = np.array([[1, 2], [3, 4] ,[5, 6]])
    >>> parameter_vector = np.array([1, 2])
    >>> hypo_val = _calc_hypothesis_val(1, data, parameter_vector)
    >>> hypo_val
    11

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

    >>> data = np.array([1, 3]).reshape(1, 2)
    >>> output = np.array([1])
    >>> parameter_vector = np.array([1, 2])
    >>> grad = _calc_gradient(data, output, parameter_vector)
    >>> grad
    array([ 6, 18])


    """
    x_index_transpose = np.transpose(data)

    result = np.dot(x_index_transpose, np.dot(data, param_vec) - output)
    return result


def learning_rate_decay(initial_learning_rate: float, epoch_no: int) -> float:
    """
    param intial_learning_rate: the learning rate in the previous epoch
    param epoch_no: current epoch_no

    >>> lr = learning_rate_decay(1, 2)
    >>> lr
    0.0001

    """
    decay_rate = 0.01
    new_learning_rate = initial_learning_rate * decay_rate ** epoch_no
    return new_learning_rate


def stochastic_gradient_descent(
    data_set: np.ndarray, param_vec: np.ndarray, seed: int, epochs: int
) -> np.ndarray:
    """
    param dataset: data_set whose data points needs to be taken
    param_vec: parameter_vectors
    param seed: to seed the random shuffle function to get reproducible results
    param epochs: how many times to loop over the data set
    return: parameter vector

    >>> data = np.array([1, 3], dtype=np.float32).reshape(1, 2)
    >>> output = np.array([1])
    >>> parameter_vector = np.array([[1], [2]], dtype=np.float32)
    >>> parameter_vector = stochastic_gradient_descent(data, parameter_vector,\
        seed=1907, epochs=100)
    >>> parameter_vector
<<<<<<< HEAD
<<<<<<< HEAD
    array([[0.6       ],
           [0.79999995]], dtype=float32)
=======
    array([[1.],
           [2.]], dtype=float32)
>>>>>>> e02ba486625c72ed6b8a705c07e3ebf77bd4b908
=======
    array([[1.],
           [2.]], dtype=float32)
>>>>>>> e02ba486625c72ed6b8a705c07e3ebf77bd4b908

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
train_data, test_data = generate_data(100, seed=0, takeout=0.7)

m = train_data.shape[0]
n = train_data.shape[1] - 1

parameter_vector = np.random.randn(n, 1)
learning_rate = 0.1

if __name__ == "__main__":

    print("Testing Stochastic Gradient Descent...")
    parameter_vector = stochastic_gradient_descent(
        train_data, parameter_vector, seed=1907, epochs=100
    )
    print("Converged.")
    print("Done..")
    error = 0.0
    for i in range(test_data.shape[0]):
        error += mse_error(i, test_data, parameter_vector)

    print(np.sqrt(error) / test_data.shape[0])
    print(parameter_vector)
