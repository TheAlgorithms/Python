def prims_algorithm(n, cost):
    visited = [0] * (n + 1)  # Initialize visited array
    visited[1] = 1  # Start from the first vertex
    mincost = 0
    ne = 1  # Number of edges in the spanning tree

    print("The edges of the spanning tree are:")

    while ne < n:
        min_cost = float('inf')
        a = u = b = v = -1  # Initialize variables

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if cost[i][j] < min_cost:
                    if visited[i] == 0:
                        continue
                    else:
                        min_cost = cost[i][j]
                        a = u = i
                        b = v = j

        if visited[u] == 0 or visited[v] == 0:
            print(f"{ne}: edge({a}, {b}) = {min_cost}\t")
            mincost += min_cost
            visited[b] = 1
            ne += 1

        cost[a][b] = cost[b][a] = float('inf')  # Mark the edge as processed

    print(f"\nMinimum cost is {mincost}")


if __name__ == "__main__":
    n = int(input("Enter the number of vertices in the graph: "))
    cost = [[0] * (n + 1) for _ in range(n + 1)]

    print("Enter the cost matrix of the graph:")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                cost[i][j] = 0  # No self-loop
            else:
                cost[i][j] = int(input(f"({i},{j}): "))
                if cost[i][j] == 0:
                    cost[i][j] = float('inf')  # Use inf for no connection

    prims_algorithm(n, cost)
