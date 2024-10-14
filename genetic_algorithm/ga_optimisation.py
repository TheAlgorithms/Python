import numpy as np


class GeneticAlgorithm:
    def __init__(
        self,
        func,
        bounds,
        pop_size=20,
        generations=100,
        mutation_rate=0.1,
        crossover_rate=0.8,
        selection_method="tournament",
    ):
        self.func = func
        self.bounds = bounds
        self.pop_size = pop_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.selection_method = selection_method

    def initialize_population(self):
        # Create random population within the bounds
        dim = len(self.bounds)
        return np.array(
            [
                np.random.uniform(self.bounds[d][0], self.bounds[d][1], self.pop_size)
                for d in range(dim)
            ]
        ).T

    def fitness(self, individual):
        # Calculate fitness (for minimization, return function value)
        return self.func(*individual)

    def selection(self, population, fitness_values):
        if self.selection_method == "tournament":
            return self.tournament_selection(population, fitness_values)
        elif self.selection_method == "roulette":
            return self.roulette_wheel_selection(population, fitness_values)

    def tournament_selection(self, population, fitness_values):
        indices = np.random.choice(len(population), size=2, replace=False)
        return (
            population[indices[0]]
            if fitness_values[indices[0]] < fitness_values[indices[1]]
            else population[indices[1]]
        )

    def roulette_wheel_selection(self, population, fitness_values):
        fitness_sum = np.sum(1.0 / (1 + fitness_values))  # inverse for minimization
        pick = np.random.uniform(0, fitness_sum)
        current = 0
        for individual, fitness in zip(population, fitness_values):
            current += 1.0 / (1 + fitness)
            if current > pick:
                return individual

    def crossover(self, parent1, parent2):
        if np.random.rand() < self.crossover_rate:
            # Uniform crossover
            mask = np.random.rand(len(parent1)) < 0.5
            child = np.where(mask, parent1, parent2)
            return child
        return parent1

    def mutate(self, individual):
        for i in range(len(individual)):
            if np.random.rand() < self.mutation_rate:
                individual[i] += np.random.uniform(-1, 1)
                individual[i] = np.clip(
                    individual[i], self.bounds[i][0], self.bounds[i][1]
                )
        return individual

    def run(self):
        population = self.initialize_population()
        best_individual = None
        best_fitness = float("inf")

        for generation in range(self.generations):
            fitness_values = np.array([self.fitness(ind) for ind in population])

            # Track the best solution
            current_best_index = np.argmin(fitness_values)
            if fitness_values[current_best_index] < best_fitness:
                best_fitness = fitness_values[current_best_index]
                best_individual = population[current_best_index]

            # Create new generation
            new_population = []
            for _ in range(self.pop_size):
                parent1 = self.selection(population, fitness_values)
                parent2 = self.selection(population, fitness_values)
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                new_population.append(child)

            population = np.array(new_population)

            # Termination Condition: Minimal improvement
            if (
                generation > 1
                and abs(best_fitness - self.fitness(best_individual)) < 1e-6
            ):
                break

        return best_individual, best_fitness


# Example Usage:
def my_function(x, y):
    return x**2 + y**2


bounds = [(-10, 10), (-10, 10)]
ga = GeneticAlgorithm(func=my_function, bounds=bounds, pop_size=30, generations=100)
best_solution, best_value = ga.run()
print(f"Optimized Solution: {best_solution}, Function Value: {best_value}")
