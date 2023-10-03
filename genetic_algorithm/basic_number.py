import random
import doctest


def fitness_function(input_value):
    """
    Calculate the fitness (objective) function value for a given input.

    Args:
        input_value (float): The input value for which the fitness is calculated.

    Returns:
        float: The fitness value calculated for the input.

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
    Optimize a numeric value using a simple genetic algorithm.

    Returns:
        tuple[float, float]: A tuple containing the best solution and its fitness value.

    Example:
    >>> best_solution, best_fitness = genetic_algorithm()
    >>> -1.5 < best_solution < -1.4
    False
    >>> 6 < best_fitness < 6.1
    False
    """
    population_size = 50
    mutation_rate = 0.1
    num_generations = 100

    population = [random.uniform(-10, 10) for _ in range(population_size)]

    for generation in range(num_generations):
        fitness_scores = [fitness_function(individual) for individual in population]

        selected_population = []
        for _ in range(population_size):
            tournament_size = 5
            tournament = random.sample(range(population_size), tournament_size)
            tournament_fitness = [fitness_scores[i] for i in tournament]
            selected_individual = population[
                tournament[tournament_fitness.index(max(tournament_fitness))]
            ]
            selected_population.append(selected_individual)

        for i in range(population_size):
            if random.random() < mutation_rate:
                selected_population[i] += random.uniform(-0.5, 0.5)

        population = selected_population

    best_solution = max(population, key=fitness_function)
    best_fitness = fitness_function(best_solution)

    return best_solution, best_fitness


if __name__ == "__main__":
    # Run the doctests
    doctest.testmod()
    input_value = float(input("Enter the value of input_value: ").strip())
    fitness = fitness_function(input_value)
    print(f"The fitness for input_value = {input_value} is {fitness}.")
