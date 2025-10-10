"""
Implementation of gradient descent algorithm for minimizing cost of a linear hypothesis
function.
"""

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
parameter_vector = [2.0, 4.0, 1.0, 5.0]
m = len(train_data)
LEARNING_RATE = 0.009


def _error(example_no: int, data_set: str = "train") -> float:
    """
    :param data_set: train data or test data
    :param example_no: example number whose error has to be checked
    :return: error in example pointed by example number.
    """
    return calculate_hypothesis_value(example_no, data_set) - output(
        example_no, data_set
    )


def _hypothesis_value(data_input_tuple: tuple[float, ...]) -> float:
    """
    Calculates hypothesis function value for a given input
    :param data_input_tuple: Input tuple of a particular example
    :return: Value of hypothesis function at that point.
    Note that there is an 'biased input' whose value is fixed as 1.
    It is not explicitly mentioned in input data.. But, ML hypothesis functions use it.
    So, we have to take care of it separately. Line 36 takes care of it.
    """
    hyp_val = 0.0
    for i in range(len(parameter_vector) - 1):
        hyp_val += data_input_tuple[i] * parameter_vector[i + 1]
    hyp_val += parameter_vector[0]
    return hyp_val


def output(example_no: int, data_set: str) -> float:
    """
    :param data_set: test data or train data
    :param example_no: example whose output is to be fetched
    :return: output for that example
    """
    if data_set == "train":
        return train_data[example_no][1]
    elif data_set == "test":
        return test_data[example_no][1]
    msg = "Unknown data_set: " + data_set
    raise ValueError(msg)


def calculate_hypothesis_value(example_no: int, data_set: str) -> float:
    """
    Calculates hypothesis value for a given example
    :param data_set: test data or train_data
    :param example_no: example whose hypothesis value is to be calculated
    :return: hypothesis value for that example
    """
    if data_set == "train":
        return _hypothesis_value(train_data[example_no][0])
    elif data_set == "test":
        return _hypothesis_value(test_data[example_no][0])
    msg = "Unknown data_set: " + data_set
    raise ValueError(msg)


def summation_of_cost_derivative(index: int, end: int = m) -> float:
    """
    Calculates the sum of cost function derivative
    :param index: index wrt derivative is being calculated
    :param end: value where summation ends, default is m, number of examples
    :return: Returns the summation of cost derivative
    Note: If index is -1, this means we are calculating summation wrt to biased
        parameter.
    """
    summation_value = 0.0
    for i in range(end):
        if index == -1:
            summation_value += _error(i)
        else:
            summation_value += _error(i) * train_data[i][0][index]
    return summation_value


def get_cost_derivative(index: int) -> float:
    """
    :param index: index of the parameter vector wrt to derivative is to be calculated
    :return: derivative wrt to that index
    Note: If index is -1, this means we are calculating summation wrt to biased
        parameter.
    """
    cost_derivative_value = summation_of_cost_derivative(index, m) / m
    return cost_derivative_value


def run_gradient_descent() -> None:
    global parameter_vector
    # Tune these values to set a tolerance value for predicted output
    absolute_error_limit = 0.000002
    relative_error_limit = 0
    j = 0
    while True:
        j += 1
        temp_parameter_vector = [0.0, 0.0, 0.0, 0.0]
        for i in range(len(parameter_vector)):
            cost_derivative = get_cost_derivative(i - 1)
            temp_parameter_vector[i] = (
                parameter_vector[i] - LEARNING_RATE * cost_derivative
            )
        if np.allclose(
            parameter_vector,
            temp_parameter_vector,
            atol=absolute_error_limit,
            rtol=relative_error_limit,
        ):
            break
        parameter_vector = temp_parameter_vector
    print(("Number of iterations:", j))


def test_gradient_descent() -> None:
    for i in range(len(test_data)):
        print(("Actual output value:", output(i, "test")))
        print(("Hypothesis output:", calculate_hypothesis_value(i, "test")))


def run_gradient_descent_vectorized() -> None:
    """
    Vectorized implementation of gradient descent for a linear hypothesis
    using NumPy arrays for efficient matrix operations.
    """
    global parameter_vector

    # Convert training data into NumPy arrays
    x_train = np.array([x for x, _ in train_data])
    y = np.array([y for _, y in train_data])

    # Add bias term (column of ones)
    x_train = np.hstack((np.ones((x_train.shape[0], 1)), x_train))

    # Convert parameter vector to NumPy array
    theta = np.array(parameter_vector, dtype=float)

    absolute_error_limit = 0.000002
    relative_error_limit = 0
    j = 0

    while True:
        j += 1

        # Compute predictions
        predictions = x_train @ theta

        # Compute errors
        errors = predictions - y

        # Compute gradient
        gradient = (x_train.T @ errors) / len(y)

        # Update parameters
        new_theta = theta - LEARNING_RATE * gradient

        # Check for convergence
        if np.allclose(
            theta,
            new_theta,
            atol=absolute_error_limit,
            rtol=relative_error_limit,
        ):
            break

        theta = new_theta

    parameter_vector = theta.tolist()
    print(("Number of iterations (vectorized):", j))


def test_gradient_descent_vectorized() -> None:
    """
    Tests the vectorized gradient descent implementation on test data
    and prints predicted vs actual outputs.
    """
    x_test = np.array([x for x, _ in test_data])
    y_test = np.array([y for _, y in test_data])

    # Add bias term
    x_test = np.hstack((np.ones((x_test.shape[0], 1)), x_test))

    theta = np.array(parameter_vector, dtype=float)
    predictions = x_test @ theta

    for i in range(len(test_data)):
        print(("Actual output value:", y_test[i]))
        print(("Hypothesis output:", predictions[i]))


if __name__ == "__main__":
    print("Running naive (loop-based) gradient descent...\n")
    run_gradient_descent()
    print("\nTesting gradient descent for a linear hypothesis function.\n")
    test_gradient_descent()

    print("\nRunning vectorized gradient descent using NumPy...\n")
    run_gradient_descent_vectorized()
    print("\nTesting vectorized gradient descent.\n")
    test_gradient_descent_vectorized()
