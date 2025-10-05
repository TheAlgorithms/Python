"""Did you know that Genetic Algorithms can be used to quickly approximate combinatorial optimization problems such as knapsack?"""

import random
from dataclasses import dataclass

random.seed(42)

# =========================== Problem setup: Knapsack ===========================

KNAPSACK_N_ITEMS = 42                   # Number of items in the knapsack problem
KNAPSACK_VALUE_RANGE = (10, 100)        # Range of item values
KNAPSACK_WEIGHT_RANGE = (5, 50)         # Range of item weights
KNAPSACK_CAPACITY_RATIO = 0.5           # Capacity as a fraction of total weight

@dataclass
class Item:
    value: int
    weight: int

def generate_knapsack_instance(n_items: int, value_range: tuple[int, int], weight_range: tuple[int, int], capacity_ratio=float) -> tuple[list[Item], int]:
    """Generates a random knapsack problem instance."""
    items = []
    for _ in range(n_items):
        value = random.randint(*value_range)
        weight = random.randint(*weight_range)
        items.append(Item(value=value, weight=weight))
    # We set capacity as a fraction of total weight
    capacity = int(sum(it.weight for it in items) * capacity_ratio)
    return items, capacity

items, capacity = generate_knapsack_instance(n_items=KNAPSACK_N_ITEMS, value_range=KNAPSACK_VALUE_RANGE, weight_range=KNAPSACK_WEIGHT_RANGE, capacity_ratio=KNAPSACK_CAPACITY_RATIO)



# ============================== GA Representation ==============================

# HYPERPARAMETERS (For tuning the GA)

POPULATION_SIZE = 120
GENERATIONS = 200
CROSSOVER_PROBABILITY = 0.9
MUTATION_PROBABILITY = 0.01
TOURNAMENT_K = 3
ELITISM = 2

OVERWEIGHT_PENALTY_FACTOR = 10

Genome = list[int] # An index list where 1 means item is included, 0 means excluded

def evaluate(genome: Genome, items: list[Item], capacity: int) -> tuple[int, int]:
    """Evaluation function - calculates the fitness of each candidate based on total value and weight."""
    total_value = 0
    total_weight = 0
    for gene, item in zip(genome, items):
        if gene:
            total_value += item.value
            total_weight += item.weight
    if total_weight > capacity:
        # Penalize overweight solutions: return small value scaled by overflow
        overflow = (total_weight - capacity)
        total_value = max(0, total_value - overflow * OVERWEIGHT_PENALTY_FACTOR)
    return total_value, total_weight

def random_genome(n: int) -> Genome:
    """Generates a random genome of length n."""
    return [random.randint(0,1) for _ in range(n)]

def selection(population: list[Genome], fitnesses: list[int], k: int) -> Genome:
    """Performs tournament selection to choose genomes from the population.
    Note that other selection strategies exist such as roulette wheel, rank-based, etc.
    """
    contenders = random.sample(list(zip(population, fitnesses)), k)
    get_fitness = lambda x: x[1]
    return max(contenders, key=get_fitness)[0][:]

def crossover(a: Genome, b: Genome, p_crossover: float) -> tuple[Genome, Genome]:
    """Performs single-point crossover between two genomes.
    Note that other crossover strategies exist such as two-point crossover, uniform crossover, etc."""
    min_length = min(len(a), len(b))
    if random.random() > p_crossover or min_length < 2:
        return a[:], b[:]
    cutoff_point = random.randint(1, min_length - 1)
    return a[:cutoff_point]+b[cutoff_point:], b[:cutoff_point]+a[cutoff_point:]

def mutation(g: Genome, p_mutation: int) -> Genome:
    """Performs bit-flip mutation on a genome.
    Note that other mutation strategies exist such as swap mutation, scramble mutation, etc.
    """
    return [(1 - gene) if random.random() < p_mutation else gene for gene in g]

def run_ga(
    items: list[Item],
    capacity: int,
    pop_size=POPULATION_SIZE,
    generations=GENERATIONS,
    p_crossover=CROSSOVER_PROBABILITY,
    p_mutation=MUTATION_PROBABILITY,
    tournament_k=TOURNAMENT_K,
    elitism=ELITISM,
):
    """Runs the genetic algorithm to solve the knapsack problem."""
    n = len(items)
    population = [random_genome(n) for _ in range(pop_size)]
    best_history = []  # track best fitness per generation
    avg_history = []
    best_overall = None
    best_fit_overall = -1

    for _ in range(generations):
        fitnesses = [evaluate(genome, items, capacity)[0] for genome in population]
        best_fit = max(fitnesses)
        best_idx = fitnesses.index(best_fit)
        best_history.append(best_fit)
        avg_fit = sum(fitnesses) / pop_size
        avg_history.append(avg_fit)

        if best_fit > best_fit_overall:
            best_fit_overall = best_fit
            best_overall = population[best_idx][:]

        # Elitism
        get_fitness = lambda i: fitnesses[i]
        elite_indices = sorted(range(pop_size), key=get_fitness, reverse=True)[:elitism] # Sort the population by fitness and get the top `elitism` indices
        elites = [population[i][:] for i in elite_indices] # Make nepo babies

        # New generation
        new_pop = elites[:]
        while len(new_pop) < pop_size:
            parent1 = selection(population, fitnesses, k=tournament_k)
            parent2 = selection(population, fitnesses, k=tournament_k)
            child1, child2 = crossover(parent1, parent2, p_crossover)
            child1 = mutation(child1, p_mutation)
            child2 = mutation(child2, p_mutation)
            new_pop.extend([child1, child2])
        population = new_pop[:pop_size]

    # Final evaluation of the best
    best_value, best_weight = evaluate(best_overall, items, capacity)
    return {
        "best_genome": best_overall,
        "best_value": best_value,
        "best_weight": best_weight,
        "capacity": capacity,
        "best_history": best_history,
        "avg_history": avg_history,
    }

result = run_ga(items, capacity)

best_items = [items[i] for i, bit in enumerate(result["best_genome"]) if bit == 1]

print(f"Knapsack capacity: {result["capacity"]}")
print(f"Best solution: value = {result["best_value"]}, weight = {result["best_weight"]}")

# print("Items included in the best solution:", best_items)

# import matplotlib.pyplot as plt

# # Plot fitness curves
# plt.figure()
# plt.plot(result["best_history"], label="Best fitness")
# plt.plot(result["avg_history"], label="Average fitness")
# plt.title("GA on Knapsack: Fitness over Generations")
# plt.xlabel("Generation")
# plt.ylabel("Fitness")
# plt.legend()
# plt.tight_layout()
# plt.show()
