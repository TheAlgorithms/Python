from collections.abc import Callable

from numpy.random import rand, randint

"""
This program performs genetic evolution on a list of bits.
Its goal is to transform every bit to a 1, using mutations and crossovers.
https://en.wikipedia.org/wiki/Genetic_algorithm
"""


def goal(individual: list[int]) -> int:
    """
    Calculate the fitness score for an individual in the genetic evolution algorithm.

    The goal of the algorithm is to transform every bit to a 1, and the fitness
    score is the negation of the sum of the bits.

    Parameters:
    - individual: A list representing an individual in the population.

    Returns:
    - The fitness score for the individual.

    Examples:
    >>> goal([1, 1, 1, 1, 1, 1, 1, 1])
    -8
    >>> goal([0, 0, 0, 0, 0, 0, 0, 0])
    0
    >>> goal([1, 0, 1, 0, 1, 0, 1, 0])
    -4
    """
    return -sum(individual)


def selection(population: list, scores: list[int], num: int) -> list:
    """
    Select individuals from the population based on tournament selection.

    Tournament selection involves randomly selecting num individuals from the
    population and choosing the one with the highest fitness score.

    Parameters:
    - population: The list of individuals in the population.
    - scores: The corresponding fitness scores for each individual.
    - k: The number of individuals to select in each tournament.

    Returns:
    - The selected individual from the tournament.

    Examples:
    >>> population = [[1, 0, 1, 1, 0], [0, 1, 0, 0, 1], [1, 1, 1, 0, 1]]
    >>> scores = [-2, -3, -1]
    >>> selection(population, scores, 2) in population
    True

    >>> population = [[0, 1, 1, 1, 0], [1, 0, 0, 1, 1], [0, 1, 0, 0, 1]]
    >>> scores = [-1, -3, -2]
    >>> selection(population, scores, 3) in population
    True

    >>> population = [[1, 1, 0, 1, 0], [0, 0, 1, 1, 1], [1, 0, 0, 0, 1]]
    >>> scores = [-2, -3, -1]
    >>> selection(population, scores, 1) not in population
    False
    """
    select = randint(len(population))
    for i in randint(0, len(population), num - 1):
        if scores[i] < scores[select]:
            select = i
    return population[select]


def crossover(parent1: list, parent2: list, crossover_rate: float) -> tuple[list, list]:
    """
    Perform crossover between two parents to produce two children.

    Crossover occurs with a probability determined by the crossover rate.
    If crossover happens, a random crossover point is chosen, and the bits
    beyond that point are swapped between the parents to create two children.

    Parameters:
    - parent1: The first parent bitstring.
    - parent2): The second parent bitstring.
    - crossover_rate: The probability of crossover between parents.

    Returns:
    - Two children resulting from the crossover.

    Examples:
    >>> parent1 = [1, 1, 1, 1, 1, 0]
    >>> parent2 = [0, 0, 0, 0, 0, 0]
    >>> child1, child2 = crossover(parent1, parent2, 0.8)
    >>> assert all(bit in {0, 1} for bit in child1 + child2)
    >>> assert child1.count(1) + child2.count(1) == parent1.count(1) + parent2.count(1)

    >>> parent1 = [1, 1, 1, 1, 1]
    >>> parent2 = [0, 0, 0, 0, 0]
    >>> child1, child2 = crossover(parent1, parent2, 0.2)
    >>> assert all(bit in {0, 1} for bit in child1 + child2)
    >>> assert child1.count(1) + child2.count(1) == parent1.count(1) + parent2.count(1)

    >>> parent1 = [1, 0, 1, 0, 1, 0]
    >>> parent2 = [0, 1, 0, 1, 0, 1]
    >>> child1, child2 = crossover(parent1, parent2, 0.5)
    >>> assert set(child1 + child2) == set(parent1 + parent2)
    >>> assert all(bit in {0, 1} for bit in child1 + child2)
    """
    child1 = parent1.copy()
    child2 = parent2.copy()
    if rand() < crossover_rate:
        crossover_point = randint(1, len(parent1) - 2)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


