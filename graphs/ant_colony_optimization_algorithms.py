"""
A simple example uses the ant colony optimization algorithm
to solve the classic TSP problem
https://en.wikipedia.org/wiki/Ant_colony_optimization_algorithms
Author: Clark
"""

import copy
import random


def distance(city1: list[int], city2: list[int]) -> float:
    """
    Calculate the distance between two coordinate points
    >>> distance([0,0],[3,4] )
    5.0
    """
    return (((city1[0] - city2[0]) ** 2) + ((city1[1] - city2[1]) ** 2)) ** 0.5


def pheromone_update(
    pheromone: list[list],
    cities: dict[int, list[int]],
    pheromone_evaporation: float,
    ants_route: list[list[int]],
    q: float,
    best_path: list,
    best_distance: float,
) -> tuple[list[list], list, float]:
    """
    Update pheromones on the route and update the best route
    """
    for a in range(cities_num):  # Update the volatilization of pheromone on all routes
        for b in range(cities_num):
            pheromone[a][b] *= pheromone_evaporation
    for ant_route in ants_route:
        total_distance = 0.0
        for i in range(len(ant_route) - 1):  # Calculate total distance
            total_distance += distance(cities[ant_route[i]], cities[ant_route[i + 1]])
        delta_pheromone = q / total_distance
        for i in range(len(ant_route) - 1):  # Update pheromones
            pheromone[ant_route[i]][ant_route[i + 1]] += delta_pheromone
            pheromone[ant_route[i + 1]][ant_route[i]] = pheromone[ant_route[i]][
                ant_route[i + 1]
            ]

        if total_distance < best_distance:
            best_path = ant_route
            best_distance = total_distance

    return pheromone, best_path, best_distance


def city_select(
    pheromone: list[list[int]],
    current_city: dict[int, list[int]],
    unvisited_cities: dict[int, list[int]],
    alpha: float,
    beta: float,
) -> tuple[dict[int, list[int]], dict[int, list[int]]]:
    """
    Choose the next city for ants
    """
    probabilities = []
    for city in unvisited_cities:
        city_distance = distance(
            unvisited_cities[city], next(iter(current_city.values()))
        )
        probability = (pheromone[city][next(iter(current_city.keys()))] ** alpha) * (
            (1 / city_distance) ** beta
        )
        probabilities.append(probability)

    chosen_city_i = random.choices(
        list(unvisited_cities.keys()), weights=probabilities
    )[0]
    chosen_city = {chosen_city_i: unvisited_cities[chosen_city_i]}
    del unvisited_cities[next(iter(chosen_city.keys()))]
    return chosen_city, unvisited_cities


if __name__ == "__main__":
    # City coordinates for TSP problem
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

    # Parameter settings
    ANTS_NUM = 10  # Number of ants
    ITERATIONS_NUM = 20  # Number of iterations
    PHEROMONE_EVAPORATION = 0.7  # Pheromone volatilization coefficient,
    # the larger the number, the greater the pheromone retention in each generation.
    ALPHA = 1.0
    BETA = 5.0
    Q = 10.0  # Pheromone system parameters Q

    # Initialize the pheromone matrix
    cities_num = len(cities)
    pheromone = [[1] * cities_num] * cities_num

    best_path: list[int] = []
    best_distance = float("inf")
    for _ in range(ITERATIONS_NUM):
        ants_route = []
        for _ in range(ANTS_NUM):
            unvisited_cities = copy.deepcopy(cities)
            current_city = {next(iter(cities.keys())): next(iter(cities.values()))}
            del unvisited_cities[next(iter(current_city.keys()))]
            ant_route = [next(iter(current_city.keys()))]
            while unvisited_cities:
                current_city, unvisited_cities = city_select(
                    pheromone, current_city, unvisited_cities, ALPHA, BETA
                )
                ant_route.append(next(iter(current_city.keys())))
            ant_route.append(0)
            ants_route.append(ant_route)

        pheromone, best_path, best_distance = pheromone_update(
            pheromone,
            cities,
            PHEROMONE_EVAPORATION,
            ants_route,
            Q,
            best_path,
            best_distance,
        )

    print("Best Path:", best_path)
    print("Best Distance:", best_distance)
