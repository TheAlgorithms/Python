"""
GENETIC ALGORITHM USING ORDER CROSSOVER,
SWAP MUTATION AND BINARY TOURNAMENT SELECTION
TO SOLVE THE TRAVELLING SALESMAN PROBLEM
https://en.wikipedia.org/wiki/Genetic_algorithm
https://en.wikipedia.org/wiki/Travelling_salesman_problem
Author: joydipb01
"""

import random
import sys

import numpy as np
import tsplib95

# Define necessary parameters - population size, total no. of generations, etc:
TOTAL_POPULATION = 100
PROB_MUTATION, PROB_CROSSOVER = 0.1, 0.9  # Mutation Probability, Crossover Probability
TOTAL_GENERATIONS = 100


def readinp(filename: str) -> tsplib95.models.Problem:
    """
    Loads the Traveling Salesman Problem (TSP) from the provided file using
    the tsplib95 package. This file should follow the .tsp format and contain
    city coordinates and possibly other metadata. This file is passed as a
    command-line argument.
    Sample .tsp files can be found here:
    http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/

    Args:
    filename (str): Path to the .tsp file.

    Returns:
    problem (tsplib95.models.Problem): The TSP problem object containing
    nodes and distances.

    Example:
    >>> import tsplib95
    >>> tsp_data = '''
    ... NAME: sample
    ... TYPE: TSP
    ... DIMENSION: 4
    ... EDGE_WEIGHT_TYPE: EUC_2D
    ... NODE_COORD_SECTION
    ... 1 0 0
    ... 2 1 0
    ... 3 0 1
    ... 4 1 1
    ... EOF
    ... '''
    >>> tsp_filename = "sample.tsp"
    >>> with open(tsp_filename, "w") as f:
    ...     f.write(tsp_data)
    >>> prob = readinp('sample.tsp')
    >>> len(list(prob.get_nodes())) > 0
    True
    >>> isinstance(prob, tsplib95.models.StandardProblem)
    True
    """
    problem = tsplib95.load(filename)
    return problem


def fitness(mem: list[int], dist_mat: np.ndarray) -> float:
    """
    Calculates the fitness of a given solution (tour). The fitness is the
    inverse of the total distance of the tour. A shorter distance results in
    a higher fitness.

    Args:
    mem (list): A tour (list of city indices) representing a potential solution.
    dist_mat (numpy array): Distance matrix with pairwise distances between cities.

    Returns:
    float: The fitness of the tour, which is 1 / total distance of the tour.

    Example:
    >>> dist_mat = np.array([[0, 2, 9], [2, 0, 3], [9, 3, 0]])
    >>> mem = [0, 1, 2]
    >>> round(fitness(mem, dist_mat), 3)
    0.091
    """
    dist = 0
    for i in range(len(mem)):
        j = (i + 1) % len(mem)  # Ensures the last city connects to the first city
        dist += dist_mat[mem[i], mem[j]]
    fitness = 1.0 / dist  # Fitness is the inverse of total distance
    return fitness


def binary_tournament_selection(
    popln: list[list[int]], dist_mat: np.ndarray
) -> tuple[list[int], list[int]]:
    """
    Selects two parents from the population using binary tournament selection.
    Two individuals are randomly chosen, and the one with higher fitness is
    selected. This process is repeated until two parents are chosen.

    Args:
    popln (list): The current population of solutions (tours).
    dist_mat (numpy array): Distance matrix with pairwise distances between cities.

    Returns:
    tuple: Two selected parent tours from the population.

    Example:
    >>> dist_mat = np.array([[0, 2, 9], [2, 0, 3], [9, 3, 0]])
    >>> popln = [[0, 1, 2], [1, 0, 2], [2, 0, 1]]
    >>> p1, p2 = binary_tournament_selection(popln, dist_mat)
    >>> p1 in popln and p2 in popln
    True
    """
    select: list[list[int]] = []
    while len(select) != 2:
        i, j = random.sample(range(len(popln)), 2)  # Randomly select two individuals
        if fitness(popln[i], dist_mat) > fitness(popln[j], dist_mat):
            select.append(popln[i])  # Select the fitter individual
        else:
            select.append(popln[j])
    return select[0], select[1]


def order_crossover(
    p1: list[int], p2: list[int], crossover_prob: float
) -> tuple[list[int], list[int]]:
    """
    Applies order crossover (OX) between two parent solutions with a certain
    probability. The OX method ensures that the relative order of the cities
    is preserved in the offspring. If crossover does not occur, the parents
    are returned unchanged.

    Args:
    p1 (list): The first parent solution (tour).
    p2 (list): The second parent solution (tour).
    crossover_prob (float): The probability of crossover occurring.

    Returns:
    tuple: Two offspring tours resulting from the crossover.

    Example:
    >>> random.seed(42)
    >>> p1 = [0, 1, 2, 3]
    >>> p2 = [3, 2, 1, 0]
    >>> child1, child2 = order_crossover(p1, p2, 1.0)
    >>> child1
    [0, 2, 1, 3]
    >>> child2
    [3, 1, 2, 0]
    """
    if random.random() < crossover_prob:  # Perform crossover with given probability
        c1: list[int] = [-1] * len(p1)
        c2: list[int] = [-1] * len(p2)
        start = random.randint(0, len(p1) - 1)
        end = random.randint(start + 1, len(p1))
        c1[start:end] = p1[start:end]  # Copy a segment from parent 1 to child 1
        c2[start:end] = p2[start:end]  # Copy a segment from parent 2 to child 2
        for i in range(len(p2)):
            # Fill the remaining cities in child 1 and child 2
            if p2[i] not in c1:
                j = i
                while c1[j] != -1:
                    j = p2.index(p1[j])
                c1[j] = p2[i]
            if p1[i] not in c2:
                j = i
                while c2[j] != -1:
                    j = p1.index(p2[j])
                c2[j] = p1[i]
        return c1, c2
    return p1, p2  # No crossover, return the parents unchanged


