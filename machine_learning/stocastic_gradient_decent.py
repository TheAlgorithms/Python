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

def output_val(record_no: int, data_set: np.ndarray) -> np.ndarray:
    """
    param record_no: data point no. in data_set
    param data_set: dataset in which record 's output needed
    return : output for that specific data point value 
    """
    return data_set[record_no, -1]

if __name__ == "__main__":
    pass