#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Gravitational Search Algorithm: 
Reference: https://link.springer.com/article/10.1007/s11042-020-09831-4#:~:text=Gravitational%20search%20algorithm%20is%20a,efficiently%20solve%20complex%20optimization%20problems.

import numpy as np

def gravitational_search_algorithm(objective_function, num_agents, num_dimensions, num_iterations, lower_bound, upper_bound):
    """
    Gravitational Search Algorithm (GSA) for optimization.

    Args:
        objective_function (callable): The objective function to be minimized.
        num_agents (int): The number of agents (particles) in the population.
        num_dimensions (int): The number of dimensions (variables) in the problem.
        num_iterations (int): The number of iterations.
        lower_bound (float): The lower bound for each dimension.
        upper_bound (float): The upper bound for each dimension.

    Returns:
        np.ndarray: The best-found solution vector.
        float: The objective value of the best-found solution.

    Raises:
        ValueError: If input parameters are invalid.
    """
    if num_agents <= 0 or num_dimensions <= 0 or num_iterations <= 0:
        raise ValueError("Invalid input parameters")

    agents = np.random.uniform(lower_bound, upper_bound, (num_agents, num_dimensions))
    velocities = np.zeros((num_agents, num_dimensions))
    best_agent = agents[0]
    best_value = objective_function(best_agent)

    for iteration in range(num_iterations):
        for i in range(num_agents):
            for j in range(num_agents):
                if i != j:
                    distance = np.linalg.norm(agents[i] - agents[j])
                    force = (G * agents[i] * agents[j]) / (distance ** epsilon)
                    acceleration = force / mass
                    velocities[i] += acceleration

            agents[i] += velocities[i]
            agents[i] = np.clip(agents[i], lower_bound, upper_bound)
            current_value = objective_function(agents[i])

            if current_value < best_value:
                best_agent = agents[i]
                best_value = current_value

    return best_agent, best_value

if __name__ == "__main__":
    # Define your objective function here
    def sphere(x):
        return sum(x**2)

    G = 6.67430e-11  # Gravitational constant
    mass = 1.0  # Mass of an agent
    epsilon = 1.0  # Gravitational constant

    # Example usage
    best_solution, best_value = gravitational_search_algorithm(sphere, 20, 10, 100, -5, 5)
    # Return results without additional print statements
    # You can use doctests to demonstrate how to use the function and test cases.

