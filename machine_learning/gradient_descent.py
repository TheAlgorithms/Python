"""
Gradient descent helpers for a simple linear hypothesis function.

Time complexity: O(iterations * n_samples * n_features)
Space complexity: O(n_features)
"""

from __future__ import annotations

from collections.abc import Sequence

import numpy as np

# List of input, output pairs (bias term handled separately)
train_data: tuple[tuple[tuple[float, ...], float], ...] = (
    ((5.0, 2.0, 3.0), 15.0),
    ((6.0, 5.0, 9.0), 25.0),
    ((11.0, 12.0, 13.0), 41.0),
    ((1.0, 1.0, 1.0), 8.0),
    ((11.0, 12.0, 13.0), 41.0),
)
test_data: tuple[tuple[tuple[float, ...], float], ...] = (
    ((515.0, 22.0, 13.0), 555.0),
    ((61.0, 35.0, 49.0), 150.0),
)
parameter_vector: list[float] = [2.0, 4.0, 1.0, 5.0]
LEARNING_RATE = 0.009


def _get_dataset(data_set: str) -> tuple[tuple[tuple[float, ...], float], ...]:
    """Return the requested dataset or raise for unknown keys."""
    if data_set == "train":
        return train_data
    if data_set == "test":
        return test_data
    msg = "data_set must be 'train' or 'test'"
    raise ValueError(msg)


def predict_from_parameters(
    parameters: Sequence[float], features: Sequence[float]
) -> float:
    """
    Evaluate the linear hypothesis, treating the first coefficient as the bias term.

    >>> predict_from_parameters([1.0, 2.0, -1.0], (3.0, 0.5))
    6.5
    """
    if len(parameters) != len(features) + 1:
        raise ValueError("parameters must include a bias term and match feature count")
    return float(parameters[0] + np.dot(parameters[1:], features))


def output(example_no: int, data_set: str = "train") -> float:
    """
    Retrieve the label for an example from the requested dataset.

    >>> output(0, data_set=\"train\")
    15.0
    """
    dataset = _get_dataset(data_set)
    return dataset[example_no][1]


def calculate_hypothesis_value(
    example_no: int,
    data_set: str = "train",
    parameters: Sequence[float] | None = None,
) -> float:
    """
    Calculate the hypothesis value for a specific example.

    >>> calculate_hypothesis_value(0, parameters=[2.0, 1.0, 0.0, 0.0])
    7.0
    """
    dataset = _get_dataset(data_set)
    params = parameter_vector if parameters is None else parameters
    return predict_from_parameters(params, dataset[example_no][0])


def _error(
    example_no: int, data_set: str = "train", parameters: Sequence[float] | None = None
) -> float:
    """Compute the prediction error for one example."""
    return calculate_hypothesis_value(example_no, data_set, parameters) - output(
        example_no, data_set
    )


def summation_of_cost_derivative(
    index: int,
    end: int | None = None,
    parameters: Sequence[float] | None = None,
    data_set: str = "train",
    dataset: Sequence[tuple[Sequence[float], float]] | None = None,
) -> float:
    """
    Calculate the summed derivative of the cost function for a parameter index.

    ``index=-1`` represents the bias term.
    """
    working_dataset = _get_dataset(data_set) if dataset is None else dataset
    params = parameter_vector if parameters is None else parameters
    limit = len(working_dataset) if end is None else end

    summation_value = 0.0
    for i in range(limit):
        features, label = working_dataset[i]
        error = predict_from_parameters(params, features) - label
        if index == -1:
            summation_value += error
        else:
            summation_value += error * features[index]
    return summation_value


def get_cost_derivative(
    index: int,
    data_set: str = "train",
    parameters: Sequence[float] | None = None,
    dataset: Sequence[tuple[Sequence[float], float]] | None = None,
) -> float:
    """
    Return the average cost derivative for one parameter.

    ``index=-1`` represents the bias term.
    """
    working_dataset = _get_dataset(data_set) if dataset is None else dataset
    return summation_of_cost_derivative(
        index, len(working_dataset), parameters, data_set, working_dataset
    ) / len(working_dataset)


def batch_gradient_descent_step(
    parameters: Sequence[float],
    learning_rate: float,
    data: Sequence[tuple[Sequence[float], float]] | None = None,
) -> list[float]:
    """
    Perform one batch gradient descent step.

    >>> dataset = (((1.0, 0.0, 0.0), 1.0), ((0.0, 1.0, 0.0), 1.0))
    >>> batch_gradient_descent_step([0.0, 0.0, 0.0, 0.0], 0.1, dataset)
    [0.1, 0.05, 0.05, 0.0]
    """
    dataset = train_data if data is None else data
    updated_parameters: list[float] = []
    for i, parameter in enumerate(parameters):
        cost_derivative = get_cost_derivative(
            i - 1, data_set="train", parameters=parameters, dataset=dataset
        )
        updated_parameters.append(parameter - learning_rate * cost_derivative)
    return updated_parameters


def run_gradient_descent(
    learning_rate: float = LEARNING_RATE,
    max_iterations: int = 10_000,
    atol: float = 2e-6,
    rtol: float = 0.0,
) -> tuple[list[float], int]:
    """
    Repeatedly apply gradient descent until the parameter vector stabilizes.

    >>> params, iterations = run_gradient_descent(max_iterations=5)
    >>> len(params)
    4
    >>> iterations >= 1
    True
    """
    global parameter_vector
    iterations = 0
    current_parameters = parameter_vector[:]
    for iteration in range(1, max_iterations + 1):
        iterations = iteration
        next_parameters = batch_gradient_descent_step(current_parameters, learning_rate)
        if np.allclose(current_parameters, next_parameters, atol=atol, rtol=rtol):
            current_parameters = next_parameters
            break
        current_parameters = next_parameters

    parameter_vector = current_parameters
    return current_parameters, iterations


def test_gradient_descent() -> None:
    """Run a quick prediction check against the test dataset."""
    params, iterations = run_gradient_descent()
    print(f"Converged in {iterations} iterations -> {params}")
    for i in range(len(test_data)):
        print(("Actual output value:", output(i, "test")))
        print(("Hypothesis output:", calculate_hypothesis_value(i, "test")))


if __name__ == "__main__":
    print("\nTesting gradient descent for a linear hypothesis function.\n")
    test_gradient_descent()
