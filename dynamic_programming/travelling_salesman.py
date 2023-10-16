import numpy as np

"""Author: grpathak22
Date: 15 October 2023
Travelling Salesman Problem using Dynamic Programming """


def travelling_salesman(tsp_graph: np.ndarray, city: int) -> None:
    """
    Solve the traveling salesman problem using dynamic programming.
    Args:
      distance_matrix: A square matrix of distances between cities.
      city: Starting city which is initially 0(index)
    Returns:
      None
    """
    global cost
    adjacent_vertex, min_val = 999, 999
    visited[city] = 1
    print((city + 1), end=" ")
    for k in range(num_cities):
        if (visited[k] == 0) and (tsp_graph[city][k] != 0):
            if tsp_graph[city][k] < min_val:
                min_val = tsp_graph[city][k]
                adjacent_vertex = k
    if min_val != 999:
        cost = cost + min_val
    if adjacent_vertex == 999:
        adjacent_vertex = 0
        print((adjacent_vertex + 1), end=" ")
        cost = cost + tsp_graph[city][adjacent_vertex]
        return
    travelling_salesman(tsp_graph, adjacent_vertex)


"""
1)Initialize a set of visited cities to be empty.
2)Set the current city to be the starting city.
3)While there are still unvisited cities:
    Find the closest unvisited city to the current city.
    Visit the closest unvisited city and add it to the set of visited cities.
    Set the current city to be the closest unvisited city.
4)Return to the starting city.
The code also keeps track of the total distance traveled,
The total distance is calculated by adding up the distances.
Once the code has finished executing,
it will print the shortest possible path and the total distance of the path."""


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    cost = 0
    tsp_graph = np.array(
        [[0, 22, 26, 30], [30, 0, 45, 35], [25, 45, 0, 60], [30, 35, 40, 0]]
    )
    num_cities = len(tsp_graph[0])
    city = 0
    visited = np.zeros(num_cities, dtype=int)
    print("Shortest Path:  \n", end=" ")
    travelling_salesman(tsp_graph, city)
    print(f"\nMinimum Cost: {cost} ", end=" ")
