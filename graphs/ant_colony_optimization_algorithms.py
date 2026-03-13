"""
Use an ant colony optimization algorithm to solve the travelling salesman problem (TSP)
which asks the following question:
"Given a list of cities and the distances between each pair of cities, what is the
 shortest possible route that visits each city exactly once and returns to the origin
 city?"

https://en.wikipedia.org/wiki/Ant_colony_optimization_algorithms
https://en.wikipedia.org/wiki/Travelling_salesman_problem

Author: Clark
"""

import copy
import random

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


def main(
    cities: dict[int, list[int]],
    ants_num: int,
    iterations_num: int,
    pheromone_evaporation: float,
    alpha: float,
    beta: float,
    q: float,  # Pheromone system parameters Q, which is a constant
) -> tuple[list[int], float]:
    """
    Ant colony algorithm main function
    >>> main(cities=cities, ants_num=10, iterations_num=20,
    ...      pheromone_evaporation=0.7, alpha=1.0, beta=5.0, q=10)
    ([0, 1, 2, 3, 4, 5, 6, 7, 0], 37.909778143828696)
    >>> main(cities={0: [0, 0], 1: [2, 2]}, ants_num=5, iterations_num=5,
    ...      pheromone_evaporation=0.7, alpha=1.0, beta=5.0, q=10)
    ([0, 1, 0], 5.656854249492381)
    >>> main(cities={0: [0, 0], 1: [2, 2], 4: [4, 4]}, ants_num=5, iterations_num=5,
    ...      pheromone_evaporation=0.7, alpha=1.0, beta=5.0, q=10)
    Traceback (most recent call last):
      ...
    IndexError: list index out of range
    >>> main(cities={}, ants_num=5, iterations_num=5,
    ...      pheromone_evaporation=0.7, alpha=1.0, beta=5.0, q=10)
    Traceback (most recent call last):
      ...
    StopIteration
    >>> main(cities={0: [0, 0], 1: [2, 2]}, ants_num=0, iterations_num=5,
    ...      pheromone_evaporation=0.7, alpha=1.0, beta=5.0, q=10)
    ([], inf)
    >>> main(cities={0: [0, 0], 1: [2, 2]}, ants_num=5, iterations_num=0,
    ...      pheromone_evaporation=0.7, alpha=1.0, beta=5.0, q=10)
    ([], inf)
    >>> main(cities={0: [0, 0], 1: [2, 2]}, ants_num=5, iterations_num=5,
    ...      pheromone_evaporation=1, alpha=1.0, beta=5.0, q=10)
    ([0, 1, 0], 5.656854249492381)
    >>> main(cities={0: [0, 0], 1: [2, 2]}, ants_num=5, iterations_num=5,
    ...      pheromone_evaporation=0, alpha=1.0, beta=5.0, q=10)
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
    >>> distance([0, 0], [3, 4] )
    5.0
    >>> distance([0, 0], [-3, 4] )
    5.0
    >>> distance([0, 0], [-3, -4] )
    5.0
    """
    return (((city1[0] - city2[0]) ** 2) + ((city1[1] - city2[1]) ** 2)) ** 0.5


def pheromone_update(
    pheromone: list[list[float]],
    cities: dict[int, list[int]],
    pheromone_evaporation: float,
    ants_route: list[list[int]],
    q: float,  # Pheromone system parameters Q, which is a constant
    best_path: list[int],
    best_distance: float,
) -> tuple[list[list[float]], list[int], float]:
    """
    Update pheromones on the route and update the best route
    >>>
    >>> pheromone_update(pheromone=[[1.0, 1.0], [1.0, 1.0]],
    ...                  cities={0: [0,0], 1: [2,2]}, pheromone_evaporation=0.7,
    ...                  ants_route=[[0, 1, 0]], q=10, best_path=[],
    ...                  best_distance=float("inf"))
    ([[0.7, 4.235533905932737], [4.235533905932737, 0.7]], [0, 1, 0], 5.656854249492381)
    >>> pheromone_update(pheromone=[],
    ...                  cities={0: [0,0], 1: [2,2]}, pheromone_evaporation=0.7,
    ...                  ants_route=[[0, 1, 0]], q=10, best_path=[],
    ...                  best_distance=float("inf"))
    Traceback (most recent call last):
      ...
    IndexError: list index out of range
    >>> pheromone_update(pheromone=[[1.0, 1.0], [1.0, 1.0]],
    ...                  cities={}, pheromone_evaporation=0.7,
    ...                  ants_route=[[0, 1, 0]], q=10, best_path=[],
    ...                  best_distance=float("inf"))
    Traceback (most recent call last):
      ...
    KeyError: 0
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
    >>> city_select(pheromone=[[1.0, 1.0], [1.0, 1.0]], current_city={0: [0, 0]},
    ...             unvisited_cities={1: [2, 2]}, alpha=1.0, beta=5.0)
    ({1: [2, 2]}, {})
    >>> city_select(pheromone=[], current_city={0: [0,0]},
    ...             unvisited_cities={1: [2, 2]}, alpha=1.0, beta=5.0)
    Traceback (most recent call last):
      ...
    IndexError: list index out of range
    >>> city_select(pheromone=[[1.0, 1.0], [1.0, 1.0]], current_city={},
    ...             unvisited_cities={1: [2, 2]}, alpha=1.0, beta=5.0)
    Traceback (most recent call last):
      ...
    StopIteration
    >>> city_select(pheromone=[[1.0, 1.0], [1.0, 1.0]], current_city={0: [0, 0]},
    ...             unvisited_cities={}, alpha=1.0, beta=5.0)
    Traceback (most recent call last):
      ...
    IndexError: list index out of range
    """
    probabilities = []
    for city, value in unvisited_cities.items():
        city_distance = distance(value, next(iter(current_city.values())))
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
    best_path, best_distance = main(
        cities=cities,
        ants_num=10,
        iterations_num=20,
        pheromone_evaporation=0.7,
        alpha=1.0,
        beta=5.0,
        q=10,
    )

    print(f"{best_path = }")
    print(f"{best_distance = }")
