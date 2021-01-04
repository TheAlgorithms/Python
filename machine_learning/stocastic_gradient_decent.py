"""
Implementation of stocastic gradient decent algorithm for minimizing cost
of a Mean Square Error function [MSE]
"""
import numpy as np

"""
function looks like y = w_0 + w_1 * x [For a single Feature[Column]]

for this dataset Created below it will be 
y = w_0 + w_1 * x_1 + w_2 * x_2 + w_3 * x_3
or simply : y = W * X                   :y = output value
                                        :X = whole Input Matrix
                                        :W = Whole Parameter Vector
                                        :* = dot product
"""
def Generate_data(seed, takeout=0.7):

    total_no = 20
    np.random.seed(seed)
    _data = np.random.randint(0, 10, size=(total_no, 4))

    bias_column = np.ones(total_no)
    data_modified = np.c_[bias_column, _data]

    amount = int(20 * 0.7)
    train_data, test_data = data_modified[:amount, :], data_modified[amount: , :]

    np.random.shuffle(train_data)
    np.random.shuffle(test_data)

    return (train_data, test_data)

train_data, test_data = Generate_data(0)

m = train_data.shape[0]
n = train_data.shape[1]

parameter_vector = np.random.randn(n, 1)
LEARNING_RATE = 0.001

def _output_val(record_no: int, data_set: np.ndarray) -> np.ndarray:
    """
    param record_no: data point no. in data_set
    param data_set: dataset in which record 's output needed
    return : output for that specific data point value 
    """
    return data_set[record_no, -1]

def mse_error(record_no, data_set, param_vec):
    """
    param record_no: data point no.
    param dataset: data_set whose data points needs to be taken
    param_vec: parameter_vector
    """
    error = np.power(_calc_hypothesis_val(record_no, data_set, param_vec) - _output_val(
        record_no, data_set), 2)

    return error * 0.5 

def _calc_hypothesis_val(record_no, data_set, param_vec):
    """
    param record_no: data point no.
    param dataset: data_set whose data points needs to be taken
    param_vec: parameter_vector
    """
    hypothesis_val = np.dot(data_set[record_no, :], param_vec)
    return hypothesis_val

def _calc_gradient(X_index, y_index, param_vec):
    pass

def stocastic_gradient_decent(data_set, param_vec, seed):
    """
    """
    np.random.seed(seed)
    np.random.shuffle(data_set)
    for i in range(m):
        random_index = np.random.randint(m)
        data_point_i = data_set[random_index:random_index + 1]
        output_val_i = data_set[random_index:random_index + 1]
        gradient = _calc_gradient(data_point_i, output_val_i, parameter_vector)
        param_vec -= LEARNING_RATE * gradient



if __name__ == "__main__":
    X = train_data[:, :n]
    stocastic_gradient_decent(X, parameter_vector, 1907)