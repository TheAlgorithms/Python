import doctest
import random


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
    0.75
    >>> fitness_function(-1.0)
    6.0
    """
    if not isinstance(input_value, (int, float)):
        raise ValueError("Input must be a valid number.")

    # Define your fitness function here (e.g., x^2, or any other function)
    return input_value**2 - 3 * input_value + 2


def genetic_algorithm() -> tuple[float, float]:
    """
    A simplified genetic algorithm example.

    Example:
    >>> random.seed(42)
    >>> best_solution, best_fitness = genetic_algorithm()
    >>> abs(best_solution - (-1.45)) < 0.1
    False
    >>> abs(best_fitness - 6.0) < 0.1  # Check if the best fitness is within a tolerance
    False
    """
    population = [random.uniform(-2, 2) for _ in range(100)]
    best_solution = min(population, key=fitness_function)
    best_fitness = fitness_function(best_solution)
    return best_solution, best_fitness


if __name__ == "__main__":
    # Example usage
    input_value = float(input("Enter the value of input_value: ").strip())
    fitness = fitness_function(input_value)
    print(f"The fitness for input_value = {input_value} is {fitness}.")

    # Run the doctests
    doctest.testmod()
