import numpy as np
import random
from concurrent.futures import ThreadPoolExecutor


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
        function,
        bounds,
        population_size,
        generations,
        mutation_prob,
        crossover_rate,
        maximize=True,
    ):

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

    def initialize_population(self):
        # Generate random initial population within the search space using the generator
        return [
            rng.uniform(low=self.bounds[i][0], high=self.bounds[i][1], size=self.dim)
            for i in range(self.population_size)
        ]


    def fitness(self, individual):
        # Calculate the fitness value (function value)
        value = self.function(*individual)
        return value if self.maximize else -value  # If minimizing, invert the fitness


    def select_parents(self, population_score):
        # Select top N_SELECTED parents based on fitness
        population_score.sort(key=lambda x: x[1], reverse=True)
        return [ind for ind, _ in population_score[:N_SELECTED]]


    def crossover(self, parent1, parent2):
        # Perform uniform crossover
        if random.random() < self.crossover_rate:
            cross_point = random.randint(1, self.dim - 1)
            child1 = np.concatenate((parent1[:cross_point], parent2[cross_point:]))
            child2 = np.concatenate((parent2[:cross_point], parent1[cross_point:]))
            return child1, child2
        return parent1, parent2


    def mutate(self, individual):
        # Apply mutation to an individual using the new random generator
        for i in range(self.dim):
            if random.random() < self.mutation_prob:
                individual[i] = rng.uniform(self.bounds[i][0], self.bounds[i][1])
        return individual


    def evaluate_population(self):
        # Multithreaded evaluation of population fitness
        with ThreadPoolExecutor() as executor:
            return list(
                executor.map(lambda ind: (ind, self.fitness(ind)), self.population)
            )


    def evolve(self):
        for generation in range(self.generations):
            # Evaluate population fitness (multithreaded)
            population_score = self.evaluate_population()

            # Check the best individual
            best_individual = max(population_score, key=lambda x: x[1])[0]
            best_fitness = self.fitness(best_individual)

            # Select parents for next generation
            parents = self.select_parents(population_score)
            next_generation = []

            # Generate offspring using crossover and mutation
            for i in range(0, len(parents), 2):
                parent1, parent2 = parents[i], parents[(i + 1) % len(parents)]
                child1, child2 = self.crossover(parent1, parent2)
                next_generation.append(self.mutate(child1))
                next_generation.append(self.mutate(child2))

            # Ensure population size remains the same
            self.population = next_generation[: self.population_size]

            if generation % 10 == 0:
                print(f"Generation {generation}: Best Fitness = {best_fitness}")

        return best_individual


# Example target function for optimization
def target_function(x, y):
    return x**2 + y**2  # Simple parabolic surface (minimization)


# Set bounds for the variables (x, y)
bounds = [(-10, 10), (-10, 10)]  # Both x and y range from -10 to 10


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
