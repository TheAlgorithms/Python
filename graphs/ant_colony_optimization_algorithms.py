"""
A simple example uses the ant colony optimization algorithm
to solve the classic TSP problem.
The travelling salesman problem (TSP) asks the following question:
"Given a list of cities and the distances between each pair of cities,
 what is the shortest possible route that visits each city exactly once
 and returns to the origin city?"

https://en.wikipedia.org/wiki/Ant_colony_optimization_algorithms
https://en.wikipedia.org/wiki/Travelling_salesman_problem

Author: Clark
"""

import copy
import random


def main(
    cities: dict[int, list[int]],
    ants_num: int,
    iterations_num: int,
    pheromone_evaporation: float,
    alpha: float,
    beta: float,
    q: float,  # Pheromone system parameters Q，which is a constant
) -> tuple[list[int], float]:
    """
    Ant colony algorithm main function
    >>> cities = {0:[0,0],1:[2,2]}
    >>> ANTS_NUM = 5
    >>> ITERATIONS_NUM = 5
    >>> PHEROMONE_EVAPORATION = 0.7
    >>> ALPHA = 1.0
    >>> BETA = 5.0
    >>> Q = 10
    >>> main(cities,ANTS_NUM,ITERATIONS_NUM,PHEROMONE_EVAPORATION,ALPHA,BETA,Q)
    ([0, 1, 0], 5.656854249492381)
    """
    # Initialize the pheromone matrix
    cities_num = len(cities)
    pheromone = [[1.0] * cities_num] * cities_num

    best_path: list[int] = []
    best_distance = float("inf")
    for _ in range(iterations_num):
        ants_route = []
        for _ in range(ants_num):
            unvisited_cities = copy.deepcopy(cities)
            current_city = {next(iter(cities.keys())): next(iter(cities.values()))}
            del unvisited_cities[next(iter(current_city.keys()))]
            ant_route = [next(iter(current_city.keys()))]
            while unvisited_cities:
                current_city, unvisited_cities = city_select(
                    pheromone, current_city, unvisited_cities, alpha, beta
                )
                ant_route.append(next(iter(current_city.keys())))
            ant_route.append(0)
            ants_route.append(ant_route)

        pheromone, best_path, best_distance = pheromone_update(
            pheromone,
            cities,
            pheromone_evaporation,
            ants_route,
            q,
            best_path,
            best_distance,
        )
    return best_path, best_distance


def distance(city1: list[int], city2: list[int]) -> float:
    """
    Calculate the distance between two coordinate points
    >>> distance([0,0], [3,4] )
    5.0
    """
    return (((city1[0] - city2[0]) ** 2) + ((city1[1] - city2[1]) ** 2)) ** 0.5


def pheromone_update(
    pheromone: list[list[float]],
    cities: dict[int, list[int]],
    pheromone_evaporation: float,
    ants_route: list[list[int]],
    q: float,  # Pheromone system parameters Q，which is a constant
    best_path: list,
    best_distance: float,
) -> tuple[list[list[float]], list, float]:
    """
    Update pheromones on the route and update the best route
    >>> pheromone = [[1.0,1.0],[1.0,1.0]]
    >>> cities = {0:[0,0],1:[2,2]}
    >>> PHEROMONE_EVAPORATION = 0.7
    >>> ants_route = [[0,1,0]]
    >>> Q = 10
    >>> best_path = []
    >>> best_distance = float("inf")
    >>> pheromone_update(
    ... pheromone,cities,PHEROMONE_EVAPORATION,ants_route,Q,best_path,best_distance
    ... )
    ([[0.7, 4.235533905932737], [4.235533905932737, 0.7]], [0, 1, 0], 5.656854249492381)
    """
    for a in range(len(cities)):  # Update the volatilization of pheromone on all routes
        for b in range(len(cities)):
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
    pheromone: list[list[float]],
    current_city: dict[int, list[int]],
    unvisited_cities: dict[int, list[int]],
    alpha: float,
    beta: float,
) -> tuple[dict[int, list[int]], dict[int, list[int]]]:
    """
    Choose the next city for ants
    >>> pheromone = [[1.0,1.0],[1.0,1.0]]
    >>> current_city = {0:[0,0]}
    >>> unvisited_cities = {1:[2,2]}
    >>> ALPHA = 1.0
    >>> BETA = 5.0
    >>> city_select(pheromone,current_city,unvisited_cities,ALPHA,BETA)
    ({1: [2, 2]}, {})
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
    Q = 10.0  # Pheromone system parameters Q，which is a constant

    best_path, best_distance = main(
        cities, ANTS_NUM, ITERATIONS_NUM, PHEROMONE_EVAPORATION, ALPHA, BETA, Q
    )

    print(f"{best_path = }")
    print(f"{best_distance = }")
