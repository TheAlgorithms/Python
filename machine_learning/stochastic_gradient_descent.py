import random
import numpy

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


# Calculate the error for a given example
def error(example_no: int, data_set: str = "train") -> float:
    """
    Calculate the error (the difference between the predicted and actual output)
    for a given example.

    :param example_no: Index of the example.
    :param data_set: 'train' or 'test' to specify the dataset.
    :return: The error for the example (float).
    """
    return hypothesis_value(example_no, data_set) - actual_output(example_no, data_set)


# Get the actual output for a given example
def actual_output(example_no: int, data_set: str) -> float:
    """
    Get the actual output value for a given example.

    :param example_no: Index of the example.
    :param data_set: 'train' or 'test' to specify the dataset.
    :return: The actual output value for the example (float).
    """
    if data_set == "train":
        return train_data[example_no][1]
    elif data_set == "test":
        return test_data[example_no][1]
    return None


def _hypothesis_value(data_input_tuple: tuple) -> float:
    hyp_val = 0
    for i in range(len(parameter_vector) - 1):
        hyp_val += data_input_tuple[i] * parameter_vector[i + 1]
    hyp_val += parameter_vector[0]
    return hyp_val


# Calculate the hypothesis value for a given example
def hypothesis_value(example_no: int, data_set: str) -> float:
    """
    Calculate the value of the hypothesis function for a given example.

    :param example_no: Index of the example.
    :param data_set: 'train' or 'test' to specify the dataset.
    :return: The value of the hypothesis function for the example (float).
    """
    if data_set == "train":
        return _hypothesis_value(train_data[example_no][0])
    elif data_set == "test":
        return _hypothesis_value(test_data[example_no][0])
    return None


# Get the derivative of the cost function for a specific parameter index and example
def cost_derivative(index: int, example_no: int) -> float:
    """
    Get the derivative of the cost function with respect to a specific parameter index.

    :param index: Index of the parameter vector for which the derivative is calculated.
    :param example_no: Index of the example.
    :return: The derivative value for the specified parameter and example (float).
    """
    derivative_value = error(example_no) * train_data[example_no][0][index]
    return derivative_value


# Main function for running stochastic gradient descent
def SGD() -> None:
    """
    Run stochastic gradient descent to optimize the parameter vector.

    This function updates the parameter_vector using stochastic gradient descent.
    """
    global parameter_vector
    absolute_error_limit = 0.000002
    relative_error_limit = 0
    max_iterations = 10000
    j = 0
    while j < max_iterations:
        j += 1
        for i in range(m):
            random_example = random.randint(0, m - 1)
            temp_parameter_vector = [0] * len(parameter_vector)
            for k in range(len(parameter_vector)):
                derivative = cost_derivative(k - 1, random_example)
                temp_parameter_vector[k] = (
                    parameter_vector[k] - LEARNING_RATE * derivative
                )
            parameter_vector = temp_parameter_vector
        if numpy.allclose(
            parameter_vector,
            temp_parameter_vector,
            atol=absolute_error_limit,
            rtol=relative_error_limit,
        ):
            break
    print(("Number of iterations (Stochastic Gradient Descent):", j))


# Function for testing the stochastic gradient descent
def test_SGD() -> None:
    """
    Test the stochastic gradient descent by printing actual and predicted values.
    """
    for i in range(len(test_data)):
        print(("Actual output value:", actual_output(i, "test")))
        print(("Hypothesis output (SGD):", hypothesis_value(i, "test")))


if __name__ == "__main__":
    SGD()
    print("\nTesting stochastic gradient descent for a linear hypothesis function.\n")
    test_SGD()
