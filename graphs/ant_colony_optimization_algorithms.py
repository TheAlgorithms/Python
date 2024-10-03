import random
import math

# Define cities as coordinates (x, y)
cities = {
    0: [0, 0],
    1: [0, 5],
    2: [3, 8],
    3: [8, 10],
    4: [12, 8],
    5: [12, 4],
    6: [8, 0],
    7: [6, 2],
}


def euclidean_distance(city1: list[int], city2: list[int]) -> float:
    """
    Calculate the Euclidean distance between two cities (points).
    """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def initialize_pheromone_matrix(size: int) -> list[list[float]]:
    """
    Initialize the pheromone matrix with 1.0 values.
    """
    return [[1.0 for _ in range(size)] for _ in range(size)]


def compute_distance_matrix(cities: dict[int, list[int]]) -> list[list[float]]:
    """
    Precompute the distance between all cities and store them in a matrix.
    """
    size = len(cities)
    dist_matrix = [[0.0] * size for _ in range(size)]
    for i in range(size):
        for j in range(i + 1, size):
            dist = euclidean_distance(cities[i], cities[j])
            dist_matrix[i][j] = dist
            dist_matrix[j][i] = dist
    return dist_matrix


def select_next_city(
    current_city: int,
    unvisited: list[int],
    pheromone: list[list[float]],
    distances: list[list[float]],
    alpha: float,
    beta: float,
) -> int:
    """
    Select the next city to visit based on pheromone levels and distances.
    """
    probabilities = []
    for city in unvisited:
        pheromone_level = pheromone[current_city][city] ** alpha
        distance_factor = (1 / distances[current_city][city]) ** beta
        probabilities.append(pheromone_level * distance_factor)

    # Normalize probabilities
    total = sum(probabilities)
    probabilities = [p / total for p in probabilities]

    # Randomly select next city based on the probabilities
    return random.choices(unvisited, weights=probabilities)[0]


def update_pheromones(
    pheromone: list[list[float]],
    ants_paths: list[list[int]],
    distances: list[list[float]],
    q: float,
    evaporation_rate: float,
    best_path: list[int],
    best_distance: float,
) -> tuple[list[list[float]], list[int], float]:
    """
    Update pheromone levels on the paths chosen by ants.
    """
    size = len(pheromone)

    # Evaporate pheromones
    for i in range(size):
        for j in range(size):
            pheromone[i][j] *= 1 - evaporation_rate

    # Update pheromones based on ants' paths
    for path in ants_paths:
        total_distance = sum(
            distances[path[i]][path[i + 1]] for i in range(len(path) - 1)
        )
        pheromone_deposit = q / total_distance

        for i in range(len(path) - 1):
            pheromone[path[i]][path[i + 1]] += pheromone_deposit
            pheromone[path[i + 1]][path[i]] += pheromone_deposit

        # Check if this is the best path found
        if total_distance < best_distance:
            best_distance = total_distance
            best_path = path

    return pheromone, best_path, best_distance


def ant_colony_optimization(
    cities: dict[int, list[int]],
    ants_num: int,
    iterations: int,
    alpha: float,
    beta: float,
    evaporation_rate: float,
    q: float,
) -> tuple[list[int], float]:
    """
    Solve the TSP using Ant Colony Optimization (ACO).
    """
    cities_num = len(cities)
    if cities_num == 0:
        return [], float("inf")  # No cities to visit

    # Initialize pheromone and distance matrices
    pheromone = initialize_pheromone_matrix(cities_num)
    distances = compute_distance_matrix(cities)

    best_path = []
    best_distance = float("inf")

    for _ in range(iterations):
        all_paths = []
        for _ in range(ants_num):
            unvisited = list(range(1, cities_num))  # Start from city 0
            path = [0]  # Start at city 0

            # Construct path for the ant
            current_city = 0
            while unvisited:
                next_city = select_next_city(
                    current_city, unvisited, pheromone, distances, alpha, beta
                )
                path.append(next_city)
                unvisited.remove(next_city)
                current_city = next_city

            path.append(0)  # Return to starting city
            all_paths.append(path)

        # Update pheromones and track the best path found
        pheromone, best_path, best_distance = update_pheromones(
            pheromone,
            all_paths,
            distances,
            q,
            evaporation_rate,
            best_path,
            best_distance,
        )

    return best_path, best_distance


if __name__ == "__main__":
    # Example usage
    best_path, best_distance = ant_colony_optimization(
        cities=cities,
        ants_num=10,
        iterations=100,
        alpha=1.0,
        beta=5.0,
        evaporation_rate=0.7,
        q=10,
    )

    print(f"Best path: {best_path}")
    print(f"Best distance: {best_distance}")
