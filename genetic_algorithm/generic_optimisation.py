import random


# Define the fitness function (objective function)
def fitness_function(x):
    return x**2 + 3 * x + 2


# Genetic Algorithm parameters
population_size = 100
mutation_rate = 0.01
num_generations = 100


# Initialize the population with random individuals
def initialize_population(size):
    return [random.uniform(-10, 10) for _ in range(size)]


# Select individuals for reproduction based on their fitness
def select_parents(population):
    fitness_scores = [fitness_function(x) for x in population]
    total_fitness = sum(fitness_scores)
    probabilities = [score / total_fitness for score in fitness_scores]
    return random.choices(population, probabilities, k=2)


# Create a new individual through crossover (blend two parents)
def crossover(parent1, parent2):
    alpha = random.uniform(0, 1)
    child = alpha * parent1 + (1 - alpha) * parent2
    return child


# Mutate an individual
def mutate(individual):
    if random.random() < mutation_rate:
        return individual + random.uniform(-0.1, 0.1)
    else:
        return individual


# Genetic Algorithm
population = initialize_population(population_size)

for generation in range(num_generations):
    new_population = []
    for _ in range(population_size // 2):
        parent1, parent2 = select_parents(population)
        child1 = crossover(parent1, parent2)
        child2 = crossover(parent1, parent2)
        child1 = mutate(child1)
        child2 = mutate(child2)
        new_population.extend([child1, child2])
    population = new_population

# Find the best individual in the final population
best_individual = max(population, key=fitness_function)
best_fitness = fitness_function(best_individual)

print(f"Best individual: {best_individual}")
print(f"Best fitness: {best_fitness}")
