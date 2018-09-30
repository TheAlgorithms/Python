import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import from_levels_and_colors

plt.ion()

'''
Simulation parameters
obstacle_prob: controls the frequency of obstacles, set to 0 for no obstacles
m, n: number of rows and columns, respectively
start_node: initial position
goal_node: goal position
'''
obstacle_prob = 0.2
m, n = 25, 25
start_node = (0, 0)
goal_node = (m-1, n-1)

colors = ['white', 'black', 'red', 'pink', 'yellow', 'green', 'orange']
levels = [0, 1, 2, 3, 4, 5, 6, 7]

cmap, norm = from_levels_and_colors(levels, colors)

grid = np.int8(np.random.random((m, n)) > (1-obstacle_prob))
grid[start_node] = 4
grid[goal_node] = 5

parent_map = [[() for _ in range(n)] for _ in range(m)]
distance_map = np.full((m, n), np.inf)
distance_map[start_node] = 0

while True:
    grid[start_node] = 4
    grid[goal_node] = 5

    current_node = np.unravel_index(np.argmin(distance_map, axis=None), distance_map.shape)
    min_distance = np.min(distance_map)
    if (current_node == goal_node) or np.isinf(min_distance):
        break

    grid[current_node] = 2
    distance = distance_map[current_node]
    distance_map[current_node] = np.inf

    i, j = current_node[0], current_node[1]

    neighbors = []
    if i-1 >= 0: 
        neighbors.append((i-1, j))
    if i+1 < m:
        neighbors.append((i+1, j))
    if j-1 >= 0:
        neighbors.append((i, j-1))
    if j+1 < n:
        neighbors.append((i, j+1))

    for neighbor in neighbors:
        if grid[neighbor] == 0 or grid[neighbor] == 5:
            distance_map[neighbor] = distance + 1
            parent_map[neighbor[0]][neighbor[1]] = current_node
            grid[neighbor] = 3

    plt.cla()
    plt.imshow(grid, cmap=cmap, norm=norm, interpolation=None)
    plt.show()
    plt.pause(1e-5)

if np.isinf(distance_map[goal_node]):
    print("No route found.")
else:
    route = [goal_node]
    while parent_map[route[0][0]][route[0][1]] is not ():
        route.insert(0, parent_map[route[0][0]][route[0][1]])

    print("The route found covers %d grid cells." % len(route))
    for i in range(1, len(route)):
        grid[route[i]] = 6
        plt.cla()
        plt.imshow(grid, cmap=cmap, norm=norm, interpolation=None)
        plt.show()
        plt.pause(0.1)