def swap_mutation(child: list[int], mutation_prob: float, num_cities: int) -> list[int]:
    """
    Applies swap mutation to a child solution with a given probability.
    Two random cities in the tour are swapped to introduce variability.

    Args:
    child (list): The child solution (tour) to be mutated.
    mutation_prob (float): The probability of mutation occurring.
    num_cities (int): The number of cities in the problem.

    Returns:
    list: The mutated child solution.

    Example:
    >>> random.seed(42)
    >>> child = [0, 1, 2, 3]
    >>> swap_mutation(child, 1.0, 4)
    [0, 3, 2, 1]
    """
    if random.random() < mutation_prob:  # Perform mutation with given probability
        i, j = random.sample(range(num_cities), 2)  # Randomly select two cities to swap
        child[i], child[j] = child[j], child[i]  # Swap the cities
    return child


def two_opt_local_search(child: list[int], dist_mat: np.ndarray) -> list[int]:
    """
    Applies the 2-opt local search algorithm to improve a solution (tour).
    It repeatedly checks for pairs of edges in the tour and swaps them if
    it reduces the total distance of the tour, stopping when no further
    improvements are found.

    Args:
    child (list): The solution (tour) to be optimized.
    dist_mat (numpy array): Distance matrix with pairwise distances between cities.

    Returns:
    list: The optimized solution after applying 2-opt.

    Example:
    >>> dist_mat = np.array([[0, 2, 9], [2, 0, 3], [9, 3, 0]])
    >>> child = [0, 1, 2]
    >>> two_opt_local_search(child, dist_mat)
    [0, 1, 2]
    """
    while True:
        improvement = 0
        best_dist = fitness(child, dist_mat)
        for i in range(1, len(child) - 1):
            for j in range(i + 1, len(child)):
                # Generate a new solution by reversing the order of cities
                # between i and j
                new_child = (
                    child[:i] + list(reversed(child[i : j + 1])) + child[j + 1 :]
                )
                new_dist = fitness(new_child, dist_mat)
                if new_dist > best_dist:  # If the new solution is better, adopt it
                    child = new_child
                    improvement = 1
        if improvement == 0:  # Stop when no further improvements are found
            break
    return child


# Run the genetic algorithm:
if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: traveling_salesman_problem.py <name/path of .tsp file>")

    no_improvement = 0

    prob = readinp(sys.argv[1])
    n_cities = len(list(prob.get_nodes()))

    # Compute distance matrix:- distance between any two cities
    dist_mat = np.zeros((n_cities, n_cities))
    for i in range(n_cities):
        for j in range(i + 1, n_cities):
            node1 = prob.node_coords[i + 1]
            node2 = prob.node_coords[j + 1]
            dist_mat[i, j] = dist_mat[j, i] = np.linalg.norm(
                np.array(node1) - np.array(node2)
            )

    # Generate initial population (first city is taken to be depot by default):
    popln: list = []
    while len(popln) < TOTAL_POPULATION:
        sol_dist = 0.0
        individual = list(range(n_cities))
        subindiv = individual[1:]
        random.shuffle(subindiv)
        individual[1:] = subindiv
        popln.append(individual)

    for iteration in range(TOTAL_GENERATIONS):
        # Binary Tournament Selection:
        parent1, parent2 = binary_tournament_selection(popln, dist_mat)

        # Order Crossover:
        child1, child2 = order_crossover(parent1, parent2, PROB_CROSSOVER)

        # Swap Mutation for child-1:
        child1 = swap_mutation(child1, PROB_MUTATION, n_cities)

        # Swap Mutation for child-2:
        child1 = swap_mutation(child2, PROB_MUTATION, n_cities)

        # 2-opt for child-1:
        child1 = two_opt_local_search(child1, dist_mat)

        # 2-opt for child-2:
        child2 = two_opt_local_search(child2, dist_mat)

        child1_fitness = fitness(child1, dist_mat)
        child2_fitness = fitness(child2, dist_mat)

        # Individual of worst fitness replaced by fittest of the children:
        worst_fit = np.argmin([fitness(individual, dist_mat) for individual in popln])
        if child1_fitness > child2_fitness:
            popln[worst_fit] = child1
        else:
            popln[worst_fit] = child2

        # Sort population based on fitnesses (first member will be the solution):
        popln.sort(key=lambda member: fitness(member, dist_mat), reverse=True)

        # Checking for improvements in solution:
        if sol_dist == fitness(popln[0], dist_mat):
            no_improvement += 1
        else:
            sol = popln[0]
            sol_dist = fitness(sol, dist_mat)
            print("New fitness at Generation", iteration + 1, "is:", 1 / sol_dist)
        if (
            no_improvement == 15
        ):  # Break if there is no improvement after 15 generations
            break

    print()
    fsol = [x + 1 for x in sol]
    print("Final Solution:", fsol)
    print("Final Fitness:", 1 / sol_dist)
