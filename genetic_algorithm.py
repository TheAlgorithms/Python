import random

# Define the target string (the goal of the genetic algorithm)
target_string = "Hello, World!"

# Function to generate a random string of the same length as the target
def generate_random_string(length):
    return ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.!?") for _ in range(length))

# Function to calculate the fitness of an individual (string)
def calculate_fitness(individual):
    return sum(1 for i, j in zip(individual, target_string) if i == j)

# Function to perform selection (tournament selection)
def selection(population):
    tournament_size = 3
    selected = [random.choice(population) for _ in range(tournament_size)]
    return max(selected, key=calculate_fitness)

# Function to perform crossover (single-point crossover)
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child = parent1[:point] + parent2[point:]
    return child

# Function to perform mutation (random character mutation)
def mutation(individual, mutation_rate):
    return ''.join(
        random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.!?")
        if random.random() < mutation_rate else char
        for char in individual
    )

# Main genetic algorithm loop
population_size = 100
mutation_rate = 0.01

population = [generate_random_string(len(target_string)) for _ in range(population_size)]

generation = 1
while True:
    population = sorted(population, key=calculate_fitness, reverse=True)
    best_individual = population[0]

    if best_individual == target_string:
        break

    new_population = [best_individual]

    while len(new_population) < population_size:
        parent1 = selection(population)
        parent2 = selection(population)
        child = crossover(parent1, parent2)
        child = mutation(child, mutation_rate)
        new_population.append(child)

    population = new_population
    generation += 1

    if generation % 10 == 0:
        print(f"Generation {generation}: {best_individual} (Fitness: {calculate_fitness(best_individual)})")

print(f"Generation {generation}: {best_individual} (Fitness: {calculate_fitness(best_individual)})")
print("Genetic algorithm completed!")
