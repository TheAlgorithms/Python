def fitness_function(input_value: float) -> float:
    """
    Calculate the fitness (objective) function value for a given input.

    Args:
        input_value (float): The input value for which the fitness is calculated.

    Returns:
        float: The fitness value calculated for the input.

    Raises:
        ValueError: If the input is not a valid floating-point number.

    Example:
    >>> fitness_function(2.5)
    12.25
    >>> fitness_function(-1.0)
    6.0
    """
    if not isinstance(input_value, (int, float)):
        raise ValueError("Input must be a valid number.")

    # Define your fitness function here (e.g., x^2, or any other function)
    return input_value**2 + 3 * input_value + 2
