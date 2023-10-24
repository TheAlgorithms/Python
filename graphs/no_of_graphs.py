def no_of_graphs(n):
    ## no of edges for given n vertices would be: n*(n-1)/2 (undirected graph)
    edges = n * (n - 1) / 2
    return pow(2, edges)


if __name__ == "__main__":
    n = input("Enter no of vertices")
    n = int(n)
    graphs = no_of_graphs(n)
    print(f"possible graphs for {n} vertices are {graphs}:")
