from numpy.random import rand, randint
from typing import Callable, Any

"""
This program performs genetic evolution on a list of bits.
Its goal is to transform every bit to a 1, using mutations and crossovers.
"""


# Goal of the algorithm, all 1s
def goal(x: list[int]) -> int:
    return -sum(x)


# Selects based on tournament of which has highest score
def selection(population: list, scores: list[int], k=3) -> list:
    select = randint(len(population))
    for i in randint(0, len(population), k - 1):
        if scores[i] < scores[select]:
            select = i
    return population[select]


# Crosses two parents, produces two children
def crossover(parent1: list, parent2: list, crossover_rate: float) -> tuple[list, list]:
    child1 = parent1.copy()
    child2 = parent2.copy()
    if rand() < crossover_rate:
        # Acts as genetic crossover in sexual reproduction
        crossover_point = randint(1, len(parent1) - 2)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


# Mutates bitstring based on mutation rate
def mutate(bitstring: list, mutation_rate: float) -> None:
    for i in range(len(bitstring)):
        if rand() <= mutation_rate:
            bitstring[i] ^= 1


# Core algorithm for genetic growth
def one_max(
    goal: Callable[[list[int]], int],
    bit_count: int,
    iterations: int,
    pop_size: int,
    crossover_rate: float,
    mutation_rate: float,
) -> list[int]:
    population = [randint(0, 2, bit_count).tolist() for _ in range(pop_size)]
    best = 0
    best_score = goal(population[0])
    # Loop over generations
    for generation in range(iterations):
        scores = [goal(individual) for individual in population]
        for i in range(pop_size):
            if scores[i] < best_score:
                best = population[i]
                best_score = scores[i]
                print(
                    "Generation: %d, Best Fit: %s Score: %d"
                    % (generation, population[i], -scores[i])
                )
        select = [selection(population, scores) for _ in range(pop_size)]
        # Next generation
        children = []
        for i in range(0, pop_size, 2):
            parent1 = select[i]
            parent2 = select[i + 1]
            # Crossover, mutate, and save for next generation
            for individual in crossover(parent1, parent2, crossover_rate):
                mutate(individual, mutation_rate)
                children.append(individual)
        population = children
    return [best, best_score]


iterations = 10
pop_size = 1000
crossover_rate = 0.98
bit_count = 16
mutation_rate = 1 / float(bit_count)
output = one_max(goal, bit_count, iterations, pop_size, crossover_rate, mutation_rate)
best = output[0]
score = -output[1]
# Score should be equal to bit_count
if score == bit_count:
    print("\n1s have been maximised.")
    print("{} Score: {}".format(best, score))
else:
    print("Genetic algorithm has failed. Try playing around with the input values.")
