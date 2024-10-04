import numpy as np


class GeneticAlgorithmOptimizer:
    def __init__(
        self,
        func,
        bounds,
        population_size=100,
        generations=500,
        crossover_prob=0.9,
        mutation_prob=0.01,
    ):
        self.func = func
        self.bounds = np.array(bounds)
        self.population_size = population_size
        self.generations = generations
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob
        self.num_variables = len(bounds)

        # Initialize the random number generator
        self.rng = np.random.default_rng()

    def initialize_population(self):
        """
        Initialize a population of random solutions within the bounds.
        """
        return self.rng.uniform(
            low=self.bounds[:, 0],
            high=self.bounds[:, 1],
            size=(self.population_size, self.num_variables),
        )

    def fitness(self, individual):
        """
        Evaluate the fitness of an individual.
        In minimization problems, we aim to minimize the function value.
        """
        return self.func(*individual)

    def select_parents(self, population, fitness_scores):
        """
        Select parents using tournament selection.
        """
        selected_indices = self.rng.choice(
            range(self.population_size), size=2, replace=False
        )
        return population[selected_indices[np.argmin(fitness_scores[selected_indices])]]

    def crossover(self, parent1, parent2):
        """
        Perform one-point crossover to create offspring.
        Skip crossover for single-variable functions.
        """
        if self.num_variables == 1:
            return parent1, parent2  # No crossover needed for single-variable functions

        if self.rng.random() < self.crossover_prob:
            point = self.rng.integers(1, self.num_variables)
            child1 = np.concatenate((parent1[:point], parent2[point:]))
            child2 = np.concatenate((parent2[:point], parent1[point:]))
            return child1, child2
        return parent1, parent2

    def mutate(self, individual):
        """
        Apply mutation to an individual with a given mutation probability.
        """
        if self.rng.random() < self.mutation_prob:
            index = self.rng.integers(0, self.num_variables)
            individual[index] = self.rng.uniform(
                self.bounds[index, 0], self.bounds[index, 1]
            )
        return individual

    def evolve(self):
        """
        Run the genetic algorithm for a number of generations.
        """
        population = self.initialize_population()
        best_solution = None
        best_fitness = float("inf")

        for gen in range(self.generations):
            fitness_scores = np.array(
                [self.fitness(individual) for individual in population]
            )

            new_population = []
            for _ in range(self.population_size // 2):
                parent1 = self.select_parents(population, fitness_scores)
                parent2 = self.select_parents(population, fitness_scores)
                child1, child2 = self.crossover(parent1, parent2)
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)
                new_population.extend([child1, child2])

            population = np.array(new_population)

            # Track the best solution
            min_fitness_index = np.argmin(fitness_scores)
            if fitness_scores[min_fitness_index] < best_fitness:
                best_fitness = fitness_scores[min_fitness_index]
                best_solution = population[min_fitness_index]

            print(f"Generation {gen + 1}, Best Fitness: {best_fitness}")

        return best_solution, best_fitness


if __name__ == "__main__":
    # Define the function to optimize
    def func(x, y):
        return x**2 + y**2  # Example: Minimizing x^2 + y^2

    # Define the bounds for each variable
    bounds = [(-10, 10), (-10, 10)]

    # Initialize and run the optimizer
    optimizer = GeneticAlgorithmOptimizer(func=func, bounds=bounds)
    best_solution, best_fitness = optimizer.evolve()

    print("Best Solution:", best_solution)
    print("Best Fitness:", best_fitness)
