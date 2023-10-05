#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Gravitational Search Algorithm

Author - Vivek Kumar Sahu
Email- vivekkumarsahu979@gmail.com

Requirements:
  - numpy
  - matplotlib (for visualization, optional)
Python:
  - 3.6 or higher
Inputs:
  - n_agents, number of agents (int)
  - n_dimensions, number of problem dimensions (int)
  - n_iterations, number of iterations for the algorithm (int)
  - search_space, a list of tuples defining the search space for each dimension
  - objective_function, a function that takes an agent's position and returns its fitness value
  - G0, initial gravitational constant (float)
  - alpha, gravitational scaling factor (float)
  - beta, attraction scaling factor (float)
Usage:
  1. Define the problem by specifying the search space and objective function.
  2. Initialize the algorithm with parameters: n_agents, n_dimensions, n_iterations, search_space, objective_function, G0, alpha, beta.
  3. Run the algorithm using the `run_gsa` function.
  4. Access the best solution and fitness value after the algorithm converges.
Reference: https://link.springer.com/article/10.1007/s11042-020-09831-4#:~:text=Gravitational%20search%20algorithm%20is%20a,efficiently%20solve%20complex%20optimization%20problems.
"""

import numpy as np
import matplotlib.pyplot as plt  # Optional for visualization

TAG = "GRAVITATIONAL-SEARCH-ALGORITHM/ "

def initialize_agents(n_agents, n_dimensions, search_space):
    """
    Initialize agents with random positions within the search space.

    Parameters:
    - n_agents (int): Number of agents.
    - n_dimensions (int): Number of problem dimensions.
    - search_space (list of tuples): Defines the search space for each dimension.

    Returns:
    - agents (numpy.ndarray): Array of agents' positions.
    """
    agents = np.random.rand(n_agents, n_dimensions)
    for i, dimension in enumerate(search_space):
        agents[:, i] = agents[:, i] * (dimension[1] - dimension[0]) + dimension[0]
    return agents

def calculate_fitness(agents, objective_function):
    """
    Calculate fitness values for each agent based on the objective function.

    Parameters:
    - agents (numpy.ndarray): Array of agents' positions.
    - objective_function (function): Objective function to optimize.

    Returns:
    - fitness (numpy.ndarray): Array of fitness values.
    """
    fitness = np.array([objective_function(agent) for agent in agents])
    return fitness

def update_agents(agents, G, alpha, beta):
    """
    Update agents' positions based on gravitational search algorithm.

    Parameters:
    - agents (numpy.ndarray): Array of agents' positions.
    - G (float): Gravitational constant.
    - alpha (float): Gravitational scaling factor.
    - beta (float): Attraction scaling factor.

    Returns:
    - agents (numpy.ndarray): Updated array of agents' positions.
    """
    n_agents, n_dimensions = agents.shape
    for i in range(n_agents):
        for j in range(n_agents):
            if i != j:
                r = np.linalg.norm(agents[i] - agents[j])
                F = G / (1 + alpha * r**beta)
                direction = (agents[j] - agents[i]) / r
                agents[i] += F * direction
    return agents

def run_gsa(n_agents, n_dimensions, n_iterations, search_space, objective_function, G0, alpha, beta):
    """
    Run the Gravitational Search Algorithm.

    Parameters:
    - n_agents (int): Number of agents.
    - n_dimensions (int): Number of problem dimensions.
    - n_iterations (int): Number of iterations.
    - search_space (list of tuples): Defines the search space for each dimension.
    - objective_function (function): Objective function to optimize.
    - G0 (float): Initial gravitational constant.
    - alpha (float): Gravitational scaling factor.
    - beta (float): Attraction scaling factor.

    Returns:
    - best_agent (numpy.ndarray): Best agent's position.
    - best_fitness (float): Best fitness value found.
    """
    agents = initialize_agents(n_agents, n_dimensions, search_space)
    best_fitness = float('inf')
    best_agent = None
    for iteration in range(n_iterations):
        fitness = calculate_fitness(agents, objective_function)
        min_fitness = np.min(fitness)
        if min_fitness < best_fitness:
            best_fitness = min_fitness
            best_agent = agents[np.argmin(fitness)]
        G = G0 / (1 + iteration)
        agents = update_agents(agents, G, alpha, beta)
    return best_agent, best_fitness

if __name__ == "__main__":
    # Example usage:
    def objective_function(x):
        return np.sum(x**2)  # Minimize the sum of squares

    n_agents = 50
    n_dimensions = 2
    n_iterations = 100
    search_space = [(-5, 5), (-5, 5)]  # Search space for 2 dimensions
    G0 = 100.0
    alpha = 0.1
    beta = 2.0

    best_agent, best_fitness = run_gsa(
        n_agents, n_dimensions, n_iterations, search_space, objective_function, G0, alpha, beta
    )

    print(f"Best Agent: {best_agent}")
    print(f"Best Fitness Value: {best_fitness}")

