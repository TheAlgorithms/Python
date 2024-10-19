# BFS, DFS, A* search, Uniform cost, Greedy search
# implementing searches for tree search

from collections import deque
import heapq

# Define the weighted graph as a dictionary
weighted_graph = {
    'S': {'A': 3, 'B': 1},
    'A': {'S': 3, 'B': 2, 'C': 2},
    'B': {'C': 3, 'S': 1, 'A': 2},
    'C': {'A': 2, 'D': 4, 'B': 3, 'G': 4},
    'D': {'C': 4, 'G': 1},
    'G': {'D': 1, 'C': 4}
}   

# BREADTH FIRST SEARCH
def breadth_first_search(graph, start, goal):
    queue = deque([(start, [start])])  # Queue of (node, path) tuples
    visited = set()

    while queue:
        current_node, path = queue.popleft()

        if current_node == goal:
            return path  # Path found

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None  # No valid path found



# Start and goal nodes
start_node = 'S'
goal_node = 'G'

# Find the breadth-first search path
bfs_path = breadth_first_search(weighted_graph, start_node, goal_node)

if bfs_path:
    print("-------------------------------------------------------------")
    print("Breadth First Search:", ' -> '.join(bfs_path))
    print()
else:
    print("No valid path found from 'S' to 'G' using Breadth-First Search.")
    
# DEPTH  FIRST SEARCH
def depth_first_search(graph, node, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(node)
    path.append(node)

    for neighbor in graph.get(node, {}):
        if neighbor not in visited:
            depth_first_search(graph, neighbor, visited, path)

    return path

# Perform DFS starting from node 'S'
dfs_path = depth_first_search(weighted_graph, 'S')

if dfs_path:
    
    print("Depth First Search:", ' -> '.join(dfs_path))
    print()
else:
    print("No valid path found using Depth-First Search.")

# UNIFORM COST SEARCH
def Uniform_Cost_Search(graph, start, goal):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            path = []
            while previous_nodes[current_node] is not None:
                path.insert(0, current_node)  # Insert node at the beginning of the path
                current_node = previous_nodes[current_node]
            path.insert(0, start)  # Insert start node at the beginning of the path
            return distances[goal], path

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            total_cost = current_distance + weight
            if total_cost < distances[neighbor]:
                distances[neighbor] = total_cost
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (total_cost, neighbor))

    return float('infinity'), []  # Goal not reachable
least_uniform_cost_to_G, path_to_G = Uniform_Cost_Search(weighted_graph, 'S', 'G')


print("Least Uniform Cost:", least_uniform_cost_to_G)
print("Uniform Cost Search:", ' -> '.join(path_to_G))
print()

# GREEDY SEARCH
def Greedy_Search(graph, start, goal, heuristic):
    visited = set()
    path = []
    current_node = start
    
    while current_node != goal:
        if current_node in visited:
            return None  
        
        path.append(current_node)
        visited.add(current_node)
        neighbors = graph[current_node]
        if not neighbors:
            return None  # No neighbors, cannot proceed
        current_node = min(neighbors, key=lambda node: neighbors[node] + heuristic[node])  # Greedy path
        
    path.append(goal)
    return path
    
     # Heuristic values
heuristics = {'S': 7, 'B': 7, 'A': 5, 'C': 4, 'D': 1, 'G': 0}


path = Greedy_Search(weighted_graph, 'S', 'G', heuristics)

if path:

    print("Greedy Search:", ' -> '.join(path))
else:
    print("No valid path found from 'S' to 'G' using Greedy Search.")


 # A* SEARCH
def A_Star_Search(graph, start, goal, heuristic):
    open_set = [(0, start)]  # Priority queue: (f(n), node)
    g_values = {node: float('infinity') for node in graph}
    g_values[start] = 0
    came_from = {}  # Initialize the dictionary to store parent nodes

    while open_set:
        f, current_node = heapq.heappop(open_set)

        if current_node == goal:
            # Path found
            path = []
            while current_node != start:
                path.insert(0, current_node)  # Insert node at the beginning of the path
                current_node = came_from[current_node]
            path.insert(0, start)
            return path

        for neighbor, weight in graph.get(current_node, {}).items():
            tentative_g = g_values[current_node] + weight
            if tentative_g < g_values.get(neighbor, float('infinity')):
                
                # This path to the neighbor is better than any previous one
                g_values[neighbor] = tentative_g
                f = tentative_g + heuristic.get(neighbor, 0)  # Use 0 as default heuristic value if not provided
                heapq.heappush(open_set, (f, neighbor))
                came_from[neighbor] = current_node

    return None  


start_node = 'S'
goal_node = 'G'


path = A_Star_Search(weighted_graph, start_node, goal_node, heuristics)

if path:
    print()
    print("A* Search:", ' -> '.join(path))
    print("-------------------------------------------------------------")
else:
    print("No valid path found from 'S' to 'G' using A* Search.")
