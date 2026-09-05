"""
Calculate joint probability distribution
https://en.wikipedia.org/wiki/Joint_probability_distribution
"""


def joint_probability_distribution(
    x_values: list[int],
    y_values: list[int],
    x_probabilities: list[float],
    y_probabilities: list[float],
) -> dict:
    """
    >>> joint_distribution =  joint_probability_distribution(
    ...     [1, 2], [-2, 5, 8], [0.7, 0.3], [0.3, 0.5, 0.2]
    ... )
    >>> from math import isclose
    >>> isclose(joint_distribution.pop((1, 8)), 0.14)
    True
    >>> joint_distribution
    {(1, -2): 0.21, (1, 5): 0.35, (2, -2): 0.09, (2, 5): 0.15, (2, 8): 0.06}
    """
    return {
        (x, y): x_prob * y_prob
        for x, x_prob in zip(x_values, x_probabilities)
        for y, y_prob in zip(y_values, y_probabilities)
    }


# Function to calculate the expectation (mean)
def expectation(values: list, probabilities: list) -> float:
    """
    >>> from math import isclose
    >>> isclose(expectation([1, 2], [0.7, 0.3]), 1.3)
    True
    """
    return sum(x * p for x, p in zip(values, probabilities))


# Function to calculate the variance
def variance(values: list[int], probabilities: list[float]) -> float:
    """
    >>> from math import isclose
    >>> isclose(variance([1,2],[0.7,0.3]), 0.21)
    True
    """
    mean = expectation(values, probabilities)
    return sum((x - mean) ** 2 * p for x, p in zip(values, probabilities))


# Function to calculate the covariance
def covariance(
    x_values: list[int],
    y_values: list[int],
    x_probabilities: list[float],
    y_probabilities: list[float],
) -> float:
    """
    >>> covariance([1, 2], [-2, 5, 8], [0.7, 0.3], [0.3, 0.5, 0.2])
    -2.7755575615628914e-17
    """
    mean_x = expectation(x_values, x_probabilities)
    mean_y = expectation(y_values, y_probabilities)
    return sum(
        (x - mean_x) * (y - mean_y) * px * py
        for x, px in zip(x_values, x_probabilities)
        for y, py in zip(y_values, y_probabilities)
    )


# Function to calculate the standard deviation
def standard_deviation(variance: float) -> float:
    """
    >>> standard_deviation(0.21)
    0.458257569495584
    """
    return variance**0.5


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    # Input values for X and Y
    x_vals = input("Enter values of X separated by spaces: ").split()
    y_vals = input("Enter values of Y separated by spaces: ").split()

    # Convert input values to integers
    x_values = [int(x) for x in x_vals]
    y_values = [int(y) for y in y_vals]

    # Input probabilities for X and Y
    x_probs = input("Enter probabilities for X separated by spaces: ").split()
    y_probs = input("Enter probabilities for Y separated by spaces: ").split()
    assert len(x_values) == len(x_probs)
    assert len(y_values) == len(y_probs)

    # Convert input probabilities to floats
    x_probabilities = [float(p) for p in x_probs]
    y_probabilities = [float(p) for p in y_probs]

    # Calculate the joint probability distribution
    jpd = joint_probability_distribution(
        x_values, y_values, x_probabilities, y_probabilities
    )

    # Print the joint probability distribution
    print(
        "\n".join(
            f"P(X={x}, Y={y}) = {probability}" for (x, y), probability in jpd.items()
        )
    )
    mean_xy = expectation(
        [x * y for x in x_values for y in y_values],
        [px * py for px in x_probabilities for py in y_probabilities],
    )
    print(f"x mean: {expectation(x_values, x_probabilities) = }")
    print(f"y mean: {expectation(y_values, y_probabilities) = }")
    print(f"xy mean: {mean_xy}")
    print(f"x: {variance(x_values, x_probabilities) = }")
    print(f"y: {variance(y_values, y_probabilities) = }")
    print(f"{covariance(x_values, y_values, x_probabilities, y_probabilities) = }")
    print(f"x: {standard_deviation(variance(x_values, x_probabilities)) = }")
    print(f"y: {standard_deviation(variance(y_values, y_probabilities)) = }")
