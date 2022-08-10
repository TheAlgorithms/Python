#!/usr/bin/env python3

from __future__ import annotations

import random


def order_based_crossover(parent1: list, parent2: list):
    """
    In the Travelling Salesman Problem, each travelling path must be valid. 
    Each path consists all cities in the set, and each path visits each of the 
    cities once only. So, none of the cities are visited more than once. 
    Therefore, Order Crossover (OX) proposed to eliminate the duplication of cities.

    >>> order_based_crossover([(4672,1791), (6248,5294), (4116,4225), (6178,2991)], 
    [(6178,2991), (4672,1791), (4116,4225), (6248,5294)])
    [(6178,2991), (6248,5294), (4672,1791), (4116,4225)]
    [(6248,5294), (4672,1791), (4116,4225), (6178,2991)]
    >>> order_based_crossover([(2360,4809), (6233,5420), (6248,5294), (84,4787)]], 
    [(6248,5294), (6233,5420), (84,4787), (2360,4809)])
    [(2360,4809), (6248,5294), (6233,5420), (84,4787)]
    [(6248,5294), (2360,4809), (6233,5420), (84,4787)]
    
    """

    size = len(parent1)

    # Choose random start/end position for crossover
    child1, child2 = [-1] * size, [-1] * size
    start, end = sorted(random.randrange(size) for _ in range(2))

    # Replicate parent1's sequence for child1, parent2's sequence for child2
    child1_inherited = []
    child2_inherited = []
    for i in range(start, end + 1):
        child1[i] = parent1[i]
        child2[i] = parent2[i]
        child1_inherited.append(parent1[i])
        child2_inherited.append(parent2[i])

    # Fill the remaining position with the other parents' entries
    current_parent1_position, current_parent2_position = 0, 0

    # Ordered Crossover bet. parent2 & child1
    i = 0
    while i < size:
        child1_gene = child1[i]
        if child1_gene == -1:
            parent2_trait = parent2[current_parent2_position]
            while parent2_trait in child1_inherited:
                current_parent2_position += 1
                parent2_trait = parent2[current_parent2_position]
            child1[i] = parent2_trait
            child1_inherited.append(parent2_trait)
        else:
            i += 1

    # Ordered Crossover bet. parent1 & child2
    j = 0
    while j < size:
        child2_gene = child2[j]
        if child2_gene == -1:
            parent1_trait = parent1[current_parent1_position]
            while parent1_trait in child2_inherited:
                current_parent1_position += 1
                parent1_trait = parent1[current_parent1_position]
            child2[j] = parent1_trait
            child2_inherited.append(parent1_trait)
        else:
            j += 1

    return child1, child2

if __name__ == "__main__":
    import doctest

    doctest.testmod()
