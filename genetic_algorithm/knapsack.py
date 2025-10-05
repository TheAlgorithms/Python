"""Did you know that Genetic Algorithms can be used to quickly approximate
combinatorial optimization problems such as knapsack?

Run doctests:
    python -m doctest -v ga_knapsack.py
"""

import random
from dataclasses import dataclass

# Keep module-level RNG deterministic for examples that rely on random,
# but individual doctests re-seed locally as needed.
random.seed(42)

# =========================== Problem setup: Knapsack ===========================

KNAPSACK_N_ITEMS: int = 42  # Number of items in the knapsack problem
KNAPSACK_VALUE_RANGE: tuple[int, int] = (10, 100)  # Range of item values
KNAPSACK_WEIGHT_RANGE: tuple[int, int] = (5, 50)  # Range of item weights
KNAPSACK_CAPACITY_RATIO: float = 0.5  # Capacity as a fraction of total weight


@dataclass
class Item:
    value: int
    weight: int


def generate_knapsack_instance(
    n_items: int,
    value_range: tuple[int, int],
    weight_range: tuple[int, int],
    capacity_ratio: float,
) -> tuple[list[Item], int]:
    """
    Generates a random knapsack problem instance.

    Returns a tuple: (items, capacity), where items is a list of Item(value, weight)
    and capacity is an int computed as floor(capacity_ratio * total_weight).

    Examples
    --------
    Use a tiny, deterministic instance to validate shape and capacity range:

    >>> random.seed(0)
    >>> items, cap = generate_knapsack_instance(
    ...     n_items=3,
    ...     value_range=(5, 5),
    ...     weight_range=(10, 10),
    ...     capacity_ratio=0.5
    ... )
    >>> len(items), cap
    (3, 15)
    >>> all(isinstance(it, Item) for it in items)
    True
    >>> [it.value for it in items], [it.weight for it in items]
    ([5, 5, 5], [10, 10, 10])
    """
    items = []
    for _ in range(n_items):
        value = random.randint(*value_range)
        weight = random.randint(*weight_range)
        items.append(Item(value=value, weight=weight))
    # Capacity as a fraction of total weight
    capacity = int(sum(it.weight for it in items) * capacity_ratio)
    return items, capacity


# Example instance (guarded by __main__ below for printing)
items, capacity = generate_knapsack_instance(
    n_items=KNAPSACK_N_ITEMS,
    value_range=KNAPSACK_VALUE_RANGE,
    weight_range=KNAPSACK_WEIGHT_RANGE,
    capacity_ratio=KNAPSACK_CAPACITY_RATIO,
)

# ============================== GA Representation ==============================

# HYPERPARAMETERS (For tuning the GA)

POPULATION_SIZE = 120
GENERATIONS = 200
CROSSOVER_PROBABILITY = 0.9
MUTATION_PROBABILITY = 0.01
TOURNAMENT_K = 3
ELITISM = 2

OVERWEIGHT_PENALTY_FACTOR = 10

genome_t = list[int]  # An index list where 1 means item is included, 0 means excluded


def evaluate(genome: genome_t, items: list[Item], capacity: int) -> tuple[int, int]:
    """
    Calculates fitness (value) and weight of a candidate solution. If overweight,
    the returned value is penalized; weight is the actual summed weight.

    Returns (value, weight).

    Examples
    --------
    Feasible genome (no penalty):

    >>> it = [Item(10, 4), Item(7, 3), Item(5, 2)]
    >>> genome = [1, 0, 1]  # take items 0 and 2
    >>> evaluate(genome, it, capacity=7)
    (15, 6)

    Overweight genome (penalty applies):
    Total value = 10+7+5 = 22, total weight = 9, capacity = 7, overflow = 2
    Penalized value = max(0, 22 - 2 * OVERWEIGHT_PENALTY_FACTOR) = 2

    >>> genome = [1, 1, 1]
    >>> evaluate(genome, it, capacity=7)
    (2, 9)
    """
    total_value = 0
    total_weight = 0
    for gene, item in zip(genome, items):
        if gene:
            total_value += item.value
            total_weight += item.weight
    if total_weight > capacity:
        overflow = total_weight - capacity
        total_value = max(0, total_value - overflow * OVERWEIGHT_PENALTY_FACTOR)
    return total_value, total_weight


def random_genome(length: int) -> genome_t:
    """
    Generates a random genome (list of 0/1) of length n.

    Examples
    --------
    Check length and content are 0/1 bits:

    >>> random.seed(123)
    >>> g = random_genome(5)
    >>> len(g), set(g).issubset({0, 1})
    (5, True)
    """
    return [random.randint(0, 1) for _ in range(length)]


def selection(
    population: list[genome_t], fitnesses: list[int], tournament_k: int
) -> genome_t:
    """
    Performs tournament selection to choose a genome from the population.

    Note that other selection strategies exist such as roulette wheel, rank-based, etc.

    Examples
    --------
    Deterministic tournament with fixed seed (k=2):

    >>> random.seed(1)
    >>> pop = [[0,0,0], [1,0,0], [1,1,0], [1,1,1]]
    >>> fits = [0, 5, 9, 7]
    >>> parent = selection(pop, fits, k=2)
    >>> parent in pop
    True
    """
    contenders = random.sample(list(zip(population, fitnesses)), tournament_k)
    get_fitness = lambda contender: contender[1]
    return max(contenders, key=get_fitness)[0][:]


