import random
import numpy as np

# Parameters
N_POPULATION = 100   # Population size
N_GENERATIONS = 500  # Maximum number of generations
N_SELECTED = 50      # Number of parents selected for the next generation
MUTATION_PROBABILITY = 0.1  # Mutation probability
CROSSOVER_RATE = 0.8  # Probability of crossover
SEARCH_SPACE = (-10, 10)  # Search space for the variables

# Genetic Algorithm for Function Optimization
class GeneticAlgorithm:
    def __init__(self, function, bounds, population_size, generations, mutation_prob, crossover_rate, maximize=True):
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
        # Generate random initial population within the search space
        return [np.random.uniform(low=self.bounds[i][0], high=self.bounds[i][1], size=self.dim) 
                for i in range(self.population_size)]
    
    def fitness(self, individual):
        # Calculate the fitness value (function value)
        value = self.function(*individual)
        return value if self.maximize else -value  # If minimizing, invert the fitness
    
    def select_parents(self):
        # Rank individuals based on fitness and select top individuals for mating
        scores = [(individual, self.fitness(individual)) for individual in self.population]
        scores.sort(key=lambda x: x[1], reverse=True)
        selected = [ind for ind, _ in scores[:N_SELECTED]]
        return selected
    
    def crossover(self, parent1, parent2):
        # Perform uniform crossover
        if random.random() < self.crossover_rate:
            cross_point = random.randint(1, self.dim - 1)
            child1 = np.concatenate((parent1[:cross_point], parent2[cross_point:]))
            child2 = np.concatenate((parent2[:cross_point], parent1[cross_point:]))
            return child1, child2
        return parent1, parent2
    
    def mutate(self, individual):
        # Apply mutation to an individual with some probability
        for i in range(self.dim):
            if random.random() < self.mutation_prob:
                individual[i] = np.random.uniform(self.bounds[i][0], self.bounds[i][1])
        return individual
    
    def evolve(self):
        for generation in range(self.generations):
            # Select parents based on fitness
            parents = self.select_parents()
            next_generation = []

            # Generate offspring using crossover and mutation
            for i in range(0, len(parents), 2):
                parent1, parent2 = parents[i], parents[(i + 1) % len(parents)]
                child1, child2 = self.crossover(parent1, parent2)
                next_generation.append(self.mutate(child1))
                next_generation.append(self.mutate(child2))

            # Ensure population size remains the same
            self.population = next_generation[:self.population_size]

            # Track the best solution so far
            best_individual = max(self.population, key=self.fitness)
            best_fitness = self.fitness(best_individual)
            
            if generation % 10 == 0:
                print(f"Generation {generation}: Best Fitness = {best_fitness}, Best Individual = {best_individual}")
        
        # Return the best individual found
        return max(self.population, key=self.fitness)


# Define a sample function to optimize (e.g., minimize the sum of squares)
def target_function(x, y):
    return x**2 + y**2  # Example: simple parabolic surface (minimization)

# Set bounds for the variables (x, y)
bounds = [(-10, 10), (-10, 10)]  # Both x and y range from -10 to 10

# Instantiate the genetic algorithm
ga = GeneticAlgorithm(
    function=target_function,
    bounds=bounds,
    population_size=N_POPULATION,
    generations=N_GENERATIONS,
    mutation_prob=MUTATION_PROBABILITY,
    crossover_rate=CROSSOVER_RATE,
    maximize=False  # Set to False for minimization
)

# Run the genetic algorithm and find the optimal solution
best_solution = ga.evolve()

print(f"Best solution found: {best_solution}")
print(f"Best fitness (minimum value of function): {target_function(*best_solution)}")
