import random
import networkx as nx
import numpy as np

def create_random_graph(num_nodes):
    """
    Create a random graph for the Traveling Salesman Problem (TSP).

    Args:
        num_nodes (int): Number of nodes in the graph.

    Returns:
        nx.Graph: A random graph with node distances.
    """
    G = nx.Graph()
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            distance = random.randint(1, 100)  # Random distances for the TSP
            G.add_edge(i, j, weight=distance)
    return G

def ant_colony_optimization(graph, num_ants, num_iterations, evaporation_rate, alpha, beta):
    """
    Solve the Traveling Salesman Problem (TSP) using Ant Colony Optimization (ACO).

    Args:
        graph (nx.Graph): Graph representing the TSP with distances.
        num_ants (int): Number of ants (solutions to build).
        num_iterations (int): Number of iterations (epochs).
        evaporation_rate (float): Rate of pheromone evaporation.
        alpha (float): Pheromone influence factor.
        beta (float): Distance influence factor.

    Returns:
        list: Best path found by ACO.
        float: Distance of the best path.
    """
    num_nodes = len(graph.nodes)
    pheromone_matrix = np.ones((num_nodes, num_nodes))  # Initialize pheromone levels
    best_path = None
    best_distance = float('inf')

    for _ in range(num_iterations):
        for ant in range(num_ants):
            start_node = random.randint(0, num_nodes - 1)
            current_node = start_node
            path = [current_node]
            distance = 0

            unvisited_nodes = set(range(num_nodes))
            unvisited_nodes.remove(current_node)

            while unvisited_nodes:
                probabilities = []
                total_prob = 0

                for node in unvisited_nodes:
                    pheromone = pheromone_matrix[current_node][node]
                    distance = graph[current_node][node]["weight"]
                    probability = (pheromone ** alpha) * ((1 / distance) ** beta)
                    probabilities.append(probability)
                    total_prob += probability

                probabilities = [p / total_prob for p in probabilities]
                next_node = np.random.choice(list(unvisited_nodes), p=probabilities)
                path.append(next_node)
                distance += graph[current_node][next_node]["weight"]
                current_node = next_node
                unvisited_nodes.remove(current_node)

            if distance < best_distance:
                best_path = path
                best_distance = distance

            # Update pheromone levels
            for i in range(num_nodes):
                for j in range(i + 1, num_nodes):
                    pheromone_matrix[i][j] *= (1 - evaporation_rate)
                    pheromone_matrix[j][i] = pheromone_matrix[i][j]
            for i in range(num_nodes - 1):
                j = i + 1
                pheromone_matrix[path[i]][path[j]] += 1 / distance
                pheromone_matrix[path[j]][path[i]] = pheromone_matrix[path[i]][path[j]

    return best_path, best_distance

if __name__ == "__main__":
    num_nodes = 10
    num_ants = 10
    num_iterations = 100
    evaporation_rate = 0.1
    alpha = 1
    beta = 2

    graph = create_random_graph(num_nodes)
    best_path, best_distance = ant_colony_optimization(graph, num_ants, num_iterations, evaporation_rate, alpha, beta)
    print("Best path:", best_path)
    print("Best distance:", best_distance)
