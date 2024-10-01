import numpy as np

def parse_function(user_input):
    """
    Convert user input from f(x, y) = x^2 + y^2 to a valid Python function.

    Parameters:
        user_input (str): The user-defined fitness function in string format.

    Returns:
        str: The function code as a string.

    Examples:
        >>> parse_function("f(x, y) = x^2 + y^2")
        'def fitness(x):\\n    return x[0]**2 + x[1]**2'
    """
    user_input = user_input.strip()
    
    if "=" in user_input:
        _, expression = user_input.split("=", 1)
        expression = expression.strip()
    else:
        raise ValueError("Invalid function format. Please use 'f(x, y) = ...'.")

    function_code = "def fitness(x):\n"
    function_code += f"    return {expression.replace('^', '**').replace('x', 'x[0]').replace('y', 'x[1]')}\n"
    
    return function_code

def genetic_algorithm(user_fitness_function) -> None:
    """
    Execute the genetic algorithm to optimize the user-defined fitness function.

    Parameters:
        user_fitness_function (function): The fitness function to be optimized.
        
    Returns:
        None

    Example:
        >>> def example_fitness_function(x):
        ...     return x[0]**2 + x[1]**2
        >>> genetic_algorithm(example_fitness_function)  # This will print outputs
    """
    rng = np.random.default_rng()  # New random number generator
    population_size = 100
    num_generations = 500
    mutation_rate = 0.01
    chromosome_length = 2
    best_fitness = np.inf
    best_solution = None

    population = rng.random((population_size, chromosome_length))

    for generation in range(num_generations):
        fitness_values = []

        for individual in population:
            fitness_value = user_fitness_function(individual)

            if fitness_value is None:
                print(f"Warning: Fitness function returned None for individual {individual}.")
                fitness_value = np.inf
            else:
                print(f"Evaluating individual {individual}, Fitness: {fitness_value:.6f}")

            fitness_values.append(fitness_value)

        fitness_values = np.array(fitness_values)

        best_idx = np.argmin(fitness_values)
        if fitness_values[best_idx] < best_fitness:
            best_fitness = fitness_values[best_idx]
            best_solution = population[best_idx]

        print(f"Generation {generation + 1}, Best Fitness: {best_fitness:.6f}")

        selected_parents = population[rng.choice(population_size, population_size)]

        offspring = []
        for i in range(0, population_size, 2):
            parent1, parent2 = selected_parents[i], selected_parents[i + 1]
            cross_point = rng.integers(1, chromosome_length)
            child1 = np.concatenate((parent1[:cross_point], parent2[cross_point:]))
            child2 = np.concatenate((parent2[:cross_point], parent1[cross_point:]))
            offspring.append(child1)
            offspring.append(child2)

        offspring = np.array(offspring)
        mutation_mask = rng.random((population_size, chromosome_length)) < mutation_rate
        offspring[mutation_mask] = rng.random(np.sum(mutation_mask))

        population = offspring

    print("\n--- Optimization Results ---")
    print(f"User-defined function: f(x, y) = {user_input.split('=')[1].strip()}")
    print(f"Best Fitness Value (Minimum): {best_fitness:.6f}")
    print(f"Optimal Solution Found: x = {best_solution[0]:.6f}, y = {best_solution[1]:.6f}")

    function_value = best_fitness
    print(f"Function Value at Optimal Solution: f({best_solution[0]:.6f}, {best_solution[1]:.6f}) = {function_value:.6f}")

if __name__ == "__main__":
    user_input = input("Please enter your fitness function in the format 'f(x, y) = ...':\n")

    try:
        fitness_function_code = parse_function(user_input)
        exec(fitness_function_code, globals())
    except (SyntaxError, ValueError) as e:
        print(f"Error: {e}")
    except NameError as e:
        print(f"Error: {e}")

    if 'fitness' in globals():
        if 'fitness' in globals():
            genetic_algorithm(globals()['fitness'])
        else:
            print("No valid fitness function provided.")
    else:
        print("No valid fitness function provided.")
