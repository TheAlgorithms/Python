import heapq


def tsp(cost):
    """
    https://www.geeksforgeeks.org/dsa/approximate-solution-for-travelling-salesman-problem-using-mst/

    Problem definition:
    Given a 2d matrix cost[][] of size n where cost[i][j] denotes the cost of moving from city i to city j.
    The task is to complete a tour from city 0 to all other towns such that we visit each city exactly once
    and then return to city 0 at minimum cost.

    Both the Naive and Dynamic Programming solutions for this problem are infeasible.
    In fact, there is no polynomial time solution available for this problem as it is a known NP-Hard problem.

    There are approximate algorithms to solve the problem though; for example, the Minimum Spanning Tree (MST) based
    approximation algorithm defined below which gives a solution that is at most twice the cost of the optimal solution.

    Assumptions:
    1. The graph is complete.

    2. The problem instance satisfies Triangle-Inequality.(The least distant path to reach a vertex j from i is always to reach j
    directly from i, rather than through some other vertex k)

    3. The cost matrix is symmetric, i.e., cost[i][j] = cost[j][i]

    Time complexity: O(n ^ 3), the time complexity of triangleInequality() function is O(n ^ 3) as we are using 3 nested loops.
    Space Complexity: O(n ^ 2), to store the adjacency list, and creating MST.

    """
    # create the adjacency list
    adj = createList(cost)

    # check for triangle inequality violations
    if triangleInequality(adj):
        print("Triangle Inequality Violation")
        return -1

    # construct the travelling salesman tour
    tspTour = approximateTSP(adj)

    # calculate the cost of the tour
    tspCost = tourCost(tspTour)

    return tspCost


# function to implement approximate TSP
def approximateTSP(adj):
    n = len(adj)

    # to store the cost of minimum spanning tree
    mstCost = [0]

    # stores edges of minimum spanning tree
    mstEdges = findMST(adj, mstCost)

    # to mark the visited nodes
    visited = [False] * n

    # create adjacency list for mst
    mstAdj = [[] for _ in range(n)]
    for e in mstEdges:
        mstAdj[e[0]].append([e[1], e[2]])
        mstAdj[e[1]].append([e[0], e[2]])

    # to store the eulerian tour
    tour = []
    eulerianCircuit(mstAdj, 0, tour, visited, -1)

    # add the starting node to the tour
    tour.append(0)

    # to store the final tour path
    tourPath = []

    for i in range(len(tour) - 1):
        u = tour[i]
        v = tour[i + 1]
        weight = 0

        # find the weight of the edge u -> v
        for neighbor in adj[u]:
            if neighbor[0] == v:
                weight = neighbor[1]
                break

        # add the edge to the tour path
        tourPath.append([u, v, weight])

    return tourPath


def tourCost(tour):
    cost = 0
    for edge in tour:
        cost += edge[2]
    return cost


def eulerianCircuit(adj, u, tour, visited, parent):
    visited[u] = True
    tour.append(u)

    for neighbor in adj[u]:
        v = neighbor[0]
        if v == parent:
            continue

        if visited[v] == False:
            eulerianCircuit(adj, v, tour, visited, u)


# function to find the minimum spanning tree
def findMST(adj, mstCost):
    n = len(adj)

    # to marks the visited nodes
    visited = [False] * n

    # stores edges of minimum spanning tree
    mstEdges = []

    pq = []
    heapq.heappush(pq, [0, 0, -1])

    while pq:
        current = heapq.heappop(pq)

        u = current[1]
        weight = current[0]
        parent = current[2]

        if visited[u]:
            continue

        mstCost[0] += weight
        visited[u] = True

        if parent != -1:
            mstEdges.append([u, parent, weight])

        for neighbor in adj[u]:
            v = neighbor[0]
            if v == parent:
                continue
            w = neighbor[1]

            if not visited[v]:
                heapq.heappush(pq, [w, v, u])
    return mstEdges


# function to calculate if the
# triangle inequality is violated
def triangleInequality(adj):
    n = len(adj)

    # Sort each adjacency list based
    # on the weight of the edges
    for i in range(n):
        adj[i].sort(key=lambda a: a[1])

    # check triangle inequality for each
    # triplet of nodes (u, v, w)
    for u in range(n):
        for x in adj[u]:
            v = x[0]
            costUV = x[1]
            for y in adj[v]:
                w = y[0]
                costVW = y[1]
                for z in adj[u]:
                    if z[0] == w:
                        costUW = z[1]
                        if (costUV + costVW < costUW) and (u < w):
                            return True
    # no violations found
    return False


# function to create the adjacency list
def createList(cost):
    n = len(cost)

    # to store the adjacency list
    adj = [[] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            # if there is no edge between u and v
            if cost[u][v] == 0:
                continue
            # add the edge to the adjacency list
            adj[u].append([v, cost[u][v]])

    return adj


if __name__ == "__main__":
    # test
    cost = [[0, 1000, 5000], [5000, 0, 1000], [1000, 5000, 0]]

    print(tsp(cost))
