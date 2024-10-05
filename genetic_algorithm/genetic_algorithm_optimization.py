import numpy as np
from typing import Callable, List, Tuple


class GeneticAlgorithmOptimizer:
    def __init__(
        self,
        objective_function: Callable[..., float],
        variable_bounds: List[Tuple[float, float]],
        population_size: int = 100,
        max_generations: int = 500,
        crossover_probability: float = 0.9,
        mutation_probability: float = 0.01,
    ) -> None:
        self.objective_function = objective_function
        self.variable_bounds = np.array(variable_bounds)
        self.population_size = population_size
        self.max_generations = max_generations
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability
        self.num_variables = len(variable_bounds)

        # Initialize the random number generator
        self.rng = np.random.default_rng()

    def generate_initial_population(self) -> np.ndarray:
        """
        Generate a population of random solutions within the given variable bounds.

        >>> optimizer = GeneticAlgorithmOptimizer(
        ...     objective_function=lambda x: x**2,
        ...     variable_bounds=[(-10, 10)]
        ... )
        >>> population = optimizer.generate_initial_population()
        >>> population.shape == (optimizer.population_size, optimizer.num_variables)
        True
        """
        return self.rng.uniform(
            low=self.variable_bounds[:, 0],
            high=self.variable_bounds[:, 1],
            size=(self.population_size, self.num_variables),
        )

    def evaluate_fitness(self, individual: List[float]) -> float:
        """
        Evaluate the fitness of an individual by computing the value of the objective function.

        >>> optimizer = GeneticAlgorithmOptimizer(
        ...     objective_function=lambda x: x**2,
        ...     variable_bounds=[(-10, 10)]
        ... )
        >>> optimizer.evaluate_fitness([2])
        4
        >>> optimizer.evaluate_fitness([0])
        0
        """
        return self.objective_function(*individual)

    def select_parent(
        self, population: np.ndarray, fitness_values: np.ndarray
    ) -> np.ndarray:
        """
        Select a parent using tournament selection based on fitness values.

        >>> optimizer = GeneticAlgorithmOptimizer(
        ...     objective_function=lambda x: x**2,
        ...     variable_bounds=[(-10, 10)]
        ... )
        >>> population = optimizer.generate_initial_population()
        >>> fitness_values = np.array([optimizer.evaluate_fitness(ind) for ind in population])
        >>> parent = optimizer.select_parent(population, fitness_values)
        >>> len(parent) == optimizer.num_variables
        True
        """
        selected_indices = self.rng.choice(
            range(self.population_size), size=2, replace=False
        )
        return population[selected_indices[np.argmin(fitness_values[selected_indices])]]

    def perform_crossover(
        self, parent1: np.ndarray, parent2: np.ndarray
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Perform one-point crossover between two parents to create offspring.
        Skip crossover for single-variable functions.

        >>> optimizer = GeneticAlgorithmOptimizer(
        ...     objective_function=lambda x: x**2,
        ...     variable_bounds=[(-10, 10)]
        ... )
        >>> parent1 = [1]
        >>> parent2 = [2]
        >>> child1, child2 = optimizer.perform_crossover(parent1, parent2)
        >>> child1 == parent1 and child2 == parent2
        True
        """
        if self.num_variables == 1:
            return parent1, parent2

        if self.rng.random() < self.crossover_probability:
            crossover_point = self.rng.integers(1, self.num_variables)
            child1 = np.concatenate(
                (parent1[:crossover_point], parent2[crossover_point:])
            )
            child2 = np.concatenate(
                (parent2[:crossover_point], parent1[crossover_point:])
            )
            return child1, child2
        return parent1, parent2

    def apply_mutation(self, individual: np.ndarray) -> np.ndarray:
        """
        Apply mutation to an individual based on the mutation probability.

        >>> optimizer = GeneticAlgorithmOptimizer(
        ...     objective_function=lambda x: x**2,
        ...     variable_bounds=[(-10, 10)]
        ... )
        >>> individual = [1]
        >>> mutated_individual = optimizer.apply_mutation(individual.copy())
        >>> len(mutated_individual) == len(individual)
        True
        """
        if self.rng.random() < self.mutation_probability:
            mutation_index = self.rng.integers(0, self.num_variables)
            individual[mutation_index] = self.rng.uniform(
                self.variable_bounds[mutation_index, 0],
                self.variable_bounds[mutation_index, 1],
            )
        return individual

    def optimize(self) -> Tuple[np.ndarray, float]:
        """
        Execute the genetic algorithm over a number of generations to find the optimal solution.
        """
        population = self.generate_initial_population()
        best_solution = None
        best_fitness_value = float("inf")

        for generation in range(self.max_generations):
            fitness_values = np.array(
                [self.evaluate_fitness(individual) for individual in population]
            )

            new_population = []
            for _ in range(self.population_size // 2):
                parent1 = self.select_parent(population, fitness_values)
                parent2 = self.select_parent(population, fitness_values)
                child1, child2 = self.perform_crossover(parent1, parent2)
                child1 = self.apply_mutation(child1)
                child2 = self.apply_mutation(child2)
                new_population.extend([child1, child2])

            population = np.array(new_population)

            # Track the best solution
            min_fitness_index = np.argmin(fitness_values)
            if fitness_values[min_fitness_index] < best_fitness_value:
                best_fitness_value = fitness_values[min_fitness_index]
                best_solution = population[min_fitness_index]

            print(
                f"Generation {generation + 1}, Best Fitness Value: {best_fitness_value}"
            )

        return best_solution, best_fitness_value


if __name__ == "__main__":

    def objective_function(x: float, y: float) -> float:
        """
        Example objective function to minimize x^2 + y^2

        >>> objective_function(0, 0)
        0
        >>> objective_function(3, 4)
        25
        >>> objective_function(-3, -4)
        25
        """
        return x**2 + y**2

    variable_bounds: List[Tuple[float, float]] = [(-10, 10), (-10, 10)]

    optimizer = GeneticAlgorithmOptimizer(
        objective_function=objective_function, variable_bounds=variable_bounds
    )
    best_solution, best_fitness_value = optimizer.optimize()

    print("Best Solution:", best_solution)
    print("Best Fitness Value:", best_fitness_value)