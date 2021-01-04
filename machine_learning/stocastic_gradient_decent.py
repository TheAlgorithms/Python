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
np.random.seed(1907)
train_data = np.random.randint(0, 10, size=(10, 4))
test_data = np.random.randint(0, 10, size=(4, 4))

m = train_data.shape[0]
n = test_data.shape[1]

bias_column = np.ones(m)
train_data_modified = np.c_[bias_column, train_data]
test_data_modified = np.c_[bias_column, train_data]

paramater_vector = np.random.randn(n, 1)
LEARNING_RATE = 0.001

def _output_val(record_no: int, data_set: np.ndarray) -> np.ndarray:
    """
    param record_no: data point no. in data_set
    param data_set: dataset in which record 's output needed
    return : output for that specific data point value 
    """
    return data_set[record_no, -1]

def mse_error(record_no, dataset):
    """
    """
    pass

def _calc_hypothesis_val(record_no, data_set, param_vec):
    """
    param record_no: data point no.
    param dataset: data_set whose data points needs to be taken
    param_vec: parameter_vector
    """
    hypothesis_val = np.dot(data_set[record_no, :], param_vec)
    return hypothesis_val

if __name__ == "__main__":
    X = train_data_modified[:, :n]
    print(_calc_hypothesis_val(record_no=1, data_set=X, param_vec=paramater_vector))