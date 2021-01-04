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

paramater_vector = np.zeros(n)
LEARNING_RATE = 0.001

def _MSE_error(record_no, data_set):
    """
    param record_no: record no in dataset whose error has to be calculated
    param record_no: dataset in which record value error needs to be calculated
    return: error in the record
    """
    mean_square_error = np.power(
        calculate_hypothesis_value(record_no, data_set) - data_set[record_no, -1], 2
    )

def _hypothesis_value(data_set, param_vector):
    """
    param data_set: whole dataset of which the hypothesis need to be calcuated
    return hypothesis_val: hypothesis value of the whole dataset
    Note:
    Here dataset's first column will be filled with Ones for the bias term [w_0]
    as x_0 is One above
    """
    data_set_with_bias_column = np.array([np.ones(m, 1), data_set])
    hypothesis_val = np.dot(data_set_with_bias_column, param_vector)
    return hypothesis_val

if __name__ == "__main__":
    print("Hypo_Test")
