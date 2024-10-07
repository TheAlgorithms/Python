import numpy as np

# List of input, output pairs
train_data = (
    ((5, 2, 3), 15),
    ((6, 5, 9), 25),
    ((11, 12, 13), 41),
    ((1, 1, 1), 8),
    ((11, 12, 13), 41),
)
test_data = (((515, 22, 13), 555), ((61, 35, 49), 150))
parameter_vector = [2, 4, 1, 5]
m = len(train_data)
LEARNING_RATE = 0.009
MOMENTUM = 0.9

# Initialize velocity (for momentum)
velocity = [0] * len(parameter_vector)

def _error(example_no, data_set="train"):
    return calculate_hypothesis_value(example_no, data_set) - output(example_no, data_set)

def _hypothesis_value(data_input_tuple):
    hyp_val = 0
    for i in range(len(parameter_vector) - 1):
        hyp_val += data_input_tuple[i] * parameter_vector[i + 1]
    hyp_val += parameter_vector[0]
    return hyp_val

def output(example_no, data_set):
    if data_set == "train":
        return train_data[example_no][1]
    elif data_set == "test":
        return test_data[example_no][1]
    return None

def calculate_hypothesis_value(example_no, data_set):
    if data_set == "train":
        return _hypothesis_value(train_data[example_no][0])
    elif data_set == "test":
        return _hypothesis_value(test_data[example_no][0])
    return None

def summation_of_cost_derivative(index, end=m):
    summation_value = 0
    for i in range(end):
        if index == -1:
            summation_value += _error(i)
        else:
            summation_value += _error(i) * train_data[i][0][index]
    return summation_value

def get_cost_derivative(index):
    return summation_of_cost_derivative(index, m) / m

def run_gradient_descent_with_momentum():
    global parameter_vector, velocity
    absolute_error_limit = 0.000002
    relative_error_limit = 0
    j = 0
    while True:
        j += 1
        temp_parameter_vector = [0] * len(parameter_vector)
        for i in range(len(parameter_vector)):
            cost_derivative = get_cost_derivative(i - 1)
            velocity[i] = MOMENTUM * velocity[i] + cost_derivative
            temp_parameter_vector[i] = parameter_vector[i] - LEARNING_RATE * velocity[i]
        
        if np.allclose(parameter_vector, temp_parameter_vector, atol=absolute_error_limit, rtol=relative_error_limit):
            break
        parameter_vector = temp_parameter_vector
    print(("Number of iterations:", j))

def test_gradient_descent():
    for i in range(len(test_data)):
        print(("Actual output value:", output(i, "test")))
        print(("Hypothesis output:", calculate_hypothesis_value(i, "test")))

if __name__ == "__main__":
    run_gradient_descent_with_momentum()
    print("\nTesting gradient descent with momentum for a linear hypothesis function.\n")
    test_gradient_descent()