def mutate(bitstring: list, mutation_rate: float) -> None:
    """
    Mutates the bitstring based on the given mutation rate.

    Parameters:
    - bitstring: The binary string to be mutated.
    - mutation_rate: The probability of mutation for each bit in the bitstring.

    Examples:
    >>> bitstring = [1, 0, 1, 0, 1, 0]
    >>> mutation_rate = 0.2
    >>> mutate(bitstring, mutation_rate)
    >>> assert all(bit in [0, 1] for bit in bitstring)
    >>> assert bitstring.count(1) + bitstring.count(0) == len(bitstring)
    >>> # Ensure that the number of bits flipped is within the expected range.
    >>> assert 0 <= bitstring.count(1) <= len(bitstring)
    >>> assert 0 <= bitstring.count(0) <= len(bitstring)
    """
    for i in range(len(bitstring)):
        if rand() <= mutation_rate:
            bitstring[i] ^= 1


def one_max(
    goal: Callable[[list[int]], int],
    bit_count: int,
    iterations: int,
    pop_size: int,
    crossover_rate: float,
    mutation_rate: float,
) -> list[int]:
    """
    Perform genetic evolution to maximize the one_max goal.

    The goal is to transform a binary string to have all 1s.

    Parameters:
    - goal: The goal function to be maximized.
    - bit_count: The length of the binary strings.
    - iterations: The number of generations to run the genetic algorithm.
    - pop_size: The size of the population in each generation.
    - crossover_rate: The probability of crossover between individuals.
    - mutation_rate: The probability of mutation for each bit in an individual.

    Returns:
    - The best individual and its score after the evolution process.

    Examples:
    >>> from io import StringIO
    >>> import sys
    >>> goal = lambda individual: -sum(individual)
    >>> bit_count = 16
    >>> iterations = 10
    >>> pop_size = 1000
    >>> crossover_rate = 0.98
    >>> mutation_rate = 1 / bit_count
    >>> old_stdout = sys.stdout
    >>> sys.stdout = StringIO()
    >>> try:
    ...     output = one_max(goal, bit_count, iterations,
    ...     pop_size, crossover_rate, mutation_rate)
    ... finally:
    ...     captured_output = sys.stdout.getvalue()
    ...     sys.stdout = old_stdout
    >>> best = output[0]
    >>> score = -output[1]
    >>> assert all(bit == 1 for bit in best)
    >>> assert score == bit_count
    >>> assert "Generation: " in captured_output
    """
    population = [randint(0, 2, bit_count).tolist() for _ in range(pop_size)]
    best = 0
    best_score = goal(population[0])
    for generation in range(iterations):
        scores = [goal(individual) for individual in population]
        for i in range(pop_size):
            if scores[i] < best_score:
                best = population[i]
                best_score = scores[i]
                print(
                    f"Generation: {generation}, "
                    f"Best Fit: {population[i]} "
                    f"Score: {-scores[i]}"
                )
        select = [selection(population, scores, 3) for _ in range(pop_size)]
        children = []
        for i in range(0, pop_size, 2):
            parent1 = select[i]
            parent2 = select[i + 1]
            for individual in crossover(parent1, parent2, crossover_rate):
                mutate(individual, mutation_rate)
                children.append(individual)
        population = children
    return [best, best_score]


iterations = 10
pop_size = 1000
crossover_rate = 0.98
bit_count = 16
mutation_rate = 1.0 / float(bit_count)
output = one_max(goal, bit_count, iterations, pop_size, crossover_rate, mutation_rate)
best = output[0]
score = -output[1]
# Score should be equal to bit_count
if score == bit_count:
    print("\n1s have been maximized.")
    print(f"{best} Score: {score}")
else:
    print("Genetic algorithm has failed. Try playing around with the input values.")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
