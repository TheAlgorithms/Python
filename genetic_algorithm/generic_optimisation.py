#import random

def fitness_function(x: float) -> float:
    """
    Calculate the fitness (objective) function value for a given input.

    Args:
        x (float): The input value for which the fitness is calculated.

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
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a valid number.")

    # Define your fitness function here (e.g., x^2, or any other function)
    return x**2 + 3 * x + 2


if __name__ == "__main__":
    # Example usage
    x_value = float(input("Enter the value of x: ").strip())
    fitness = fitness_function(x_value)
    print(f"The fitness for x = {x_value} is {fitness}.")
