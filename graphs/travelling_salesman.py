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
    adj = create_list(cost)
 
    #check for triangle inequality violations
    if triangle_inequality(adj):
        print("Triangle Inequality Violation")
        return -1

    # construct the travelling salesman tour
    tsp_tour = approximate_tsp(adj)
 
    # calculate the cost of the tour
    tsp_cost = tour_cost(tsp_tour)
 
    return tsp_cost


# function to implement approximate TSP
def approximate_tsp(adj):
    n = len(adj)

    # to store the cost of minimum spanning tree
    mst_cost = [0]
 
    # stores edges of minimum spanning tree
    mst_edges = find_mst(adj, mst_cost)
 
    # to mark the visited nodes
    visited = [False] * n

    # create adjacency list for mst
    mst_adj = [[] for _ in range(n)]
    mst_edges = find_mst(adj, mst_cost)
    for e in mst_edges:
        mst_adj[e[0]].append([e[1], e[2]])
        mst_adj[e[1]].append([e[0], e[2]])
 
    # to store the eulerian tour
    tour = []
    eulerian_circuit(mst_adj, 0, tour, visited, -1)
 
    # add the starting node to the tour
    tour.append(0)

    # to store the final tour path
    tour_path = []
 
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
        tour_path.append([u, v, weight])
 
    return tour_path

def tour_cost(tour):
    cost = 0
    for edge in tour:
        cost += edge[2]
    return cost


def eulerian_circuit(adj, u, tour, visited, parent):
    visited[u] = True
    tour.append(u)

    for neighbor in adj[u]:
        v = neighbor[0]
        if v == parent:
            continue

        if visited[v] == False:
            eulerian_circuit(adj, v, tour, visited, u)
 
# function to find the minimum spanning tree
def find_mst(adj, mst_cost):
    n = len(adj)

    # to marks the visited nodes
    visited = [False] * n

    # stores edges of minimum spanning tree
    mst_edges = []
 
    pq = []
    heapq.heappush(pq, [0, 0, -1])

    while pq:
        current = heapq.heappop(pq)

        u = current[1]
        weight = current[0]
        parent = current[2]

        if visited[u]:
            continue
 
        mst_cost[0] += weight
        visited[u] = True

        if parent != -1:
            mst_edges.append([u, parent, weight])
 
        for neighbor in adj[u]:
            v = neighbor[0]
            if v == parent:
                continue
            w = neighbor[1]

            if not visited[v]:
                heapq.heappush(pq, [w, v, u])
    return mst_edges
 


# function to calculate if the
# triangle inequality is violated
def triangle_inequality(adj):
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
            cost_UV = x[1]
            for y in adj[v]:
                w = y[0]
                cost_VW = y[1]
                for z in adj[u]:
                    if z[0] == w:
                        cost_UW = z[1]
                        if (cost_UV + cost_VW < cost_UW) and (u < w):
                            return True
    # no violations found
    return False


# function to create the adjacency list
def create_list(cost):
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