def crossover(
    genome_1: genome_t, genome_2: genome_t, p_crossover: float
) -> tuple[genome_t, genome_t]:
    """
    Performs single-point crossover between two genomes.
    If crossover does not occur (random > p_crossover) or genomes are too short,
    returns copies of the parents.

    Note: other crossover strategies exist (two-point, uniform, etc.).

    Examples
    --------
    Force crossover with p=1.0 and fixed RNG; verify lengths and bit content:

    >>> random.seed(2)
    >>> a, b = [0,0,0,0], [1,1,1,1]
    >>> c1, c2 = crossover(a, b, p_crossover=1.0)
    >>> len(c1) == len(a) == len(c2) == len(b)
    True
    >>> set(c1).issubset({0,1}) and set(c2).issubset({0,1})
    True

    No crossover if p=0.0:

    >>> c1, c2 = crossover([0,0,0], [1,1,1], p_crossover=0.0)
    >>> c1, c2
    ([0, 0, 0], [1, 1, 1])
    """
    min_length = min(len(genome_1), len(genome_2))
    if random.random() > p_crossover or min_length < 2:
        return genome_1[:], genome_2[:]
    cutoff_point = random.randint(1, min_length - 1)
    return genome_1[:cutoff_point] + genome_2[cutoff_point:], genome_2[
        :cutoff_point
    ] + genome_1[cutoff_point:]


def mutation(genome: genome_t, p_mutation: float) -> genome_t:
    """
    Performs bit-flip mutation on a genome. Each bit flips with probability p_mutation.

    Note: other mutation strategies exist (swap, scramble, etc.).

    Examples
    --------
    With probability 1.0, every bit flips:

    >>> mutation([0, 1, 1, 0], p_mutation=1.0)
    [1, 0, 0, 1]

    With probability 0.0, nothing changes:

    >>> mutation([0, 1, 1, 0], p_mutation=0.0)
    [0, 1, 1, 0]
    """
    return [(1 - gene) if random.random() < p_mutation else gene for gene in genome]


def run_ga(
    items: list[Item],
    capacity: int,
    pop_size: int = POPULATION_SIZE,
    generations: int = GENERATIONS,
    p_crossover: float = CROSSOVER_PROBABILITY,
    p_mutation: float = MUTATION_PROBABILITY,
    tournament_k: int = TOURNAMENT_K,
    elitism: int = ELITISM,
) -> dict:
    """
    Runs the genetic algorithm to (approximately) solve the knapsack problem.

    Returns a dict with keys:
      - 'best_genome' (genome_t)
      - 'best_value' (int)
      - 'best_weight' (int)
      - 'capacity' (int)
      - 'best_history' (list[int])
      - 'avg_history' (list[float])

    Examples
    --------
    Use a tiny instance and few generations to validate structure and lengths:

    >>> random.seed(1234)
    >>> tiny_items = [Item(5,2), Item(6,3), Item(2,1), Item(7,4)]
    >>> cap = 5
    >>> out = run_ga(
    ...     tiny_items, cap,
    ...     pop_size=10, generations=5,
    ...     p_crossover=0.9, p_mutation=0.05,
    ...     tournament_k=2, elitism=1
    ... )
    >>> sorted(out.keys())
    ['avg_history', 'best_genome', 'best_history', 'best_value', 'best_weight', 'capacity']
    >>> len(out['best_history']) == 5 and len(out['avg_history']) == 5
    True
    >>> isinstance(out['best_genome'], list) and isinstance(out['best_value'], int)
    True
    >>> out['capacity'] == cap
    True
    """
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
        elite_indices = sorted(range(pop_size), key=get_fitness, reverse=True)[:elitism]
        elites = [population[i][:] for i in elite_indices]

        # New generation
        new_pop = elites[:]
        while len(new_pop) < pop_size:
            parent1 = selection(population, fitnesses, tournament_k=tournament_k)
            parent2 = selection(population, fitnesses, tournament_k=tournament_k)
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


# ================================ Script entry =================================

if __name__ == "__main__":
    result = run_ga(items, capacity)
    best_items = [items[idx] for idx, bit in enumerate(result["best_genome"]) if bit == 1]

    print(f"Knapsack capacity: {result['capacity']}")
    print(
        f"Best solution: value = {result['best_value']}, weight = {result['best_weight']}"
    )
    # Uncomment to inspect chosen items:
    # print("Items included in the best solution:", best_items)

    # Optional: plot fitness curves
    # import matplotlib.pyplot as plt
    # plt.figure()
    # plt.plot(result["best_history"], label="Best fitness")
    # plt.plot(result["avg_history"], label="Average fitness")
    # plt.title("GA on Knapsack: Fitness over Generations")
    # plt.xlabel("Generation")
    # plt.ylabel("Fitness")
    # plt.legend()
    # plt.tight_layout()
    # plt.show()
