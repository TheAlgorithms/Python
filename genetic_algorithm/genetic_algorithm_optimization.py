import random
from collections.abc import Callable, Sequence
from concurrent.futures import ThreadPoolExecutor

import numpy as np

# Parameters
N_POPULATION = 100  # Population size
N_GENERATIONS = 500  # Maximum number of generations
N_SELECTED = 50  # Number of parents selected for the next generation
MUTATION_PROBABILITY = 0.1  # Mutation probability
CROSSOVER_RATE = 0.8  # Probability of crossover
SEARCH_SPACE = (-10, 10)  # Search space for the variables

# Random number generator
rng = np.random.default_rng()


class GeneticAlgorithm:
    def __init__(
        self,
        function: Callable[[float, float], float],
        bounds: Sequence[tuple[int | float, int | float]],
        population_size: int,
        generations: int,
        mutation_prob: float,
        crossover_rate: float,
        maximize: bool = True,
    ) -> None:
        self.function = function  # Target function to optimize
        self.bounds = bounds  # Search space bounds (for each variable)
        self.population_size = population_size
        self.generations = generations
        self.mutation_prob = mutation_prob
        self.crossover_rate = crossover_rate
        self.maximize = maximize
        self.dim = len(bounds)  # Dimensionality of the function (number of variables)

        # Initialize population
        self.population = self.initialize_population()

    def initialize_population(self) -> list[np.ndarray]:
        """
        Initialize the population with random individuals within the search space.

        Example:
        >>> ga = GeneticAlgorithm(
        ...     function=lambda x, y: x**2 + y**2,
        ...     bounds=[(-10, 10), (-10, 10)],
        ...     population_size=5,
        ...     generations=10,
        ...     mutation_prob=0.1,
        ...     crossover_rate=0.8,
        ...     maximize=False
        ... )
        >>> len(ga.initialize_population())
        5  # The population size should be equal to 5.
        >>> all(len(ind) == 2 for ind in ga.initialize_population())
        # Each individual should have 2 variables
        True
        """
        return [
            np.array([rng.uniform(b[0], b[1]) for b in self.bounds])
            for _ in range(self.population_size)
        ]

    def fitness(self, individual: np.ndarray) -> float:
        """
        Calculate the fitness value (function value) for an individual.

        Example:
        >>> ga = GeneticAlgorithm(
        ...     function=lambda x, y: x**2 + y**2,
        ...     bounds=[(-10, 10), (-10, 10)],
        ...     population_size=10,
        ...     generations=10,
        ...     mutation_prob=0.1,
        ...     crossover_rate=0.8,
        ...     maximize=False
        ... )
        >>> individual = np.array([1.0, 2.0])
        >>> ga.fitness(individual)
        -5.0  # The fitness should be -1^2 + 2^2 = 5 for minimizing
        >>> ga.maximize = True
        >>> ga.fitness(individual)
        5.0  # The fitness should be 1^2 + 2^2 = 5 when maximizing
        """
        value = float(self.function(*individual))  # Ensure fitness is a float
        return value if self.maximize else -value  # If minimizing, invert the fitness

    def select_parents(
        self, population_score: list[tuple[np.ndarray, float]]
    ) -> list[np.ndarray]:
        """
        Select top N_SELECTED parents based on fitness.

        Example:
        >>> ga = GeneticAlgorithm(
        ...     function=lambda x, y: x**2 + y**2,
        ...     bounds=[(-10, 10), (-10, 10)],
        ...     population_size=10,
        ...     generations=10,
        ...     mutation_prob=0.1,
        ...     crossover_rate=0.8,
        ...     maximize=False
        ... )
        >>> population_score = [
        ...     (np.array([1.0, 2.0]), 5.0),
        ...     (np.array([-1.0, -2.0]), 5.0),
        ...     (np.array([0.0, 0.0]), 0.0),
        ... ]
        >>> selected_parents = ga.select_parents(population_score)
        >>> len(selected_parents)
        2  # Should select the two parents with the best fitness scores.
        >>> np.array_equal(selected_parents[0], np.array([1.0, 2.0]))
        True  # Parent 1 should be [1.0, 2.0]
        >>> np.array_equal(selected_parents[1], np.array([-1.0, -2.0]))
        True  # Parent 2 should be [-1.0, -2.0]

        >>> population_score = [
        ...     (np.array([1.0, 2.0]), 5.0),
        ...     (np.array([1.0, -2.0]), 5.0),
        ...     (np.array([0.0, 0.0]), 0.0),
        ...     (np.array([-1.0, 2.0]), 5.0),
        ...     (np.array([-1.0, -2.0]), 5.0)
        ... ]
        >>> selected_parents = ga.select_parents(population_score)
        >>> len(selected_parents)
        5  # Should select the top 5 parents with the best fitness scores.
        >>> np.array_equal(selected_parents[0], np.array([1.0, 2.0]))
        True  # Parent 1 should be [1.0, 2.0]
        """

        if not population_score:
            raise ValueError("Population score is empty, cannot select parents.")

        population_score.sort(key=lambda score_tuple: score_tuple[1], reverse=True)
        selected_count = min(N_SELECTED, len(population_score))
        return [ind for ind, _ in population_score[:selected_count]]

    def crossover(
        self, parent1: np.ndarray, parent2: np.ndarray
    ) -> tuple[np.ndarray, np.ndarray]:
        """
        Perform uniform crossover between two parents to generate offspring.

        Args:
            parent1 (np.ndarray): The first parent.
            parent2 (np.ndarray): The second parent.
        Returns:
            tuple[np.ndarray, np.ndarray]: The two offspring generated by crossover.

        Example:
        >>> ga = GeneticAlgorithm(
        ...     lambda x, y: -(x**2 + y**2),
        ...     [(-10, 10), (-10, 10)],
        ...     10, 100, 0.1, 0.8, True
        ... )
        >>> parent1, parent2 = np.array([1, 2]), np.array([3, 4])
        >>> len(ga.crossover(parent1, parent2)) == 2
        True
        """
        if random.random() < self.crossover_rate:
            cross_point = random.randint(1, self.dim - 1)
            child1 = np.concatenate((parent1[:cross_point], parent2[cross_point:]))
            child2 = np.concatenate((parent2[:cross_point], parent1[cross_point:]))
            return child1, child2
        return parent1, parent2

    def mutate(self, individual: np.ndarray) -> np.ndarray:
        """
        Apply mutation to an individual.

        Args:
            individual (np.ndarray): The individual to mutate.

        Returns:
            np.ndarray: The mutated individual.

        Example:
        >>> ga = GeneticAlgorithm(
        ...     lambda x, y: -(x**2 + y**2),
        ...     [(-10, 10), (-10, 10)],
        ...     10, 100, 0.1, 0.8, True
        ... )
        >>> ind = np.array([1.0, 2.0])
        >>> mutated = ga.mutate(ind)
        >>> len(mutated) == 2  # Ensure it still has the correct number of dimensions
        True
        """
        for i in range(self.dim):
            if random.random() < self.mutation_prob:
                individual[i] = rng.uniform(self.bounds[i][0], self.bounds[i][1])
        return individual

    def evaluate_population(self) -> list[tuple[np.ndarray, float]]:
        """
        Evaluate the fitness of the entire population in parallel.

        Returns:
            list[tuple[np.ndarray, float]]:
                The population with their respective fitness values.

        Example:
        >>> ga = GeneticAlgorithm(
        ...     lambda x, y: -(x**2 + y**2),
        ...     [(-10, 10), (-10, 10)],
        ...     10, 100, 0.1, 0.8, True
        ... )
        >>> eval_population = ga.evaluate_population()
        >>> len(eval_population) == ga.population_size  # Ensure population size
        True
        >>> all(
        ...     isinstance(ind, tuple) and isinstance(ind[1], float)
        ...     for ind in eval_population
        ... )
        True
        """
        with ThreadPoolExecutor() as executor:
            return list(
                executor.map(
                    lambda individual: (individual, self.fitness(individual)),
                    self.population,
                )
            )

    def evolve(self, verbose: bool = True) -> np.ndarray:
        """
        Evolve the population over the generations to find the best solution.

        Args:
            verbose (bool): If True, prints the progress of the generations.

        Returns:
            np.ndarray: The best individual found during the evolution process.

        Example:
        >>> ga = GeneticAlgorithm(
        ...     function=lambda x, y: x**2 + y**2,
        ...     bounds=[(-10, 10), (-10, 10)],
        ...     population_size=10,
        ...     generations=10,
        ...     mutation_prob=0.1,
        ...     crossover_rate=0.8,
        ...     maximize=False
        ... )
        >>> best_solution = ga.evolve(verbose=False)
        >>> len(best_solution)
        2  # The best solution should be a 2-element array (var_x, var_y)
        >>> isinstance(best_solution[0], float)  # First element should be a float
        True
        >>> isinstance(best_solution[1], float)  # Second element should be a float
        True
        """
        best_individual = None
        for generation in range(self.generations):
            # Evaluate population fitness (multithreaded)
            population_score = self.evaluate_population()

            # Ensure population_score isn't empty
            if not population_score:
                raise ValueError("Population score is empty. No individuals evaluated.")

            # Check the best individual
            best_individual = max(
                population_score, key=lambda score_tuple: score_tuple[1]
            )[0]
            best_fitness = self.fitness(best_individual)

            # Select parents for next generation
            parents = self.select_parents(population_score)
            next_generation = []

            # Generate offspring using crossover and mutation
            for i in range(0, len(parents), 2):
                parent1, parent2 = (
                    parents[i],
                    parents[(i + 1) % len(parents)],
                )  # Wrap around for odd cases
                child1, child2 = self.crossover(parent1, parent2)
                next_generation.append(self.mutate(child1))
                next_generation.append(self.mutate(child2))

            # Ensure population size remains the same
            self.population = next_generation[: self.population_size]

            if verbose and generation % 10 == 0:
                print(f"Generation {generation}: Best Fitness = {best_fitness}")

        return best_individual


# Example target function for optimization
def target_function(var_x: float, var_y: float) -> float:
    """
    Example target function (parabola) for optimization.
    Args:
        var_x (float): The x-coordinate.
        var_y (float): The y-coordinate.
    Returns:
        float: The value of the function at (var_x, var_y).

    Example:
    >>> target_function(0, 0)
    0
    >>> target_function(1, 1)
    2
    """
    return var_x**2 + var_y**2  # Simple parabolic surface (minimization)


# Set bounds for the variables (var_x, var_y)
bounds = [(-10, 10), (-10, 10)]  # Both var_x and var_y range from -10 to 10

# Instantiate and run the genetic algorithm
ga = GeneticAlgorithm(
    function=target_function,
    bounds=bounds,
    population_size=N_POPULATION,
    generations=N_GENERATIONS,
    mutation_prob=MUTATION_PROBABILITY,
    crossover_rate=CROSSOVER_RATE,
    maximize=False,  # Minimize the function
)

best_solution = ga.evolve()
print(f"Best solution found: {best_solution}")
print(f"Best fitness (minimum value of function): {target_function(*best_solution)}")
