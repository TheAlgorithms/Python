"""
Genetic algorithm for function optimization.

Author: kpuyam
"""

import random
from collections.abc import Callable

# Define the parameters for the genetic algorithm
N_POPULATION = 100
N_SELECTED = 20
MUTATION_PROBABILITY = 0.1
NUM_GENERATIONS = 50


def evaluate(func: Callable, params: list[float]) -> float:
    """
    Evaluate the fitness of an individual based on the provided function.

    Example:
    >>> evaluate(lambda x, y: x ** 2 + y ** 2, [3, 4])
    25
    >>> evaluate(lambda x, y: x + y, [3, 4])
    7
    """
    return func(*params)


def crossover(parent_1: list[float], parent_2: list[float]) -> list[float]:
    """Perform crossover between two parents."""
    crossover_point = random.randint(1, len(parent_1) - 1)
    child = parent_1[:crossover_point] + parent_2[crossover_point:]
    return child


def mutate(individual: list[float], mutation_rate: float) -> list[float]:
    """Mutate an individual with a certain probability."""
    mutated_individual = []
    for gene in individual:
        if random.random() < mutation_rate:
            # Add some noise to the gene's value
            mutated_gene = gene + random.uniform(-0.1, 0.1)
            mutated_individual.append(mutated_gene)
        else:
            mutated_individual.append(gene)
    return mutated_individual


def select(
    population: list[tuple[list[float], float]], num_selected: int
) -> list[list[float]]:
    """Select individuals based on their fitness scores."""
    sorted_population = sorted(population, key=lambda x: x[1])
    selected_parents = [
        individual[0] for individual in sorted_population[:num_selected]
    ]
    return selected_parents


def optimize(
    func: Callable,
    param_ranges: list[tuple[float, float]],
) -> tuple[list[float], float]:
    """Optimize the given function using a genetic algorithm."""
    # Initialize the population
    population = [
        [random.uniform(param_range[0], param_range[1]) for param_range in param_ranges]
        for _ in range(N_POPULATION)
    ]

    # Main optimization loop
    for _generation in range(NUM_GENERATIONS):
        # Evaluate the fitness of each individual in the population
        population_fitness = [
            (individual, evaluate(func, individual)) for individual in population
        ]

        # Select parents for crossover
        selected_parents = select(population_fitness, N_SELECTED)

        # Generate offspring through crossover and mutation
        offspring = []
        for _i in range(N_POPULATION):
            parent_1 = random.choice(selected_parents)
            parent_2 = random.choice(selected_parents)
            child = crossover(parent_1, parent_2)
            child = mutate(child, MUTATION_PROBABILITY)
            offspring.append(child)

        # Replace the old population with the offspring
        population = offspring

    # Find the best individual in the final population
    best_individual, best_fitness = max(population_fitness, key=lambda x: x[1])

    return best_individual, best_fitness


if __name__ == "__main__":
    # Set random seed for reproducibility
    random.seed(123)

    # Example usage:
    def quadratic_function(x, y):
        """Example function to optimize."""
        return x**2 + y**2

    param_ranges = [(-10, 10), (-10, 10)]
    best_params, best_fitness = optimize(quadratic_function, param_ranges)
    print("Best parameters:", best_params)
    print("Best fitness:", best_fitness)
