# https://en.wikipedia.org/wiki/Joint_probability_distribution
# Function to calculate the joint probability distribution
def calculate_joint_probability(
    x_values: list, y_values: list, x_probabilities: list, y_probabilities: list
) -> dict:
    """
    Given two random variables that are defined on the same probability space,
    [1] the joint probability distribution is the corresponding 
    probability distribution on all possible pairs of outputs.
    The joint distribution can just as well be considered for any given
      number of random variables.

    Args:
        lst (List[int]): The X values.
        2nd (List[int]): The y values.
        3rd (List[int]): The x probability.
        4th (List[int]): The y probability.

    Returns:
        List[int]: The Joint probability.

    Examples:
    >>> calculate_joint_probability([1],[1],[1],[1])
    {(1,1):1}
    >>> calculate_joint_probability([1][1,2][0.5][0.1,0.5])
    {(1,1):0.05 , (1,2):0.25}

    """
    joint_distribution = {}

    # Calculate the joint probability for all combinations of (X, Y)
    for x, x_prob in zip(x_values, x_probabilities):
        for y, y_prob in zip(y_values, y_probabilities):
            joint_prob = x_prob * y_prob
            joint_distribution[(x, y)] = joint_prob
    return joint_distribution


if __name__ == "__main__":
    import doctest

    # print(calculate_joint_probability([1], [1, 2], [0.5], [0.1, 0, 5]))
    doctest.testmod()
