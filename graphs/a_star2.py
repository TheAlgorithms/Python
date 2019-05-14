from heapq import heappush, heappop


def manhattan_distance(node1, node2):
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])


def euclidean_distance(node1, node2):
    return ((abs(node1[0] - node2[0])) ** 2 + (abs(node1[1] - node2[1])) ** 2) ** .5


def get_neighbors(graph, node):
    neighbors = {(-1, 0), (0, 1), (1, 0), (0, -1)}
    neighborsFound = set()

    for neighbor in neighbors:
        try:
            y = node[1] + neighbor[1]
            x = node[0] + neighbor[0]
            if x == -1 or y == -1:
                continue
            elif graph[y][x] >= 1:
                neighborsFound.add((x, y))
        except IndexError:  # does nothing on index errors
            continue

    return neighborsFound


def getCost(graph, node):
    return graph[node[1]][node[0]]


def a_star(graph, start, goal):
    closed = set()
    distance = {}
    heap = []
    path = []

    heappush(heap, (0, start))
    distance[start] = (0, (None))

    while len(heap) != 0:
        currentCost, current = heappop(heap)

        if current in closed:
            continue

        if current == goal:
            cost, temp = distance[current]
            totalCost = 0
            path.append(current)

            while temp != None:
                path.append(temp)
                totalCost += cost
                cost, temp = distance[temp]
            return (totalCost, path[::-1])

        for neighbor in get_neighbors(graph, current):
            if neighbor in closed:
                continue

            nodeCost = getCost(graph, neighbor)
            endDistance = (manhattan_distance(neighbor, goal) ** .6)

            if neighbor not in closed or distance[neighbor][0] > nodeCost:
                distance[neighbor] = (nodeCost, current)
                heappush(heap, ((nodeCost + currentCost + endDistance), neighbor))
        closed.add(current)


graph1 = [
    [1, 1, -1, 1, 1],
    [1, 1, -1, 1, 1],
    [1, 1, 25, 9, 1],
    [1, -1, -1, 1, 1],
    [1, 1, -1, 1, 7],
    [12, 1, 50, 1, 1],
    [1, 1, 39, 1, 1],
]
graph2 = [
    [1, 1, -1, 1, 1],
    [1, 1, -1, 1, 1],
    [1, 1, 1, 9, 1],
    [1, -1, -1, 1, 1],
    [1, 1, -1, 1, 7],
    [12, 1, 50, 1, 1],
    [1, 1, 39, 1, 1],
]
graph3 = [
    [1, 1, -1, 1, 1],
    [1, 1, -1, 1, 1],
    [1, 1, 25, 9, 1],
    [1, -1, -1, 1, 1],
    [1, 1, -1, 1, 7],
    [12, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
]
graph4 = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [-1, -1, -1, -1, -1, -1, -1, 1],
    [1, 1, 1, 1, 1, 1, -1, 1],
    [1, 1, 1, 1, 1, 1, -1, 1],
    [1, 1, 1, 1, 1, 1, -1, 1],
    [1, 1, 1, 1, 1, 1, -1, 1],
    [1, 1, 1, 1, 1, 1, -1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],

]
start = (0, 0)
goal = (4, 0)

print(a_star(graph1, start, goal), '\n')
print(a_star(graph2, start, goal), '\n')
print(a_star(graph3, start, goal), '\n')
print(a_star(graph4, (0, 8), (7, 0)), '\n')
