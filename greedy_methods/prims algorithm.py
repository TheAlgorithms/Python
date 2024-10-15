def prims_algorithm(n, cost):
    visited = [0] * (n + 1)  # Initialize visited array
    visited[1] = 1  # Start from the first vertex
    mincost = 0
    ne = 1  # Number of edges in the spanning tree

    print("The edges of the spanning tree are:")

    while ne < n:
        min_cost = float('inf')
        a = b = -1  # Initialize edge endpoints

        for i in range(1, n + 1):
            if visited[i]:  # Check only visited vertices
                for j in range(1, n + 1):
                    if not visited[j] and cost[i][j] < min_cost:
                        min_cost = cost[i][j]
                        a, b = i, j

        if a != -1 and b != -1:  # Ensure valid edge found
            print(f"{ne}: edge({a}, {b}) = {min_cost}\t")
            mincost += min_cost
            visited[b] = 1
            ne += 1
